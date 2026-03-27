import streamlit as st
import src

st.set_page_config(page_title="Расчет среднего значения в наборе", page_icon="📈")
st.markdown("# Расчет среднего значения в наборе")

txt = st.text_area(
    "Набор значений", height="content"
)

st.success(f'{src.average_value_set.calcultion_average_value_set(txt)}')
