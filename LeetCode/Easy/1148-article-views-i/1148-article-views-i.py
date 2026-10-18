import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    result_df = views[views['author_id'] == views['viewer_id']].copy()
    result_df = result_df.sort_values(by='author_id')
    result_df = result_df.drop_duplicates(subset='author_id')
    result_df = result_df.rename(columns={'author_id': 'id'})
    return result_df[['id']]