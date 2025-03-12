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



# List of video file names
video_files = ["Hamdi.mp4", "Abdullah.mp4", "Reja.mp4", "Wajee.mp4"]

# Create columns for videos (adjust number of columns as needed)
cols = st.columns(len(video_files))

# Display videos in separate columns
for idx, video_file in enumerate(video_files):
    with open(video_file, "rb") as file:
        video_bytes = file.read()
        cols[idx].video(video_bytes)



