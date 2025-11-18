

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Set random seed for reproducibility
np.random.seed(42)
random.seed(42)


def generate_marketing_data():
    """Generate 16 months of marketing campaign data"""

    print("🚀 Starting data generation...")

    # Date range: July 2024 - October 2025 (16 months)
    start_date = datetime(2024, 7, 1)
    end_date = datetime(2025, 10, 31)
    date_range = pd.date_range(start=start_date, end=end_date, freq='D')

    # Marketing channels
    channels = [
        'Google Ads', 'Facebook Ads', 'Instagram Ads', 'LinkedIn Ads',
        'Email Marketing', 'Organic Search', 'Display Ads', 'YouTube Ads',
        'Twitter Ads', 'TikTok Ads', 'Affiliate Marketing', 'Referral'
    ]

    # Campaign types
    campaign_types = [
        'Brand Awareness', 'Lead Generation', 'Product Launch',
        'Retargeting', 'Seasonal Promotion', 'Flash Sale'
    ]

    # Products
    products = [
        'Premium Plan', 'Basic Plan', 'Enterprise Plan',
        'Starter Kit', 'Add-on Service'
    ]

    # Initialize data list
    data = []
    total_rows = 0

    # Generate daily campaign data for each channel
    for date in date_range:
        month = date.month
        day_of_week = date.weekday()

        # Seasonal multipliers
        if month in [11, 12]:  # Holiday season
            seasonal_mult = 1.4
        elif month in [6, 7, 8]:  # Summer
            seasonal_mult = 0.85
        elif month in [1, 2]:  # New Year
            seasonal_mult = 1.2
        else:
            seasonal_mult = 1.0

        # Weekend effect (lower engagement)
        weekend_mult = 0.7 if day_of_week >= 5 else 1.0

        for channel in channels:
            # Channel-specific performance
            performance = get_channel_performance(channel)

            # Apply seasonal and weekend multipliers
            impressions = int(performance['impressions'] * seasonal_mult * weekend_mult)
            clicks = int(performance['clicks'] * seasonal_mult * weekend_mult)
            conversions = int(performance['conversions'] * seasonal_mult * weekend_mult)
            spend = performance['spend'] * seasonal_mult * weekend_mult
            avg_order_value = performance['avg_order_value']

            # Calculate revenue
            revenue = conversions * avg_order_value * np.random.uniform(0.9, 1.1)

            # Random campaign type and product
            campaign_type = random.choice(campaign_types)
            product = random.choice(products)

            # Append row
            data.append({
                'date': date.strftime('%Y-%m-%d'),
                'channel': channel,
                'campaign_type': campaign_type,
                'product': product,
                'impressions': impressions,
                'clicks': clicks,
                'conversions': conversions,
                'spend': round(spend, 2),
                'revenue': round(revenue, 2)
            })
            total_rows += 1

        # Progress indicator
        if total_rows % 1000 == 0:
            print(f"   Generated {total_rows:,} rows...")

    # Create DataFrame
    print(f"\n📊 Creating DataFrame with {total_rows:,} rows...")
    df = pd.DataFrame(data)

    # Calculate metrics
    print("🔢 Calculating marketing metrics...")
    df['ctr'] = (df['clicks'] / df['impressions'] * 100).round(2)
    df['conversion_rate'] = (df['conversions'] / df['clicks'] * 100).round(2)
    df['cac'] = (df['spend'] / df['conversions']).round(2)
    df['roas'] = (df['revenue'] / df['spend']).round(2)
    df['profit'] = (df['revenue'] - df['spend']).round(2)

    # Replace infinities and NaN
    df = df.replace([np.inf, -np.inf], 0)
    df = df.fillna(0)

    # Save to CSV
    output_path = 'data/marketing_campaigns.csv'
    df.to_csv(output_path, index=False)

    # Print summary
    print(f"\n✅ SUCCESS! Generated {len(df):,} rows")
    print(f"📅 Date range: {df['date'].min()} to {df['date'].max()}")
    print(f"💰 Total spend: ${df['spend'].sum():,.2f}")
    print(f"💵 Total revenue: ${df['revenue'].sum():,.2f}")
    print(f"📈 Overall ROAS: {(df['revenue'].sum() / df['spend'].sum()):.2f}x")
    print(f"📁 Saved to: {output_path}")

    # Generate channel summary
    print("\n" + "=" * 60)
    print("📊 CHANNEL PERFORMANCE SUMMARY")
    print("=" * 60)

    channel_summary = df.groupby('channel').agg({
        'spend': 'sum',
        'revenue': 'sum',
        'conversions': 'sum',
        'impressions': 'sum',
        'clicks': 'sum'
    }).round(2)

    channel_summary['roas'] = (channel_summary['revenue'] / channel_summary['spend']).round(2)
    channel_summary['cac'] = (channel_summary['spend'] / channel_summary['conversions']).round(2)
    channel_summary['conversion_rate'] = (
            channel_summary['conversions'] / channel_summary['clicks'] * 100
    ).round(2)

    print(channel_summary.sort_values('roas', ascending=False).to_string())

    return df


