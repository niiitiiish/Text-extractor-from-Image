import easyocr 
import torch
import streamlit as st
import numpy as np
from PIL import Image


reader=easyocr.Reader(['en' ,'hi'])
st.title("Image Text extractor")
st.write("upload an image:")



uploaded_file=st.file_uploader("select an image file", type=['jpeg','png','jpg'])
if st.button("EXTRACT"):
    if uploaded_file:
        image=Image.open(uploaded_file)
        st.image(image,caption="uploaded image",use_column_width=True)
        image_np=np.array(image)
        result=reader.readtext(image_np)
        st.write("Extracted text: ")
        for(_,text,_)in result:
            st.write(f"{text}")
    else:
        st.error("please upload the corrrect image file")
else:
    st.write("")