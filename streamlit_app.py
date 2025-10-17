import streamlit as st
import pandas as pd
from networksecurity.utils.main_utils.utils import load_object
from networksecurity.utils.ml_utils.model.estimator import NetworkModel
from networksecurity.exception.exception import NetworkSecurityException
import os 
import sys
import matplotlib.pyplot as plt

st.sidebar.title("About the Project")
st.sidebar.info("""
**Phishing Website Predictor**
- Built using a trained ML model
- Upload a CSV file to classify whether a website is malicious or not
- Interpretation of results:\n
 -1: Phishing website\n
  0: Suspicious website\n
  1: Legitimate website
                


👨‍💻 Developed by: Harsh Malik\n
📧 Contact: harshmalik0034@gmail.com""")
st.set_page_config(page_title="Phishing Website Predictor",layout="wide")
st.title("Phishing Website Predictor")
st.markdown("This app uses a trained ML model to detect or classify phishing websites. Upload your CSV file to get started.")
upload_file=st.file_uploader("Upload your csv file",type=["csv"])

if upload_file is not None:
    try:
        df=pd.read_csv(upload_file)
        st.write("Data Preview:")
        st.dataframe(df.head())

        preprocessor=load_object("final_model/preprocessor.pkl")
        model=load_object("final_model/model.pkl")
        network_model=NetworkModel(preprocessor=preprocessor,model=model)

        input_df=df.copy()
        if 'Predicted' in input_df.columns:
            input_df=input_df.drop(columns=['Predicted'])

        pred=network_model.predict(input_df)
        df1=df.copy()
        df1['Predicted']=pred

        st.success('Predictions Generated Successfully')
        st.write("Prediction Results:")
        tab1,tab2=st.tabs(["Uploaded Data","Predicted Data"])
        with tab1:
            st.write("Uploaded Data:")
            st.dataframe(input_df)

        with tab2:
            st.write("Predicted Data:")
            st.dataframe(df1)

        counts=df1['Predicted'].value_counts().sort_index()
        st.write("Prediction Distribution:")
        st.write(counts)

        fig,ax=plt.subplots(figsize=(4,3))
        ax.bar(counts.index.astype(str),counts.values,color=['red','orange','green'])
        ax.set_xlabel("Website Legitimacy")
        ax.set_ylabel("Count")
        ax.set_title("Prediction Distribution")
        st.pyplot(fig,use_container_width=False)

        csv=df1.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download Predictions as CSV",
            data=csv,
            file_name='Predictions.csv',
            mime='text/csv'
        )
    except Exception as e:
        raise NetworkSecurityException(e,sys)
else:
    st.info("Upload a csv file to begin")
