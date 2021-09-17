import pandas as pd
import numpy as np

def score(df, promo_pred_col = 'promotion'):
    n_treat       = df.loc[df[promo_pred_col],:].shape[0]
    n_control     = df.loc[~df[promo_pred_col],:].shape[0]
    n_treat_purch = df.loc[df[promo_pred_col], 'purchase'].sum()
    n_ctrl_purch  = df.loc[~df[promo_pred_col], 'purchase'].sum()
    irr = n_treat_purch / n_treat - n_ctrl_purch / n_control
    nir = 10 * n_treat_purch - 0.15 * n_treat - 10 * n_ctrl_purch
    return (irr, nir)
    

def test_results(promotion_strategy):
    test_data = pd.read_csv('../data/processed/test.csv')
    df = test_data[['v1', 'v2', 'v3', 'v4', 'v5', 'v6', 'v7']]
    promos = promotion_strategy(df)
    score_df = test_data.iloc[np.where(promos)]    
    irr, nir = score(score_df)
    print("Nice job!  See how well your strategy worked on our test data below!")
    print()
    print('Your irr with this strategy is {:0.4f}.'.format(irr))
    print()
    print('Your nir with this strategy is {:0.2f}.'.format(nir))
    
    print("We came up with a model with an irr of {} and an nir of {} on the test set.\n\n How did you do?".format(0.0188, 189.45))
    return irr, nir
