import streamlit as st
import src

st.set_page_config(page_title="Форматирование скорпированного из книги текста", page_icon="📈")
st.markdown("# Форматирование текста")

if "text" not in st.session_state:
    st.session_state.text = ""

if st.button('Очистить'):
    st.session_state.text = ""
    st.rerun()

txt = st.text_area("", height="content", placeholder='Текст', key='text')
if txt:
    st.code(src.format_text.fix_text(txt), wrap_lines=True)
