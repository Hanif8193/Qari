import streamlit as st

# For Urdu font support
from PIL import ImageFont
from pytube import YouTube
# Load Jameel Noori Nastaliq font
font_path = "path/to/jameel_noori_nastaliq.ttf"  

# Configure font settings
font_settings = {
    "weight": 400,
    "subset": "latin"
}

st.title(" سنی جماعت القرآن پاکستان")
st.image("qari.png", caption="قاری عنایت اللہ سیالوی")

st.title("قاری عنایت اللہ سیالوی صاحب کے صاحبزادگان")



# Title


# Create columns for a flexible layout
col1, col2, col3, col4 = st.columns(4)

# Add images and captions in columns
with col1:
    st.image("pic1.png", caption="قاری بلال سیالوی")

with col2:
    st.image("Pic2.png", caption="قاری اویس سیالوی")

with col3:
    st.image("Pic3.png", caption="قاری حذیفہ سیالوی")

with col4:
    st.image("Pic4.png", caption="قاری حنظلہ سیالوی")
    # Add spacing
st.markdown("<br><br>", unsafe_allow_html=True)

st.title("انٹرنیشنل قراء")



x=open("Hamdi.mp4","rb")
vi=x.read()
st.video(vi)
