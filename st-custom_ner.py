import streamlit as st
import spacy
from spacy import displacy
import Dr_Appukuttan_ner
CNM = spacy.load("Dr_Appukuttan_ner")


st.title("Custom NER for Oral Medicine")
st.info("This is a demo NER using spacy to identify the entities in the electronic health records")

text = st.text_area("Enter a health record related to Oral medicine")

if (st.button("Submit")):
    document = CNM(text)
    enitity = displacy.render(document, style = "ent", jupyter= False)
    st.markdown(enitity, unsafe_allow_html=True)
