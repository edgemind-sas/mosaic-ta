import os
import sys
import tqdm
import time
import numpy as np
import datetime
import pandas as pd
import plotly.io as pio

import pkg_resources
installed_pkg = {pkg.key for pkg in pkg_resources.working_set}
if 'ipdb' in installed_pkg:
    import ipdb  # noqa: F401
import importlib

# Custom remote librairies
import mosaic
import mosaic.utils as mut
import mosaic.backtest as mbt
import mosaic.bot as mbo
import mosaic.database as mdd
import mosaic.decision_model as mdm
# Reload librairies in dev phase
importlib.reload(mosaic)
importlib.reload(mut)
importlib.reload(mbt)
importlib.reload(mbo)
importlib.reload(mdd)
importlib.reload(mdm)

# TO BE ADAPTED IF NEEDED : Custom data PATH
ONLINE_MODE = False

if ONLINE_MODE:
    client = mdd.DbClient(org="edgemind",
                          url="http://callisto.edgemind.net:2086",
                          token="-KRSutWAsQmri3hF8-g4HfD7EPLW1cAPU3k5ygRraETU5EHt846ibwN7LFjR53eK3X_djjvoaFfIUNk0UbT9GQ==")

DATA_PATH = os.path.join("..", "data")
FIG_PATH = os.path.join("..", "fig")

config = {
    "collection": "crypto",
    "name": "ohlcv",
    "tags": {
        "period": "5m",
        "exchange": "binance",
        "base": "BTC",
        "quote": "USDT",
    },
    "values": ["open", "high", "low", "close", "volume"],
    "start_date": '2021-01-01 00:00:00',
    "stop_date": '2023-01-01 00:00:00',
}

source = mdd.InfluxDataSource(**config)

source_filename = os.path.join(
    DATA_PATH,
    f"{source.get_str_info()}_"\
    f"{config['start_date']}_{config['stop_date']}.csv.bz2")

if os.path.exists(source_filename) or (not ONLINE_MODE):
    ohlcv_df = pd.read_csv(source_filename,
                              index_col="time",
                              parse_dates=["time"])
else:

    ohlcv_df = \
        client.get_data(source,
                        start=config["start_date"],
                        stop=config["stop_date"])

    ohlcv_df.to_csv(source_filename,
                    index=True)

print("Data loaded")

dm = mdm.DML_RSI2(
        offset=1,
        params={
            "window": 10,
            "buy_level": 15,
            "sell_level": 95,
        })

# We suppose ohlcv_df is a DataFrame of OHLCV data.
signals = dm.compute(ohlcv_df)
# We can concat signals values with indicators value to check if computation is as expected
indic_signals_df = pd.concat([dm.indic_s, signals], axis=1)
indic_signals_df

fig = dm.plotly(ohlcv_df.head(300), layout={"title": "Signaux du DM RSI"})
fig.show()

bot = mbo.BotLong(decision_model=dm)

bot.run_test(ohlcv_df)

bot.perf_test

bot.trades_test

fig = bot.plotly_test(layout={"title": "Performance de la stratégie RSI simple"})
fig

fig_filename = "bot_rsi_simple.html"
fig.write_html(fig_filename)
