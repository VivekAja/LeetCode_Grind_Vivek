import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    next_num = logs['num'].shift(-1)
    next_next_num = logs['num'].shift(-2)

    con = (logs['num'] == next_num) & (logs['num'] == next_next_num)

    result = logs[con]['num'].drop_duplicates().to_frame()
    return result.rename(columns = {'num':'ConsecutiveNums'})