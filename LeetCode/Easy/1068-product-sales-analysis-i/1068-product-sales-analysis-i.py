import pandas as pd

def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(product, sales, on='product_id', how= 'right')
    return merged[['product_name','year','price']]