<!-- Badges -->
<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/pandas-%20-black?logo=pandas&labelColor=white" alt="pandas">
  <img src="https://img.shields.io/badge/NumPy-%20-black?logo=numpy&labelColor=white" alt="NumPy">
  <img src="https://img.shields.io/badge/Matplotlib-%20-black?logo=matplotlib&labelColor=white" alt="Matplotlib">
  <img src="https://img.shields.io/badge/Seaborn-%20-black" alt="Seaborn">
  <img src="https://img.shields.io/badge/SQLite-%20-black?logo=sqlite&labelColor=white" alt="SQLite">
  <img src="https://img.shields.io/badge/Jupyter-Notebook-orange?logo=jupyter&logoColor=white" alt="Jupyter">
</p>

# Retail Sales Analytics

**About:** End-to-end workflow to **generate realistic sales data → clean & explore (EDA) → load to SQL → answer business questions → visualize KPIs**.  
Built to mimic a real analytics pipeline that recruiters can evaluate quickly.

## Why this project? (and how it’s helpful)
- **Real-world pipeline:** Separates concerns—Python for data prep, **SQL** for business questions, notebooks for fast visuals—just like an entry-level analyst role.
- **Portfolio signal:** ~**100k rows** of synthetic data shows performance and scale; clean repo structure proves you can organize projects.
- **Decision-focused:** Charts/KPIs for **monthly revenue**, **category mix**, **city/channel performance**, **returns**, **AOV** → the metrics teams actually use.
- **Practice-ready:** Gives you hands-on exercises in **EDA, joins/aggregations/window logic, plotting**, and storytelling with data.

## What’s inside
- **Python:** data generation, cleaning, EDA, and plots (Matplotlib/Seaborn)
- **SQL (SQLite):** schema + business queries (monthly revenue, top products, category share, AOV, margin, returns)
- **Visuals:** revenue trend, category mix, city/channel performance, margin distribution
- **Structure:** `data/`, `sql/`, `src/`, `notebooks/`, `reports/figures/` for easy navigation

## Quickstart
```bash
pip install -r requirements.txt
python src/generate_data.py           # creates data/raw/transactions.csv (~100k rows)
python src/load_to_sql.py             # builds database/sales.db and loads table
python src/visualize.py               # saves charts into reports/figures/
