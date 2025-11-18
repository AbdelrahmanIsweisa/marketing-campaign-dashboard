"""
Dashboard Visualization Script
Creates interactive charts using Plotly
"""

import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots


def load_data():
    """Load marketing campaign data"""
    return pd.read_csv('data/marketing_campaigns.csv')


def create_channel_performance_chart(df):
    """Bar chart of ROAS by channel"""

    channel_perf = df.groupby('channel').agg({
        'spend': 'sum',
        'revenue': 'sum',
        'conversions': 'sum'
    }).reset_index()

    channel_perf['roas'] = (channel_perf['revenue'] / channel_perf['spend']).round(2)
    channel_perf = channel_perf.sort_values('roas', ascending=True)

    # Color code by performance
    colors = ['red' if x < 1.5 else 'yellow' if x < 2.0 else 'green'
              for x in channel_perf['roas']]

    fig = go.Figure(data=[
        go.Bar(
            y=channel_perf['channel'],
            x=channel_perf['roas'],
            orientation='h',
            marker=dict(color=colors),
            text=channel_perf['roas'],
            textposition='outside'
        )
    ])

    fig.update_layout(
        title='Channel Performance by ROAS',
        xaxis_title='Return on Ad Spend (ROAS)',
        yaxis_title='Channel',
        height=500
    )

    fig.write_html('dashboards/channel_performance.html')
    print("✅ Created: dashboards/channel_performance.html")

    return fig


def create_monthly_trend_chart(df):
    """Line chart of monthly revenue and spend"""

    df['month'] = pd.to_datetime(df['date']).dt.to_period('M').astype(str)

    monthly = df.groupby('month').agg({
        'spend': 'sum',
        'revenue': 'sum',
        'conversions': 'sum'
    }).reset_index()

    fig = make_subplots(specs=[[{"secondary_y": True}]])

    fig.add_trace(
        go.Scatter(x=monthly['month'], y=monthly['revenue'],
                   name='Revenue', line=dict(color='green', width=3)),
        secondary_y=False
    )

    fig.add_trace(
        go.Scatter(x=monthly['month'], y=monthly['spend'],
                   name='Spend', line=dict(color='red', width=3)),
        secondary_y=False
    )

    fig.update_layout(
        title='Monthly Revenue vs Spend Trend',
        height=500
    )

    fig.update_xaxes(title_text='Month')
    fig.update_yaxes(title_text='Amount ($)', secondary_y=False)

    fig.write_html('dashboards/monthly_trends.html')
    print("✅ Created: dashboards/monthly_trends.html")

    return fig


def create_conversion_funnel(df):
    """Funnel chart showing conversion stages"""

    total_impressions = df['impressions'].sum()
    total_clicks = df['clicks'].sum()
    total_conversions = df['conversions'].sum()

    fig = go.Figure(go.Funnel(
        y=['Impressions', 'Clicks', 'Conversions'],
        x=[total_impressions, total_clicks, total_conversions],
        textposition='inside',
        textinfo='value+percent initial'
    ))

    fig.update_layout(
        title='Marketing Conversion Funnel',
        height=500
    )

    fig.write_html('dashboards/conversion_funnel.html')
    print("✅ Created: dashboards/conversion_funnel.html")

    return fig


def create_budget_allocation(df):
    """Treemap of budget allocation by channel"""

    channel_spend = df.groupby('channel').agg({
        'spend': 'sum',
        'revenue': 'sum'
    }).reset_index()

    channel_spend['roas'] = (channel_spend['revenue'] / channel_spend['spend']).round(2)

    fig = px.treemap(
        channel_spend,
        path=['channel'],
        values='spend',
        color='roas',
        color_continuous_scale='RdYlGn',
        title='Budget Allocation by Channel (Size=Spend, Color=ROAS)'
    )

    fig.write_html('dashboards/budget_allocation.html')
    print("✅ Created: dashboards/budget_allocation.html")

    return fig


def main():
    """Generate all dashboard visualizations"""

    print("📊 Loading data...")
    df = load_data()

    print("\n🎨 Creating visualizations...")
    create_channel_performance_chart(df)
    create_monthly_trend_chart(df)
    create_conversion_funnel(df)
    create_budget_allocation(df)

    print("\n" + "=" * 70)
    print("✅ ALL DASHBOARDS CREATED!")
    print("=" * 70)
    print("\n📂 Open the HTML files in dashboards/ folder to view")
    print("   - Right-click → Open With → Browser")


if __name__ == '__main__':
    main()
