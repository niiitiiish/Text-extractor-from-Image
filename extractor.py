import easyocr 
import streamlit as st

import numpy as np
from PIL import Image


reader=easyocr.Reader(['en'],model_storage_directory='.')
st.title("Image Text extractor")
st.write("upload an image:")



uploaded_file=st.file_uploader("select an image file", type=['jpeg','png','jpg'])
if st.button("EXTRACT"):
    if uploaded_file:
        image=Image.open(uploaded_file)
        st.image(image,caption="uploaded image",use_container_width =True)
        with  st.spinner("in Progress"):
       
            image_np=np.array(image)
            result=reader.readtext(image_np)
            extracted_text=[]
            st.write("Extracted text: ")
            for(_,text,_)in result:
                extracted_text.append(text)

            textract= " ".join(extracted_text)
            st.text_area("Extracted Text:", textract, height=300)
      
    else:
        st.error("please upload the corrrect image file")
else:
    st.write("")
