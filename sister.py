import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(page_title="Miss My Sister", page_icon="❤️")

# Big floating hearts + hug emojis
html("""
<style>
.heart {
  position: fixed;
  font-size: 40px;
  animation: float 7s linear infinite;
}

.hug {
  position: fixed;
  font-size: 50px;
  animation: hugfloat 6s linear infinite;
}

@keyframes float {
  0% {bottom:-10%; opacity:1;}
  100% {bottom:110%; opacity:0;}
}

@keyframes hugfloat {
  0% {top:-10%; opacity:1;}
  100% {top:110%; opacity:0;}
}
</style>

<script>
setInterval(() => {
  const heart = document.createElement("div");
  heart.className = "heart";
  heart.innerHTML = "❤️";
  heart.style.left = Math.random()*100 + "vw";
  document.body.appendChild(heart);
  setTimeout(()=>heart.remove(),7000);
}, 500);

setInterval(() => {
  const hug = document.createElement("div");
  hug.className = "hug";
  hug.innerHTML = "🫂";
  hug.style.left = Math.random()*100 + "vw";
  document.body.appendChild(hug);
  setTimeout(()=>hug.remove(),6000);
}, 900);
</script>
""")

# Center text
st.markdown("<h1 style='text-align:center;font-size:60px;'>❤️ Meenakshi Ka ❤️</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align:center;font-size:40px;'>🫂 I miss my sister so much 🥺</h2>", unsafe_allow_html=True)

st.markdown("<h3 style='text-align:center;'>❤️❤️❤️ Sending hugs ❤️❤️❤️</h3>", unsafe_allow_html=True)

st.caption("Made with ❤️ using Streamlit")
