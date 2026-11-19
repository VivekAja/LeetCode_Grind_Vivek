import pandas as pd

def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    merged_df = employee.merge(bonus, how = "left", on= "empId")
    mask = merged_df[(merged_df["bonus"]< 1000) | (merged_df["bonus"].isna())]
    return mask[["name","bonus"]]