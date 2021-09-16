def irr(df):
    """
    Calculates the Incremental Response Rate (IRR) for a given dataframe.

    Args:
        df: A pandas dataframe

    Returns:
        The IRR value
    """

    treat_rate = df[df.promotion].purchase.sum() / len(df[df.promotion])
    ctrl_rate = df[df.promotion == False].purchase.sum() / len(df[df.promotion == False])

    return treat_rate - ctrl_rate

def nir(df):
    """
    Calculates the Net Incremental Revenue (NIR) for a given dataframe.

    Args:
        df: A pandas dataframe

    Returns:
        The NIR value
    """

    return 10 * df[df.promotion].purchase.sum() - (0.15 * len(df[df.promotion])) - (10 * df[df.promotion == False].purchase.sum()) 