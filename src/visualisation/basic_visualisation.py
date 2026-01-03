import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_price_distribution(df_berlin_clean):
    plt.figure(figsize=(7, 7))
    sns.histplot(df_berlin_clean['Price'], kde=True, bins=50)
    plt.title('Distribution of Accommodation Prices in Berlin')
    plt.xlabel('Price (€)')
    plt.ylabel('Frequency')
    plt.show()

def plot_ratings_vs_price(df_berlin_clean):
    plt.figure(figsize=(18, 6))
    plt.subplot(1, 2, 2)
    sns.scatterplot(x='Guest Satisfaction', y='Price', data=df_berlin_clean, alpha=0.6)
    plt.title('Price vs. Guest Satisfaction')
    plt.xlabel('Guest Satisfaction')
    plt.ylabel('Price (€)')
    plt.tight_layout()
    plt.show()

def plot_avg_rating_distribution(df_customers_clean):
    plt.figure(figsize=(10, 6))
    sns.histplot(df_customers_clean['avg_rating'], bins=20, kde=True, color='salmon')
    plt.title('Distribution of Average Ratings')
    plt.xlabel('Rating')
    plt.ylabel('Frequency')
    plt.show()

def plot_customers_by_district(df_customers):
    plt.figure(figsize=(12, 6))
    district_counts = df_customers['district'].value_counts().sort_values(ascending=False)
    sns.barplot(x=district_counts.index, y=district_counts.values, palette='viridis')
    plt.title('Number of Customers per District')
    plt.xlabel('District')
    plt.ylabel('Customer Count')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()
