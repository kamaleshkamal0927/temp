import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(page_title="Miss My Sister", page_icon="❤️")

# Floating hearts
html("""
<style>
.heart {
  position: fixed;
  font-size: 28px;
  animation: float 6s linear infinite;
}
@keyframes float {
  0% {bottom:0; opacity:1;}
  100% {bottom:100%; opacity:0;}
}
</style>

<script>
setInterval(() => {
  const heart = document.createElement("div");
  heart.className = "heart";
  heart.innerHTML = "❤️";
  heart.style.left = Math.random()*100 + "vw";
  document.body.appendChild(heart);
  setTimeout(()=>heart.remove(),6000);
}, 400);
</script>
""")

# Text
st.markdown("<h1 style='text-align:center;'>❤️ Meenakshi Ka ❤️</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align:center;'>🥺 I miss my sister so much 💖</h2>", unsafe_allow_html=True)

# GIFs (fixed)
st.image("https://media.giphy.com/media/l0HlBO7eyXzSZkJri/giphy.gif", width=250)
st.image("https://media.giphy.com/media/3oriO0OEd9QIDdllqo/giphy.gif", width=250)

st.caption("Made with ❤️ using Streamlit")

