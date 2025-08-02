
import streamlit as st
import requests
import json
from PIL import Image

st.title("🩺 Doctor Prescription Analyzer")

st.write("Upload a doctor's prescription image or enter text to extract and analyze details.")

option = st.radio("Choose input type:", ("Upload Image", "Enter Text"))

if option == "Upload Image":
    uploaded_file = st.file_uploader("Upload Prescription Image", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Prescription', use_container_width=True)
        if st.button("Analyze Prescription"):
            files = {'file': uploaded_file.getvalue()}
            response = requests.post("http://localhost:8000/extract_text", files=files)
            if response.ok:
                text = response.json()["text"]
                st.text_area("Extracted Text", value=text, height=150)
                # Analyze the text
                analysis_response = requests.post("https://my-fastapi-backend.onrender.com/analyze_prescription", json={"text": user_input})
                if analysis_response.ok:
                    result = analysis_response.json()
elif option == "Enter Text":
    user_input = st.text_area("Enter Prescription Text")
    if st.button("Analyze Prescription"):
        analysis_response = requests.post("http://localhost:8000/analyze_prescription", json={"text": user_input})
        if analysis_response.ok:
            result = analysis_response.json()

# Display output if available
if 'result' in locals():
    st.subheader("🧾 Extracted Medicines")
    for med in result["medicines"]:
        st.write(f"- *{med['name']}*: {med['dosage']}, {med['frequency']}, {med.get('timing', 'No timing info')}")

    st.subheader("🔍 Age Limit Check")
    st.info(result["age_limit_check"])

    st.subheader("🦠 Predicted Disease")
    st.success(result["predicted_disease"])

    st.subheader("🍽 Nutrition Advice")
    st.write(result["diet"])

    st.subheader("🏃 Workout Suggestion")
    st.write(result["workout"])
