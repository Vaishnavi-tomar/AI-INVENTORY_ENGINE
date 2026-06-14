AI Inventory Engine — Local Setup Guide (Windows)

This project is an AI-powered inventory forecasting engine built using:

Python
Amazon Chronos forecasting models
PyTorch
Gradio UI

It predicts future demand and helps identify potential stock shortages using historical retail sales data.

Features
AI demand forecasting
Reorder point prediction
Inventory risk visualization
Interactive Gradio dashboard
Walmart M5 dataset integration
Amazon Chronos Transformer forecasting
Tech Stack
Python
PyTorch
Chronos Forecasting
Gradio
Pandas
NumPy
Matplotlib
System Requirements

Recommended:

Windows 10/11
Python 3.10–3.12
8GB+ RAM
Stable internet connection
5GB+ free disk space

CPU mode works fine.

GPU is optional.

1. Install Python

Download Python:

Python Official Website

During installation:

✅ CHECK Add Python to PATH
✅ Select Install Now

Verify installation:

python --version
pip --version
2. Clone Repository

Install Git if needed:

Git for Windows

Clone repo:

git clone https://github.com/HimakshP/AI-INVENTORY_ENGINE.git
cd AI-INVENTORY_ENGINE
3. Create Virtual Environment
python -m venv venv

Activate it:

venv\Scripts\activate

You should now see:

(venv)
4. Install Dependencies

Upgrade pip first:

python -m pip install --upgrade pip

Install requirements:

pip install -r requirements.txt
5. Fix Chronos Installation

If you get errors related to ChronosPipeline, install the correct Chronos package:

pip uninstall chronos -y

Then:

pip install git+https://github.com/amazon-science/chronos-forecasting.git
6. Download Dataset

This project uses the Walmart M5 Forecasting dataset.

Download from Kaggle:

M5 Forecasting Dataset

Extract these files into the project root folder:

calendar.csv
sales_train_evaluation.csv
sell_prices.csv

Your project folder should look like:

AI-INVENTORY_ENGINE/
│
├── app.py
├── requirements.txt
├── calendar.csv
├── sales_train_evaluation.csv
├── sell_prices.csv
├── README.md
└── venv/
7. Run the Application

Start the app:

python app.py

First launch may take several minutes because:

Chronos model downloads
Torch initializes
Dataset preprocessing runs

Eventually you should see:

Running on local URL: http://127.0.0.1:7860

Open that URL in your browser.

8. Using the App
Select a product
Enter current inventory
View:
stock risk analysis
reorder recommendations
AI demand forecast graph
Common Errors & Fixes
Error: No module named chronos

Run:

pip install git+https://github.com/amazon-science/chronos-forecasting.git
Error: ChronosPipeline import failed

Wrong package installed.

Fix:

pip uninstall chronos -y
pip install git+https://github.com/amazon-science/chronos-forecasting.git
Error: No such file or directory

Make sure:

calendar.csv
sales_train_evaluation.csv
sell_prices.csv

are inside the project folder.

Error: torch cuda

This project runs on CPU by default.

No CUDA setup required.

Notes
Initial model download can exceed 1GB.
CPU inference may take 10–40 seconds per prediction.
Only the first 2000 dataset rows are loaded for local performance.
Dataset Attribution

Dataset:

Source:
Kaggle M5 Dataset