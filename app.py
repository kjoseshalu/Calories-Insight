import streamlit as st
import google.generativeai as genai
import os
# Load environment variables
from dotenv import load_dotenv
load_dotenv()
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input_prompt,image):
    model=genai.GenerativeModel("models/gemini-1.5-pro")
    response=model.generate_content([input_prompt,image[0]])
    return response.text

def input_image_setup(uploaded_data):
    if uploaded_data is not None:
        bytes_data = uploaded_data.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")
    

#initializing the app
st.set_page_config(page_title="Calories Insight", layout="wide")
st.header("Calories Insight")
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image,caption="Uploaded Image", use_container_width=True)
submit=st.button("Tell me about the Total Calories")

input_prompt = """
You are an expert in nutritionist where you need to see the foof items from the image
                and calculate the total calories,also provide the details of
                every food items with calories
                in below format
                1.Item 1 - no of calories
                2.Item 2 - no of calories
                -----
                ----
Finally you can also mention whether the food is healthy or not and also
mention the 
percentage split of the ration of carbohydrates,fats,sugars,proteins,fibers and other important
things required in our diet
"""

if submit:
    image_data=input_image_setup(uploaded_file)
    try:
        response = get_gemini_response(input_prompt,image_data)
        st.write(response)
    except Exception as e:
        st.error(f"Error: {e}")