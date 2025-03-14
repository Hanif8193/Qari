import streamlit as st
from pytube import YouTube
from PIL import ImageFont
import os
st.write(os.listdir())

# Load Jameel Noori Nastaliq font
font_path = "path/to/jameel_noori_nastaliq.ttf"

# Configure font settings (optional, as Streamlit doesn’t natively support custom fonts)
# font_settings = {
#     "weight": 400,
#     "subset": "latin"
# }

st.title("سنی جماعت القرآن پاکستان")
st.image("qari.png", caption="قاری عنایت اللہ سیالوی")

st.title("قاری عنایت اللہ سیالوی صاحب کے صاحبزادگان")

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

# Display videos
st.header("حمدی کنجو")
with open("Hamdi.mp4", "rb") as x:
    vi = x.read()
    st.video(vi)

st.header("قاری رجا ایوب")
with open("Reja.mp4", "rb") as x1:
    vi = x1.read()
    st.video(vi)

st.header("وجی دیوان")
with open("Wajee.mp4", "rb") as x2:
    vi = x2.read()
    st.video(vi)

st.header("شیخ عبداللہ")
with open("Abdullah.mp4", "rb") as x3:
    vi = x3.read()
    st.video(vi)

