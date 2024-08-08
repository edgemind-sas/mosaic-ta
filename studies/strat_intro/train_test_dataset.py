import pandas as pd
import statsmodels.api as sm
import argparse

parser = argparse.ArgumentParser(description='Get train and test sets.')
parser.add_argument('-k', '--k_horizon', type=int, help='k_horizon')
args = parser.parse_args()

if args.k_horizon is None:
    raise ValueError('No k_horizon provided.')

k_horizon = args.k_horizon
var_target = f"r{args.k_horizon}"
data_all = pd.concat([indics_df.shift(1), returns], axis=1).dropna()
target = data_all[var_target]

var_features = list(indics_df.columns)

pct_train = 0.7
nb_train = int(pct_train*len(data_all))

data_all_train = data_all.iloc[:nb_train]
data_all_test = data_all.iloc[nb_train:]

target_train = data_all_train[var_target]
target_test = data_all_test[var_target]

features_train_df = sm.add_constant(data_all_train[var_features])
features_test_df = sm.add_constant(data_all_test[var_features])

ohlcv_train_df = ohlcv_df.loc[data_all_train.index]
ohlcv_test_df = ohlcv_df.loc[data_all_test.index]

