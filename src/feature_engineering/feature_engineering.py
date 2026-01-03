import numpy as np
import pandas as pd

def engineer_customer_features(df_customers):
    LAT_CENTER, LON_CENTER = 52.5163, 13.3777
    df = df_customers.copy()
    df['dist_to_center_km'] = np.sqrt(
        (df['latitude'] - LAT_CENTER)**2 + (df['longitude'] - LON_CENTER)**2
    ) * 111
    df['join_date'] = pd.to_datetime(df['join_date'])
    df['tenure_days'] = (pd.Timestamp.now() - df['join_date']).dt.days
    return df

# Add more feature engineering functions as needed
