import os

from src.extraction.data_extraction import download_airbnb_dataset, generate_customers_csv
from src.cleaning.data_cleaning import clean_accommodation_data, clean_customer_data
from src.visualisation.basic_visualisation import (
    plot_price_distribution,
    plot_ratings_vs_price,
    plot_avg_rating_distribution,
    plot_customers_by_district
)

def main():
    # Data Extraction
    df = download_airbnb_dataset()
    df_customers = generate_customers_csv()

    # Data Cleaning
    df_berlin_clean = clean_accommodation_data(df)
    df_customers_clean = clean_customer_data(df_customers)

    # Save cleaned data
    cleaned_dir = os.path.join(os.path.dirname(__file__), 'data', 'cleaned')
    os.makedirs(cleaned_dir, exist_ok=True)
    df_berlin_clean.to_csv(os.path.join(cleaned_dir, 'Aemf1_cleaned.csv'), index=False)
    df_customers_clean.to_csv(os.path.join(cleaned_dir, 'airbnb_customers_cleaned.csv'), index=False)
    print("Data cleaning and wrangling complete. The final dataset has been saved in 'data/cleaned'.")

    # Basic Visualisation
    plot_price_distribution(df_berlin_clean)
    plot_ratings_vs_price(df_berlin_clean)
    plot_avg_rating_distribution(df_customers_clean)
    plot_customers_by_district(df_customers)

if __name__ == "__main__":
    main()