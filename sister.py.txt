import streamlit as st

st.set_page_config(page_title="Miss My Sister", page_icon="💖")

st.title("💖 I Miss My Sister")

# Upload image
image = st.file_uploader("Upload your sister's photo", type=["jpg", "png", "jpeg"])

if image:
    st.image(image, caption="My Lovely Sister ❤️", width=300)

if st.button("Show My Message"):
    st.success("🥺 I MISS MY SISTER SO MUCH ❤️")

st.markdown("---")
st.caption("Made with ❤️ using Streamlit")
