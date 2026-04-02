# AI-INVENTORY_ENGINE
"Initial commit of AI Inventory Engine Code"

# 📦 AI-Powered Inventory Engine for Stock-Run Prediction

### 🚀 Strategic Overview
In retail supply chains, "Stock-Outs" (out-of-stock events) lead to millions in lost revenue. This project implements a **Transformer-based Forecasting Engine** using the **Amazon Chronos-2 Foundation Model** to predict future demand and automate reorder alerts for warehouse managers.

---

### 📊 Key Technical Features
* **Zero-Shot Forecasting:** Leveraged the **Chronos-T5-Base** model to perform probabilistic forecasting on the M5 Walmart dataset without the need for extensive local training.
* **Safety Stock Optimization:** Implemented **P90 Quantile regression** logic to ensure 90% service level reliability during lead-time demand.
* **Automated Decision Logic:** Created a "Reorder Point" (ROP) engine that calculates the intersection of current inventory and AI-predicted risk.
* **Interactive Dashboard:** Built a **Gradio-powered UI** for real-time human-in-the-loop inventory management.

---

### 🖼️ System Demo & Proof of Life
Below is a static snapshot of the AI engine's predictive capability and risk-zone calculation:

![AI Forecast Proof](ai_forecast_proof.png)

---

### 🛠️ Technical Stack
| Category | Tools |
| :--- | :--- |
| **Model** | Amazon Chronos-2 (Transformer-based) |
| **Language** | Python 3.x |
| **Libraries** | PyTorch, Pandas, NumPy, Matplotlib |
| **Deployment** | FastAPI, Gradio, Google Colab (T4 GPU) |

---

### 📈 Business Impact
By shifting from traditional "Moving Average" methods to **Probabilistic AI Forecasting**, this engine:
1. Reduces manual inventory checks through **automated status alerts**.
2. Minimizes "Holding Costs" by optimizing reorder quantities.
3. Prevents lost sales by identifying **Demand Spikes** (Holidays/Events) that simple statistics often miss.

---

### 📂 Repository Structure
* `Inventory_Engine.ipynb`: Full source code with data pipeline and model inference.
* `Amazon_Inventory_Report_2026.csv`: Sample batch report generated for 50+ products.
* `requirements.txt`: Environment configuration for reproducibility.
