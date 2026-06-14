# -*- coding: utf-8 -*-
"""M5_projects_local.py"""

import pandas as pd
import zipfile
import numpy as np
import torch
import gradio as gr
import matplotlib.pyplot as plt

from chronos import ChronosPipeline


sales = pd.read_csv('sales_train_evaluation.csv', nrows=2000)
calendar = pd.read_csv('calendar.csv')
prices = pd.read_csv('sell_prices.csv', nrows=5000)

print("✅ Data is back and unzipped!")


df = pd.melt(
    sales,
    id_vars=[
        'id',
        'item_id',
        'dept_id',
        'cat_id',
        'store_id',
        'state_id'
    ],
    var_name='d',
    value_name='sales'
)


df = df.merge(
    calendar[['d', 'event_name_1', 'wm_yr_wk']],
    on='d',
    how='left'
)

df = df.merge(
    prices,
    on=['store_id', 'item_id', 'wm_yr_wk'],
    how='left'
)


df['sell_price'] = df['sell_price'].fillna(
    df.groupby('id')['sell_price'].transform('mean')
)

df['is_event'] = df['event_name_1'].notnull().astype(int)

print("✅ Master Table is Re-created and ready for the AI!")


pipeline = ChronosPipeline.from_pretrained(
    "amazon/chronos-t5-base",
    device_map="cpu"
)

print("✅ AI Brain Loaded Successfully!")


context = torch.tensor(
    df[df['id'] == df['id'].unique()[0]]['sales'].values[-100:]
)


forecast = pipeline.predict(
    context,
    prediction_length=28
)

print("Forecast Complete! The 'Brain' has spoken.")

def inventory_engine(product_id, current_stock):

    
    context_data = df[df['id'] == product_id]['sales'].values[-100:]

    context_tensor = torch.tensor(context_data)

    
    forecast = pipeline.predict(
        context_tensor,
        prediction_length=21
    )

    
    low, median, high = np.quantile(
        forecast[0].numpy(),
        [0.1, 0.5, 0.9],
        axis=0
    )

    
    rop = np.sum(high[:7])

    if current_stock <= 0:
        status = "🔴 OUT OF STOCK"

    elif current_stock <= rop:
        status = f"⚠️ REORDER IMMEDIATELY (Threshold: {int(rop)})"

    else:
        status = "🟢 STOCK HEALTHY"

    
    plt.figure(figsize=(10, 4))

    plt.plot(
        context_data[-30:],
        label="Past 30 Days Sales",
        color="black"
    )

    plt.plot(
        np.arange(30, 51),
        median,
        label="Predicted Sales",
        color="blue"
    )

    plt.fill_between(
        np.arange(30, 51),
        low,
        high,
        color="blue",
        alpha=0.2,
        label="Risk Zone"
    )

    plt.axhline(
        y=current_stock,
        color='red',
        linestyle='--',
        label="Current Stock Level"
    )

    plt.legend()

    plt.title(f"Inventory Forecast: {product_id}")

    return status, plt.gcf()


demo = gr.Interface(
    fn=inventory_engine,

    
    inputs=[
        gr.Dropdown(
            choices=list(df['id'].unique()[:50]),
            label="Select Product"
        ),

        gr.Number(
            label="Enter Current Warehouse Stock",
            value=50
        )
    ],

    outputs=[
        gr.Textbox(label="Action Plan"),
        gr.Plot(label="Demand Visualizer")
    ],

    title="📦 Amazon-Style Stock-Run Engine",

    description="Using Transformer-based AI to prevent out-of-stock events."
)


lead_time = 7

def calculate_rop(median_forecast, high_forecast):

    
    demand_during_lead_time = np.sum(
        median_forecast[:lead_time]
    )

    
    safety_stock = (
        np.sum(high_forecast[:lead_time]) -
        demand_during_lead_time
    )

    return demand_during_lead_time + safety_stock

print("✅ Day 12 Logic Updated: Lead-Time Demand + Safety Stock.")


def get_prediction(product_id):

    data = df[df['id'] == product_id]['sales'].values[-100:]

    context = torch.tensor(data)

    forecast = pipeline.predict(
        context,
        prediction_length=21
    )

    low, median, high = np.quantile(
        forecast[0].numpy(),
        [0.1, 0.5, 0.9],
        axis=0
    )

    return data, low, median, high

def calculate_rop(median_f, high_f):

    lead_time = 7

    demand_during_lt = np.sum(
        median_f[:lead_time]
    )

    safety_stock = (
        np.sum(high_f[:lead_time]) -
        demand_during_lt
    )

    return demand_during_lt + safety_stock

print("🚀 Starting Batch Process for 50 items... please wait.")

results = []

top_items = df['id'].unique()[:50]

for item in top_items:

    try:
        history, low, median, high = get_prediction(item)

        rop = calculate_rop(median, high)

        current_inv = np.random.randint(10, 100)

        results.append({
            "Product_ID": item,
            "Current_Stock": current_inv,
            "Reorder_Point": int(rop),
            "Status": "🚨 REORDER" if current_inv <= rop else "✅ HEALTHY"
        })

    except Exception as e:
        print(f"Error processing {item}: {e}")

report_df = pd.DataFrame(results)

report_df.to_csv(
    "Amazon_Inventory_Report_2026.csv",
    index=False
)

print("✅ Day 13 Success! Download 'Amazon_Inventory_Report_2026.csv' from your sidebar.")

print(report_df.head())

with open('requirements.txt', 'w') as f:
    f.write(
        'pandas\nnumpy\ntorch\nchronos-forecasting\ngradio\nfastapi\nmatplotlib'
    )

print("✅ requirements.txt generated!")

sample_id = df['id'].unique()[0]

status, fig = inventory_engine(
    sample_id,
    current_stock=20
)

fig.savefig("ai_forecast_proof.png")

print("✅ Graph saved! Now download it from the folder icon on the left.")

demo.launch()