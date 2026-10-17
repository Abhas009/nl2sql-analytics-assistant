import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="NL2SQL Analytics", page_icon="📊", layout="wide")
st.title("📊 NL2SQL Analytics Assistant")
st.markdown("Ask a question about the GitHub events data in plain English.")

question = st.text_input("Your question:", placeholder="e.g., Which repo had the most total events?")

if st.button("Ask AI"):
    if question:
        with st.spinner("Thinking..."):
            try:
                # Send request to your FastAPI backend
                res = requests.post("http://127.0.0.1:8000/query", json={"question": question})
                res.raise_for_status()
                data = res.json()

                st.success("Query executed successfully!")
                
                st.subheader("Generated SQL")
                st.code(data["sql"], language="sql")
                
                st.subheader("AI Summary")
                st.info(data["summary"])
                
                st.subheader("Data")
                df = pd.DataFrame(data["rows"])
                st.dataframe(df, use_container_width=True)
                
            except Exception as e:
                st.error(f"Error: {e}")
