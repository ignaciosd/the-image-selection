import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

# Define the images and their corresponding URLs
image_urls = [
    "https://lh4.googleusercontent.com/0syh03zKCeKxO_PcohEXJ-RH1bwlClwzKhRfhuW2Rj_iPiAcQ7DZGL-mKqpyYJ0bmsxvyuETOOfgvHaNls_3lU4tjhlQ0sdVFKA5MlTdYQ4qHVIiiw_DgoFkW1Rw87wt_A=w1280",
    "https://www.dropbox.com/scl/fi/0c0zv5hcbbyael21ykq6z/Caleb_Hoffman.png?rlkey=qe05olkypw0v8255u64jvh4b9&dl=0",
    "https://lh3.googleusercontent.com/Fw7g5P_uTeqJ3XS8xp0TMLjCDzY2n3Y31mbxZGKKzycC_pVreaOs6PArTEpBe-uO29P7jK43tXPz0771SogIr84=w1280",
    "https://drive.google.com/file/d/1MBk_bXXK1V6GL0shUIs18QT3YhmCRkB1/view?usp=sharing"
]

websites = [
    "https://mlbvisuals-caleb.streamlit.app/",
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






