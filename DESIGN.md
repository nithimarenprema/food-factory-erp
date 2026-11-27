# Food Factory ERP – Design Document

## 1. System Architecture

The system connects five business activities:

1. Sales order management
2. GST invoicing
3. Production management
4. Inventory management
5. Monthly audit reporting

## 2. Technology Stack

- Python
- Streamlit
- Pandas
- PostgreSQL (planned)

## 3. Database Design

Proposed database tables:

| Table | Purpose |
|---|---|
| Users | User login and roles |
| Products | Finished products |
| Customers | Retailers and distributors |
| Materials | Raw materials |
| BOM | Bill of Materials |
| Purchases | Material purchases |
| Orders | Customer orders |
| Production | Production runs |
| Stock Movements | Inventory transactions |
| Invoices | GST invoices |
| Payments | Customer collections |

## 4. BOM Calculation

Murukku 200g standard batch:

- Flour: 40 kg
- Oil: 10 litres
- Spice: 1.2 kg
- Pouches: 200 pieces
- Cartons: 10 pieces

Expected output: 200 packets.

Actual output: 188 packets.

Yield variance: -6%.

Oil consumption variance: +5%.

Both exceed the 3% tolerance.

## 5. Inventory Calculation

Flour:
100 + 60 - 40 = 120 kg

Oil:
30 - 10.5 = 19.5 litres

Pouches:
500 - 188 - 6 = 306 pieces

Finished goods:
50 + 188 = 238 packets

After dispatch:
238 - 150 = 88 packets

## 6. Costing Method

Weighted average valuation is used for flour.

Flour weighted average rate:

₹43.125 per kg.

Material cost: ₹4,055.

Labour: ₹1,200.

Gas and power: ₹600.

Total production cost: ₹5,855.

Cost per good packet:

₹5,855 / 188 = ₹31.14.

## 7. GST Calculation

Taxable value: ₹7,500.

CGST: ₹187.50.

SGST: ₹187.50.

Invoice total: ₹7,875.

## 8. Limitations

This version is an MVP demonstration.

Persistent database, authentication, complete stock ledger,
invoice PDF generation and production-grade audit controls
require further implementation.

## 9. Future Enhancements

- Role-based authentication
- PostgreSQL integration
- Offline order synchronization
- Batch and expiry tracking
- Tally integration
- Automated audit exports