def get_channel_performance(channel):
    """Define realistic performance characteristics for each channel"""

    profiles = {
        'Google Ads': {
            'impressions': np.random.randint(8000, 15000),
            'ctr': np.random.uniform(0.03, 0.05),
            'conv_rate': np.random.uniform(0.08, 0.12),
            'spend': np.random.uniform(800, 1500),
            'avg_order_value': np.random.uniform(120, 180)
        },
        'Facebook Ads': {
            'impressions': np.random.randint(12000, 20000),
            'ctr': np.random.uniform(0.02, 0.04),
            'conv_rate': np.random.uniform(0.05, 0.09),
            'spend': np.random.uniform(600, 1200),
            'avg_order_value': np.random.uniform(90, 140)
        },
        'Instagram Ads': {
            'impressions': np.random.randint(10000, 18000),
            'ctr': np.random.uniform(0.025, 0.045),
            'conv_rate': np.random.uniform(0.04, 0.08),
            'spend': np.random.uniform(500, 1000),
            'avg_order_value': np.random.uniform(80, 120)
        },
        'LinkedIn Ads': {
            'impressions': np.random.randint(3000, 6000),
            'ctr': np.random.uniform(0.015, 0.03),
            'conv_rate': np.random.uniform(0.10, 0.15),
            'spend': np.random.uniform(900, 1800),
            'avg_order_value': np.random.uniform(200, 350)
        },
        'Email Marketing': {
            'impressions': np.random.randint(15000, 25000),
            'ctr': np.random.uniform(0.15, 0.25),
            'conv_rate': np.random.uniform(0.08, 0.14),
            'spend': np.random.uniform(100, 300),
            'avg_order_value': np.random.uniform(110, 160)
        },
        'Organic Search': {
            'impressions': np.random.randint(20000, 35000),
            'ctr': np.random.uniform(0.04, 0.08),
            'conv_rate': np.random.uniform(0.10, 0.16),
            'spend': 0,  # Organic = no ad spend
            'avg_order_value': np.random.uniform(100, 150)
        },
        'Display Ads': {
            'impressions': np.random.randint(25000, 40000),
            'ctr': np.random.uniform(0.01, 0.02),
            'conv_rate': np.random.uniform(0.02, 0.05),
            'spend': np.random.uniform(700, 1300),
            'avg_order_value': np.random.uniform(85, 130)
        },
        'YouTube Ads': {
            'impressions': np.random.randint(15000, 25000),
            'ctr': np.random.uniform(0.015, 0.03),
            'conv_rate': np.random.uniform(0.04, 0.08),
            'spend': np.random.uniform(800, 1400),
            'avg_order_value': np.random.uniform(95, 145)
        },
        'Twitter Ads': {
            'impressions': np.random.randint(8000, 14000),
            'ctr': np.random.uniform(0.02, 0.035),
            'conv_rate': np.random.uniform(0.03, 0.06),
            'spend': np.random.uniform(400, 800),
            'avg_order_value': np.random.uniform(75, 115)
        },
        'TikTok Ads': {
            'impressions': np.random.randint(18000, 30000),
            'ctr': np.random.uniform(0.025, 0.045),
            'conv_rate': np.random.uniform(0.03, 0.07),
            'spend': np.random.uniform(600, 1100),
            'avg_order_value': np.random.uniform(70, 110)
        },
        'Affiliate Marketing': {
            'impressions': np.random.randint(5000, 10000),
            'ctr': np.random.uniform(0.04, 0.07),
            'conv_rate': np.random.uniform(0.08, 0.13),
            'spend': np.random.uniform(300, 700),
            'avg_order_value': np.random.uniform(100, 150)
        },
        'Referral': {
            'impressions': np.random.randint(3000, 7000),
            'ctr': np.random.uniform(0.05, 0.10),
            'conv_rate': np.random.uniform(0.12, 0.18),
            'spend': np.random.uniform(50, 200),
            'avg_order_value': np.random.uniform(120, 180)
        }
    }

    profile = profiles[channel]
    impressions = profile['impressions']
    clicks = int(impressions * profile['ctr'])
    conversions = int(clicks * profile['conv_rate'])

    return {
        'impressions': impressions,
        'clicks': clicks,
        'conversions': conversions,
        'spend': profile['spend'],
        'avg_order_value': profile['avg_order_value']
    }


if __name__ == '__main__':
    # Generate the data
    df = generate_marketing_data()

    print("\n✨ Data generation complete! Next step: SQL analysis")