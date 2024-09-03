from pygwalker.api.streamlit import StreamlitRenderer
import pandas as pd
import streamlit as st
 
# Adjust the width of the Streamlit page
st.set_page_config(
    page_title="Use Pygwalker In Streamlit",
    layout="wide"
)
# Import your data
df = pd.read_csv("https://kanaries-app.s3.ap-northeast-1.amazonaws.com/public-datasets/bike_sharing_dc.csv")

# Streamlit file uploader for users to upload CSV files
# uploaded_file = st.file_uploader("Upload your dataset (CSV)", type=["csv"])

# if uploaded_file is not None:
#     # Read the uploaded file into a pandas DataFrame
#     df = pd.read_csv(uploaded_file)
 
pyg_app = StreamlitRenderer(df)
 
pyg_app.explorer()