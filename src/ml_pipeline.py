def clean_data(df):

    y = df.purchase
    X = df[["v2", "v3"]]

    return X, y