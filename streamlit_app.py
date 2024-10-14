import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

# Define the images and their corresponding URLs
image_urls = [
    "https://lh4.googleusercontent.com/0syh03zKCeKxO_PcohEXJ-RH1bwlClwzKhRfhuW2Rj_iPiAcQ7DZGL-mKqpyYJ0bmsxvyuETOOfgvHaNls_3lU4tjhlQ0sdVFKA5MlTdYQ4qHVIiiw_DgoFkW1Rw87wt_A=w1280",
    "https://www.dropbox.com/scl/fi/0c0zv5hcbbyael21ykq6z/Caleb_Hoffman.png?rlkey=qe05olkypw0v8255u64jvh4b9&dl=0",
    "https://previews.dropbox.com/p/thumb/ACaWdjaga98QW7REbZfdnmCtwm-YtLmEX6Lx39wj8IYrTypKm1oQ5BIofRFM7dNOS4douVqmmsQpRqbuqAL42P9XTkuyoeSNodOpUcsEtqUR9B6Kamy_dohqwXtuuDpFi-sYH7QRYL8tfP2loPLcr8e_nkeTHEdhMsnVegAzS61CwCo9LTiMdqsUViZ89qt3cLWyi5KF4Jld-8ugWvKjioVbmBiGznHsaxzfr7SnVe14jrb6jiw6TC5-3TEK_UibHcN8qWZDQZ9Fow3tWcJASkDewQq5Wcx_sYXRwRO2PUbjMUSmu740rMVUuWs6JEB120q3ISq7lq0e0z35Hx1UDjwTgsOW8_4Rtx_NHOk-xOMGRwd9l8L4iPtzlyJrkurl-udqSa9PEiIgWQoSawwwoXC3xELJY9jDMenXCdsV1q55mP5XaFyMcXhfoRkZ39IlpF8lA4a6lhYbi0gUrS7WAdR-UaSi3qWAjgNV8eZddfaoHsMQ87O8VwiMssyK2x9at7ET3Yh-ZuXZjS7XnGg4-SHS/p.png?is_prewarmed=true",
    "https://via.placeholder.com/150/FFFF00/FFFFFF?text=Image+4"
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






