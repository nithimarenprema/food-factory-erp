import streamlit as st
import pandas as pd

st.set_page_config(page_title="Food Factory ERP", layout="wide")

st.title("🏭 Food Factory ERP System")
st.caption("Order-to-Audit Management System")

if "production" not in st.session_state:
    st.session_state.production = False

if "dispatched" not in st.session_state:
    st.session_state.dispatched = False

menu = st.sidebar.selectbox(
    "Select Module",
    ["Dashboard", "Production", "Inventory",
     "Sales Orders", "GST Invoice", "Reports"]
)

if menu == "Dashboard":
    st.header("Owner Dashboard")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Finished Stock", "238 packets" if not st.session_state.dispatched else "88 packets")
    c2.metric("Yield Variance", "-6%", "-6%")
    c3.metric("Oil Variance", "+5%", "+5%")
    c4.metric("Outstanding", "₹3,875")

    st.success("Food Factory ERP is running")

elif menu == "Production":
    st.header("Production Management")

    st.write("Product: Murukku 200g")
    st.write("Expected output: 200 packets")

    flour = st.number_input("Flour issued (kg)", value=40.0)
    oil = st.number_input("Oil issued (L)", value=10.5)
    spice = st.number_input("Spice issued (kg)", value=1.2)
    output = st.number_input("Actual good packets", value=188)
    damaged = st.number_input("Damaged pouches", value=6)
    cartons = st.number_input("Cartons used", value=9)

    if st.button("Save Production"):
        st.session_state.production = True
        st.success("Production recorded!")

    st.metric("Yield Variance", f"{(output-200)/200*100:.2f}%")
    st.metric("Oil Variance", f"{(oil-10)/10*100:.2f}%")

    if st.session_state.production:
        st.warning("Production variance exceeds 3% tolerance")

elif menu == "Inventory":
    st.header("Stock Management")

    produced = st.session_state.production

    data = {
        "Material": ["Flour", "Oil", "Spice", "Pouches", "Cartons", "Murukku"],
        "Closing Stock": [
            "120 kg" if produced else "160 kg",
            "19.5 L" if produced else "30 L",
            "3.8 kg" if produced else "5 kg",
            "306" if produced else "500",
            "21" if produced else "30",
            "238 packets" if produced else "50 packets"
        ]
    }

    st.dataframe(pd.DataFrame(data), use_container_width=True)

elif menu == "Sales Orders":
    st.header("Salesman Order Entry")

    customer = st.selectbox(
        "Customer",
        ["Retailer A - Tamil Nadu", "Distributor B - Karnataka"]
    )

    quantity = st.number_input("Quantity", min_value=1, value=150)

    if st.button("Submit Order"):
        if customer.startswith("Retailer"):
            st.success("Order submitted successfully")
        else:
            st.error("Insufficient stock: 32 packets")

    st.info("Admin must approve orders before invoicing.")

    if st.button("Admin Approve Retailer A"):
        st.session_state.dispatched = True
        st.success("Order approved and 150 packets dispatched")

elif menu == "GST Invoice":
    st.header("GST Tax Invoice")

    st.write("Customer: Retailer A")
    st.write("GSTIN: Dummy GSTIN for demonstration")
    st.write("HSN: Assumed illustrative HSN")
    st.write("Taxable Value: ₹7,500")
    st.write("CGST (2.5%): ₹187.50")
    st.write("SGST (2.5%): ₹187.50")
    st.subheader("Invoice Total: ₹7,875")

    payment = st.number_input("Payment received", value=4000)

    st.metric("Outstanding", f"₹{7875-payment:,.2f}")

elif menu == "Reports":
    st.header("Monthly Audit Reports")

    reports = {
        "Report": [
            "Sales Register",
            "GST Summary",
            "Purchase Register",
            "Stock Ledger",
            "Production Variance",
            "Outstanding"
        ],
        "Status": ["Available"] * 6
    }

    df = pd.DataFrame(reports)
    st.dataframe(df, use_container_width=True)

    st.download_button(
        "Download CSV Report",
        df.to_csv(index=False),
        "audit_report.csv",
        "text/csv"
    )

st.divider()
st.caption("Food Factory ERP | NIT Trichy Internship Prototype")
