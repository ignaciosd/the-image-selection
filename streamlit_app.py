import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

# Define the images and their corresponding URLs
image_urls = [
    "https://lh4.googleusercontent.com/0syh03zKCeKxO_PcohEXJ-RH1bwlClwzKhRfhuW2Rj_iPiAcQ7DZGL-mKqpyYJ0bmsxvyuETOOfgvHaNls_3lU4tjhlQ0sdVFKA5MlTdYQ4qHVIiiw_DgoFkW1Rw87wt_A=w1280",
    "https://lh5.googleusercontent.com/nZV6N0jIX-OVoJl1ozXzBn974LBcMzL0_PZ2_gy-cCy9zO2bbH2Jj9SkTfUIQnbPDg9b-k-d9mfj72h198TwTH8D-NywLLt3TNqIBhNrpRmYexARG9mVqZSLU2GP1-r8tw=w1280",
    "https://lh6.googleusercontent.com/W5z6V2i79dQZRC5S2PT6Z97g8cRvcEY7X_asIhGi_yZhQBWvw37N_XsSYZ65H-2JIIoMqsa0d_bgfUZPBcczd4jwDq2gZue50xpOYihpFInwGt3yfI2KVX8nxmbwb4seXg=w1280",
    "https://lh5.googleusercontent.com/psOEqfIuXS3flne5DwbRlohnvrTp-NNtoP6B3gHbhBOBTmPJSlG4h-erF7cJ7hnPlt_zBGjCgG0J5GXJ0UPjZMAZ0LN2urMTBupqZQqJHBN7NERRd36ePpV1yWolB8FTBw=w1280"
]

websites = [
    "https://www.ignaciosd.com",
    "https://mlbvisuals-caleb.streamlit.app/",
    "https://blank-app-e1rq5dmukpj.streamlit.app/",
    "https://blank-app-t0fggotm63q.streamlit.app/"
]

st.title("Click an Image to Open a Website")

# Layout the images in two rows
col1, col2 = st.columns(2)

# Function to display clickable images
def clickable_image(image_url, link):
    st.markdown(f'<a href="{link}" target="_blank"><img src="{image_url}" style="width: 100%; height: auto;"></a>', unsafe_allow_html=True)
    st.markdown(f'<p>This is a <strong>bold</strong> text.</p>')

# Display images with clickable links
with col1:
    clickable_image(image_urls[0], websites[0])
    clickable_image(image_urls[1], websites[1])

with col2:
    clickable_image(image_urls[2], websites[2])
    clickable_image(image_urls[3], websites[3])






