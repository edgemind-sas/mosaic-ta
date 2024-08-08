import plotly.express as px
import statsmodels.api as sm
import argparse

parser = argparse.ArgumentParser(description='Logistic Regression')
parser.add_argument('-b', '--buy_threshold', type=float, default=0, help='buy_threshold is the return threshold for buying')
parser.add_argument('-l', '--logit_value_threshold', type=float, default=0.5, help='logit_value_threshold is the value threshold for the logit for buying')
args = parser.parse_args()

if args.buy_threshold is None:
    raise ValueError('No buy_threshold provided.')

target_train = target_train.apply(lambda x: 1 if x > args.buy_threshold else 0)

train = sm.Logit(target_train, features_train_df)
train_res = train.fit(disp=0)
# train_res.summary()

target_pred = train_res.predict(features_test_df)

buy_thresh = args.logit_value_threshold
idx_pred_buy = target_pred > buy_thresh
idx_pred_sell = idx_pred_buy.shift(k_horizon).fillna(False)

quote_init = 1
quote_trade_invest = 1/k_horizon

trades_df = \
    backtest_fix_sell(
        ohlcv_test_df,
        idx_buy=idx_pred_buy,
        idx_sell=idx_pred_sell,
        quote_init=quote_init,
        quote_trade_invest=quote_trade_invest,
        base_name="BTC",
        quote_name="USDT",
        )

print(f"k: {k_horizon} - {trades_df['USDT:perf'].iloc[-1]}")

# #perf = trades_trades["USDT:balance"].cumsum().rename("perf")
# fig_perf = \
#     px.line(trades_df["USDT:perf"], title=f"Modèle 2 : Performance de la stratégie",
#             labels=dict(
#                 value="Performance"))
# fig_perf.update_layout(showlegend=False)
# fig_perf.update_yaxes(range=[0, trades_df["USDT:perf"].max()*1.05])
# fig_perf.update_traces(line=dict(width=5))
#
