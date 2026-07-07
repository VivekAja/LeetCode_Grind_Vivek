import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    unique = employee["salary"].drop_duplicates().sort_values(ascending = False)
    if len(unique) >= 2:
        sec = unique.iloc[1]
    else:
        sec= None
    return pd.DataFrame({'SecondHighestSalary': [sec]})
    