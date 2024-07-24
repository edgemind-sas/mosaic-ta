import pandas as pd
import plotly.express as px
import pandas_ta as ta
import statsmodels.api as sm

ohlcv_df = pd.read_csv("btc_5m_2021_2022.csv.bz2",
                       compression="bz2",
                       index_col="time")

k_horizon = 12
returns = ohlcv_df["close"].pct_change(k_horizon+1).shift(-k_horizon).rename(f"r{k_horizon}")

# Features
indics_df = pd.DataFrame(index=ohlcv_df.index)

indics_df.ta.rsi(close=ohlcv_df["close"], length=5, append=True)
indics_df.ta.rsi(close=ohlcv_df["close"], length=10, append=True)
indics_df.ta.rsi(close=ohlcv_df["close"], length=30, append=True)
indics_df

length_list = [5, 10, 30]
for length in length_list:
    indics_df.ta.mfi(close=ohlcv_df['close'],
                     high=ohlcv_df['high'],
                     low=ohlcv_df['low'],
                     volume=ohlcv_df['volume'],
                     length=length,
                     append=True)

var_target = f"r{k_horizon}"
data_all = pd.concat([indics_df.shift(1), returns], axis=1).dropna()
target = data_all[var_target]

var_features_mod2 = list(indics_df.columns)
features_mod2_df = sm.add_constant(data_all[var_features_mod2])

mod2 = sm.OLS(target, features_mod2_df)
mod2_res = mod2.fit()
# mod2_res.summary()

pct_train = 0.7
nb_train = int(pct_train*len(data_all))

data_all_train = data_all.iloc[:nb_train]
data_all_test = data_all.iloc[nb_train:]
target_train = data_all_train[var_target]
target_test = data_all_test[var_target]

ohlcv_train_df = ohlcv_df.loc[data_all_train.index]
ohlcv_test_df = ohlcv_df.loc[data_all_test.index]

def backtest_fix_sell(
        ohlcv_df,
        idx_buy,
        idx_sell,
        quote_init=1,
        quote_trade_invest=1,
        base_name="base",
        quote_name="quote",
        buy_on="open",
        sell_on="close",
        balance_on="close",
        ):
    
    trades_quote_ob = \
        pd.Series(0, index=ohlcv_df.index, name=f"{quote_name}:ob")
    trades_base_ob = \
        pd.Series(0, index=ohlcv_df.index, name=f"{base_name}:ob")

    trades_quote_ob[idx_buy] += -quote_trade_invest
    trades_base_ob[idx_buy] = \
        quote_trade_invest/ohlcv_df[buy_on]

    trades_base_os = \
        (-trades_base_ob.shift(k_horizon)\
         .rename(f"{base_name}:os"))\
         .fillna(0)
    trades_quote_os = \
        ((-trades_base_os)*\
         ohlcv_df[sell_on])\
         .rename(f"{quote_name}:os").fillna(0)

    trades_quote = (trades_quote_ob + trades_quote_os).rename(f"{quote_name}:o")
    trades_base = (trades_base_ob + trades_base_os).rename(f"{base_name}:o")
    trades_base_quote = \
        (trades_base*ohlcv_df.loc[trades_base.index, balance_on])\
        .rename(f"{base_name}-{quote_name}")
    trades_quote_balance = trades_quote + trades_base_quote
    trades_quote_balance.iloc[0] += quote_init
    trades_quote_balance = trades_quote_balance.cumsum().rename(f"{quote_name}:balance")

    trades_quote_perf = (trades_quote_balance/quote_init).rename(f"{quote_name}:perf")
    
    trades_df = pd.concat([
        trades_quote_ob,
        trades_base_ob,
        trades_quote_os,
        trades_base_os,
        trades_quote,
        trades_base,
        trades_base_quote,
        trades_quote_balance,
        trades_quote_perf,
    ], axis=1)

    return trades_df

features_mod2_train_df = sm.add_constant(data_all_train[var_features_mod2])
features_mod2_test_df = sm.add_constant(data_all_test[var_features_mod2])

mod2_train = sm.OLS(target_train, features_mod2_train_df)
mod2_train_res = mod2_train.fit()
mod2_train_res.summary()

mod2_target_pred = mod2_train_res.predict(features_mod2_test_df)

mod2_pred_mae = (mod2_target_pred - target_test).abs().mean()

buy_thresh = 0.00
idx_mod2_pred_buy = mod2_target_pred > buy_thresh
idx_mod2_pred_sell = idx_mod2_pred_buy.shift(k_horizon).fillna(False)

quote_init = 1
quote_trade_invest = 1/k_horizon

mod2_trades_df = \
    backtest_fix_sell(
        ohlcv_test_df,
        idx_buy=idx_mod2_pred_buy,
        idx_sell=idx_mod2_pred_sell,
        quote_init=quote_init,
        quote_trade_invest=quote_trade_invest,
        base_name="BTC",
        quote_name="USDT",
        )

#mod2_perf = mod2_trades_trades["USDT:balance"].cumsum().rename("perf")
fig_mod2_perf = \
    px.line(mod2_trades_df["USDT:perf"], title=f"Modèle 2 : Performance de la stratégie",
            labels=dict(
                value="Performance"))
fig_mod2_perf.update_layout(showlegend=False)
fig_mod2_perf.update_yaxes(range=[0, mod2_trades_df["USDT:perf"].max()*1.05])
fig_mod2_perf.update_traces(line=dict(width=5))
