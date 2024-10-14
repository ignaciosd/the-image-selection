import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

# Define the images and their corresponding URLs
image_urls = [
    "https://lh4.googleusercontent.com/0syh03zKCeKxO_PcohEXJ-RH1bwlClwzKhRfhuW2Rj_iPiAcQ7DZGL-mKqpyYJ0bmsxvyuETOOfgvHaNls_3lU4tjhlQ0sdVFKA5MlTdYQ4qHVIiiw_DgoFkW1Rw87wt_A=w1280",
    "https://via.placeholder.com/150/FF0000/FFFFFF?text=Image+2",
    "https://via.placeholder.com/150/00FF00/FFFFFF?text=Image+3",
    "https://via.placeholder.com/150/FFFF00/FFFFFF?text=Image+4"
]

websites = [
    "https://www.google.com",
    "https://www.bing.com",
    "https://www.yahoo.com",
    "https://www.duckduckgo.com"
]

st.title("Click an Image to Open a Website")

# Layout the images in two rows
col1, col2 = st.columns(2)

# Function to display clickable images
def clickable_image(image_url, link):
    st.markdown(f'<a href="{link}" target="_blank"><img src="{image_url}" style="width: 100%; height: auto;"></a>', unsafe_allow_html=True)

# Display images with clickable links
with col1:
    clickable_image(image_urls[0], websites[0])
    clickable_image(image_urls[1], websites[1])

with col2:
    clickable_image(image_urls[2], websites[2])
    clickable_image(image_urls[3], websites[3])






