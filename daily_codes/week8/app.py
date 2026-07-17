import streamlit as st
import pandas as pd
import numpy as np
import joblib

st.title("Grape Quality Prediction")
st.write("put the values and know the quality of ur grapes")

# COLOR_INTENSITY', 'FLAVANOIDS', 'PROLINE', 'TEMPERATURE', 'FER_P2O5_PER'

COLOR_INTENSITY = st.number_input("COLOR INTENSITY")
FLAVANOIDS = st.number_input("FLAVANOIDS")
PROLINE = st.number_input("PROLINE")
TEMPERATURE = st.number_input("TEMPERATURE")
FER_P2O5_PER = st.number_input("FER_P2O5_PER")
