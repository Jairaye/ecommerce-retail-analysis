import pandas as pd
import numpy as np

# Load the v2 dataset (multi-order version)
df = pd.read_csv('ecommerce_customer_behavior_dataset_v2.csv')

print("✅ Data loaded successfully!")
print(f"Total records: {len(df)}")
print(f"\nColumns: {df.columns.tolist()}")
print(f"\nFirst few rows:")
print(df.head())

# ==========================================
# STEP 1: Convert Currency (TRY → USD)
# ==========================================
# Average TRY to USD rate during 2023-2024: ~0.035
EXCHANGE_RATE = 0.035

df['Unit_Price_USD'] = (df['Unit_Price'] * EXCHANGE_RATE).round(2)
df['Discount_Amount_USD'] = (df['Discount_Amount'] * EXCHANGE_RATE).round(2)
df['Total_Amount_USD'] = (df['Total_Amount'] * EXCHANGE_RATE).round(2)

# Drop original TRY columns
df = df.drop(['Unit_Price', 'Discount_Amount', 'Total_Amount'], axis=1)

# Rename USD columns to standard names
df = df.rename(columns={
    'Unit_Price_USD': 'Unit_Price',
    'Discount_Amount_USD': 'Discount_Amount',
    'Total_Amount_USD': 'Total_Amount'
})

print("\n✅ Currency conversion complete (TRY → USD)")
print(f"Average transaction: ${df['Total_Amount'].mean():.2f}")

# ==========================================
# STEP 2: Map Turkish Cities to US Cities
# ==========================================
turkish_to_us_cities = {
    'Istanbul': 'New York',
    'Ankara': 'Los Angeles',
    'Izmir': 'Chicago',
    'Bursa': 'Houston',
    'Antalya': 'Phoenix',
    'Adana': 'Philadelphia',
    'Gaziantep': 'San Antonio',
    'Konya': 'San Diego',
    'Kayseri': 'Dallas',
    'Mersin': 'San Jose'
}

df['City'] = df['City'].map(turkish_to_us_cities)

print("\n✅ Cities mapped to US locations")
print(f"Cities: {df['City'].unique()}")

# ==========================================
# STEP 3: Adjust Payment Methods
# ==========================================
print(f"\nOriginal payment methods: {df['Payment_Method'].unique()}")

us_payment_map = {
    'Credit Card': 'Credit Card',
    'Debit Card': 'Debit Card',
    'PayPal': 'PayPal',
    'Bank Transfer': 'ACH Transfer',
    'Cash on Delivery': 'Buy Now Pay Later'
}

df['Payment_Method'] = df['Payment_Method'].map(
    lambda x: us_payment_map.get(x, x)
)

print(f"Updated payment methods: {df['Payment_Method'].unique()}")

# ==========================================
# STEP 4: Save Transformed Dataset
# ==========================================
output_filename = 'us_retail_ecommerce_data.csv'
df.to_csv(output_filename, index=False)

print(f"\n✅ Data transformation complete!")
print(f"✅ Saved to: {output_filename}")
print(f"\n📊 Final Dataset Summary:")
print(f"   - Total records: {len(df):,}")
print(f"   - Unique customers: {df['Customer_ID'].nunique():,}")
print(f"   - Date range: {df['Date'].min()} to {df['Date'].max()}")
print(f"   - Total revenue: ${df['Total_Amount'].sum():,.2f}")
print(f"   - Average transaction: ${df['Total_Amount'].mean():.2f}")
print(f"   - Product categories: {df['Product_Category'].nunique()}")

print(f"\n🎯 Ready for analysis!")