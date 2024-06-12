import pandas as pd
import numpy as np


def get_df(rows: int = 1000) -> pd.DataFrame:
    """
    Generate a pandas DataFrame from a list of random integers in the range of 0-100 as column a, and add a new column
    named b with the values being the modulo 10 of the number of column a.
    :param rows: How many rows to generate
    :return: Dataframe with columns a, b
    """
    dataframe = pd.DataFrame(np.random.randint(0, 100, rows), columns=['a'])

    # new column with values mapped to mod10 as column b
    dataframe['b'] = dataframe.map(lambda x: x % 10)

    return dataframe


if __name__ == '__main__':
    get_df()
