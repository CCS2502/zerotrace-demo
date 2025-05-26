
import streamlit as st
import pandas as pd
import numpy as np
import datetime
import random
from web3 import Web3

# Multilingual Setup
language = st.selectbox("🌐 Select Language / Sélectionnez la langue", ["English", "Français"])

# Translations
translations = {
    "English": {
        "title": "ZerøTrace – Carbon Emissions Dashboard",
        "select_factory": "Select a facility",
        "emissions_chart": "Carbon Emissions Overview (Simulated)",
        "forecast_chart": "AI Forecast (Next 6 Months)",
        "log_blockchain": "Log ESG Report to Blockchain",
        "success": "Report successfully logged on blockchain!",
    },
    "Français": {
        "title": "ZerøTrace – Tableau de bord des émissions de carbone",
        "select_factory": "Sélectionnez une installation",
        "emissions_chart": "Aperçu des émissions de carbone (Simulé)",
        "forecast_chart": "Prévision IA (6 prochains mois)",
        "log_blockchain": "Enregistrer le rapport ESG sur la blockchain",
        "success": "Rapport enregistré avec succès sur la blockchain !",
    }
}
T = translations[language]

st.title(T["title"])

# Select facility
factory = st.selectbox(T["select_factory"], ["Solar Plant", "Thermal Station", "Phosphate Factory"])

# Simulate emissions data
dates = pd.date_range(end=datetime.date.today(), periods=6)
emissions = np.random.uniform(500, 900, size=6)

# Display emissions chart
st.subheader(T["emissions_chart"])
st.line_chart(pd.DataFrame({"CO₂ (tons)": emissions}, index=dates))

# AI Forecast
future_dates = pd.date_range(start=datetime.date.today(), periods=6)
forecast = emissions + np.random.uniform(-50, 50, size=6)

st.subheader(T["forecast_chart"])
st.line_chart(pd.DataFrame({"Forecast CO₂ (tons)": forecast}, index=future_dates))

# Simulate blockchain logging
if st.button(T["log_blockchain"]):
    # Simulated action: In real use, connect to Ethereum testnet
    st.success(T["success"])
