import streamlit as st
import src


st.set_page_config(page_title="Расчет среднегодового роста", page_icon="📈")
st.markdown("# Расчет среднегодового роста")

col1, col2 = st.columns(2)
a = col1.number_input("Первое значение", value=10.0)
b = col2.number_input("Второе значение", min_value=0.0)
count_years = st.number_input("Количетсво лет", min_value=2, step=1, value=7)

average_annual_growth = src.average_annual_growth.calculation_average_annual_growth(a, b, count_years)
st.success(f'{average_annual_growth}')
