"""
SQL Analysis Script for Marketing Campaigns
Creates SQLite database and runs analysis queries
"""

import sqlite3
import pandas as pd
from pathlib import Path


def create_database():
    """Load CSV into SQLite database"""

    print("📊 Creating SQLite database...")

    # Read CSV
    df = pd.read_csv('data/marketing_campaigns.csv')

    # Create SQLite connection
    conn = sqlite3.connect('data/marketing_analysis.db')

    # Write to database
    df.to_sql('campaigns', conn, if_exists='replace', index=False)

    print(f"✅ Created database with {len(df):,} rows")

    conn.close()
    return True


def run_query(query_name, query_sql):
    """Execute SQL query and display results"""

    print(f"\n{'=' * 70}")
    print(f"📊 {query_name}")
    print('=' * 70)

    conn = sqlite3.connect('data/marketing_analysis.db')

    try:
        df = pd.read_sql_query(query_sql, conn)
        print(df.to_string(index=False))

        # Save to CSV
        output_file = f"data/analysis_{query_name.lower().replace(' ', '_')}.csv"
        df.to_csv(output_file, index=False)
        print(f"\n💾 Saved to: {output_file}")

    except Exception as e:
        print(f"❌ Error: {e}")

    conn.close()


def main():
    """Run all analysis queries"""

    # Create database
    create_database()

    # Query 1: Overall Performance Summary
    run_query("Overall Performance Summary", """
                                             SELECT COUNT(DISTINCT date)                as total_days,
                                                    COUNT(DISTINCT channel)             as total_channels,
                                                    SUM(impressions)                    as total_impressions,
                                                    SUM(clicks)                         as total_clicks,
                                                    SUM(conversions)                    as total_conversions,
                                                    ROUND(SUM(spend), 2)                as total_spend,
                                                    ROUND(SUM(revenue), 2)              as total_revenue,
                                                    ROUND(SUM(revenue) - SUM(spend), 2) as total_profit,
                                                    ROUND(AVG(ctr), 2)                  as avg_ctr,
                                                    ROUND(AVG(conversion_rate), 2)      as avg_conversion_rate,
                                                    ROUND(SUM(revenue) / SUM(spend), 2) as overall_roas
                                             FROM campaigns
                                             """)

    # Query 2: Channel Performance
    run_query("Channel Performance Comparison", """
                                                SELECT channel,
                                                       COUNT(*)                                                        as days_active,
                                                       SUM(impressions)                                                as impressions,
                                                       SUM(clicks)                                                     as clicks,
                                                       SUM(conversions)                                                as conversions,
                                                       ROUND(SUM(spend), 2)                                            as spend,
                                                       ROUND(SUM(revenue), 2)                                          as revenue,
                                                       ROUND(SUM(revenue) - SUM(spend), 2)                             as profit,
                                                       ROUND(SUM(spend) / SUM(conversions), 2)                         as cac,
                                                       ROUND(SUM(revenue) / SUM(spend), 2)                             as roas,
                                                       ROUND((CAST(SUM(conversions) AS FLOAT) / SUM(clicks)) * 100, 2) as conversion_rate
                                                FROM campaigns
                                                WHERE conversions > 0
                                                GROUP BY channel
                                                ORDER BY roas DESC
                                                """)

    # Query 3: Underperforming Campaigns
    run_query("Underperforming Campaigns (ROAS < 1.5)", """
                                                        SELECT channel,
                                                               campaign_type,
                                                               SUM(conversions)                                                  as conversions,
                                                               ROUND(SUM(spend), 2)                                              as spend,
                                                               ROUND(SUM(revenue), 2)                                            as revenue,
                                                               ROUND(SUM(revenue) / SUM(spend), 2)                               as roas,
                                                               ROUND((SUM(spend) / (SELECT SUM(spend) FROM campaigns)) * 100, 2) as pct_of_total_spend
                                                        FROM campaigns
                                                        WHERE spend > 0
                                                        GROUP BY channel, campaign_type
                                                        HAVING ROUND(SUM(revenue) / SUM(spend), 2) < 1.5
                                                        ORDER BY spend DESC LIMIT 10
                                                        """)

    # Query 4: Monthly Trends
    run_query("Monthly Trend Analysis", """
                                        SELECT strftime('%Y-%m', date) as month,
            SUM(impressions) as impressions,
            SUM(clicks) as clicks,
            SUM(conversions) as conversions,
            ROUND(SUM(spend), 2) as spend,
            ROUND(SUM(revenue), 2) as revenue,
            ROUND(SUM(revenue) / SUM(spend), 2) as roas,
            ROUND((CAST(SUM(conversions) AS FLOAT) / SUM(clicks)) * 100, 2) as conversion_rate
                                        FROM campaigns
                                        GROUP BY month
                                        ORDER BY month
                                        """)

    # Query 5: Top Performers
    run_query("Top Performing Campaigns (ROAS > 2.0)", """
                                                       SELECT channel,
                                                              campaign_type,
                                                              product,
                                                              SUM(conversions)                    as conversions,
                                                              ROUND(SUM(spend), 2)                as spend,
                                                              ROUND(SUM(revenue), 2)              as revenue,
                                                              ROUND(SUM(revenue) / SUM(spend), 2) as roas
                                                       FROM campaigns
                                                       WHERE spend > 0
                                                       GROUP BY channel, campaign_type, product
                                                       HAVING ROUND(SUM(revenue) / SUM(spend), 2) > 2.0
                                                       ORDER BY roas DESC LIMIT 15
                                                       """)

    print("\n" + "=" * 70)
    print("✅ ALL QUERIES COMPLETE!")
    print("=" * 70)
    print("\n📁 Results saved in data/ folder")
    print("🔍 Review CSV files for detailed analysis")


if __name__ == '__main__':
    main()