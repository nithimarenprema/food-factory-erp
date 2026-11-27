# food-factory-erp
# Food Factory ERP

Order-to-Audit Management System.

## Problem
Small food manufacturers manage orders, production,
inventory and accounting separately.

## Solution
A unified ERP prototype connecting sales, production,
inventory, GST and audit reports.

## Technology
- Python
- Streamlit
- Pandas

## Modules
1. Owner Dashboard
2. Production Management
3. Inventory Management
4. Sales Order Management
5. GST Invoice
6. Audit Reports

## Benchmark Results

- Flour closing: 120 kg
- Oil closing: 19.5 L
- Spice closing: 3.8 kg
- Pouches closing: 306
- Cartons closing: 21
- Finished goods: 238 packets
- Yield variance: -6%
- Oil variance: +5%
- Invoice: ₹7,875
- Outstanding: ₹3,875
- Production cost: ₹5,855
- Cost per packet: ₹31.14

## Costing
Weighted average material valuation.
Labour and power allocated to the production run.

## Limitations
This is an MVP demonstration.
Persistent database, authentication, complete audit
trail and production-grade GST compliance are future work.

## Run locally

pip install -r requirements.txt
streamlit run app.py
