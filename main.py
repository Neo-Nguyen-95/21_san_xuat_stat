import streamlit as st
import pandas as pd
from utils import transform_excel_to_stat, check_file_format

st.title("THỐNG KÊ SỐ LƯỢNG CH TRONG NHCH")

# File uploader
uploaded_file = st.file_uploader("Upload file excel", type=["xlsx"])

if uploaded_file is not None:
    # Read the uploaded Excel file
    datapath = pd.ExcelFile(uploaded_file)
    status, message = check_file_format(datapath)
    if status:
        st.success(message)
        df = transform_excel_to_stat(datapath)
        # Show dataframe
        st.dataframe(df)
    else:
        st.error(message)
    
else:
    st.info("Kéo thả file excel để thống kê")

