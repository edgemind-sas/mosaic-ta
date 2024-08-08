import pandas as pd
import pandas_ta as ta

ohlcv_df = pd.read_csv("btc_5m_2021_2022.csv.bz2",
                       compression="bz2",
                       index_col="time")

returns = pd.DataFrame(index=ohlcv_df.index)
for k in range(31):
    returns[f"r{k}"] = ohlcv_df["close"].pct_change(k+1).shift(-k)

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


