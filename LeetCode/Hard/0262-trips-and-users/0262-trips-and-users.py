import pandas as pd

def trips_and_users(trips: pd.DataFrame, users: pd.DataFrame) -> pd.DataFrame:
    unbanned_users = users[users['banned'] == 'No']['users_id']
    valid_date = trips['request_at'].between("2013-10-01","2013-10-03")
    active_client = trips['client_id'].isin(unbanned_users)
    active_driver = trips['driver_id'].isin(unbanned_users)

    clean_trips = trips[valid_date & active_client & active_driver]

    if clean_trips.empty:
        return pd.DataFrame(columns=['Day', 'Cancellation Rate'])
    canned = clean_trips['status'].str.startswith('cancelled')

    rates = clean_trips[canned].groupby('request_at').size() / clean_trips.groupby('request_at').size()

    rates = rates.fillna(0).round(2)

    result = rates.reset_index()
    result.columns = ['Day', 'Cancellation Rate']

    return result

