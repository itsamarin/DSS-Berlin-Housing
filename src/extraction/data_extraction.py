import kagglehub
import os
import pandas as pd
import uuid
import numpy as np

def download_airbnb_dataset(save_to_original=True):
    download_dir = kagglehub.dataset_download("dipeshkhemani/airbnb-cleaned-europe-dataset")
    file_name = 'Aemf1.csv'
    file_path = os.path.join(download_dir, file_name)
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Expected file '{file_name}' not found in {download_dir}")
    df = pd.read_csv(file_path)
    if save_to_original:
        original_dir = os.path.join(os.path.dirname(__file__), '..', 'data', 'original')
        os.makedirs(original_dir, exist_ok=True)
        df.to_csv(os.path.join(original_dir, file_name), index=False)
    return df

def generate_customers_csv(n_customers=2000, output_path=None):
    # synthetic data generation
    districts = ['Mitte', 'Pankow', 'Charlottenburg-Wilmersdorf', 'Friedrichshain-Kreuzberg',
                 'Neukölln', 'Tempelhof-Schöneberg', 'Lichtenberg', 'Spandau', 'Steglitz-Zehlendorf']
    LAT_CENTER, LON_CENTER = 52.5163, 13.3777
    data = {
        'customer_id': [str(uuid.uuid4())[:8].upper() for _ in range(n_customers)],
        'join_date': pd.to_datetime(np.random.choice(pd.date_range('2015-01-01', '2024-12-31'), n_customers)),
        'district': np.random.choice(districts, n_customers),
        'latitude': np.random.uniform(52.4, 52.6, n_customers),
        'longitude': np.random.uniform(13.2, 13.5, n_customers),
        'verification': np.random.choice(['Verified', 'Partial', 'None'], n_customers, p=[0.7, 0.2, 0.1]),
        'country': np.random.choice(['USA', 'CAN', 'UK', 'GER', 'FRA', 'AUS', 'JPN', 'BRA'], n_customers),
        'lifetime_bookings': np.random.negative_binomial(1, 0.1, n_customers),
        'avg_rating': np.round(np.clip(np.random.normal(4.8, 0.3, n_customers), 1.0, 5.0), 2),
        'cancellation_rate': np.round(np.random.uniform(0, 0.15, n_customers), 3),
        'is_business_traveler': np.random.choice([0, 1], n_customers, p=[0.8, 0.2])
    }
    df_customers = pd.DataFrame(data)
    if output_path is None:
        original_dir = os.path.join(os.path.dirname(__file__), '..', 'data', 'original')
        os.makedirs(original_dir, exist_ok=True)
        output_path = os.path.join(original_dir, 'airbnb_customers.csv')
    df_customers.to_csv(output_path, index=False)
    return df_customers
