import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from ..feature_engineering.feature_engineering import engineer_customer_features

def clean_accommodation_data(df):
    df_berlin = df[df['City'] == 'Berlin']
    df_berlin_copy = df_berlin.copy().drop(columns=['City'])
    for col in ['Shared Room', 'Private Room', 'Superhost']:
        df_berlin_copy[col] = df_berlin_copy[col].astype(int)
    categorical_cols = ['Day', 'Room Type']
    ohe = OneHotEncoder(sparse_output=False)
    one_hot_features = ohe.fit_transform(df_berlin_copy[categorical_cols])
    df_one_hot = pd.DataFrame(one_hot_features, columns=ohe.get_feature_names_out(categorical_cols), index=df_berlin_copy.index)
    df_berlin_numeric_and_bool = df_berlin_copy.drop(columns=categorical_cols)
    df_berlin_encoded = pd.concat([df_berlin_numeric_and_bool, df_one_hot], axis=1)
    cols_to_scale = [
        'Price', 'Person Capacity', 'Cleanliness Rating', 'Guest Satisfaction',
        'Bedrooms', 'City Center (km)', 'Metro Distance (km)',
        'Attraction Index', 'Normalised Attraction Index',
        'Restraunt Index', 'Normalised Restraunt Index'
    ]
    scaler = StandardScaler()
    df_berlin_clean = df_berlin_encoded.copy()
    def remove_outliers(df, column):
        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        return df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]
    df_berlin_clean = remove_outliers(df_berlin_clean, 'Price')
    df_berlin_clean[cols_to_scale] = scaler.fit_transform(df_berlin_clean[cols_to_scale])
    return df_berlin_clean

def clean_customer_data(df_customers):
    df = engineer_customer_features(df_customers)
    df['avg_rating'] = df['avg_rating'].fillna(df['avg_rating'].median())
    df['verification'] = df['verification'].fillna('Unknown')
    categorical_cols = ['district', 'verification', 'country']
    df = pd.get_dummies(df, columns=categorical_cols, drop_first=True, dtype=int)
    df = df.drop(columns=['customer_id', 'latitude', 'longitude', 'join_date'])
    numerical_cols = ['lifetime_bookings', 'avg_rating', 'cancellation_rate', 'tenure_days', 'dist_to_center_km']
    scaler = StandardScaler()
    df[numerical_cols] = scaler.fit_transform(df[numerical_cols])
    return df
