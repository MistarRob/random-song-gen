import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

if "suggest" not in st.session_state:
    st.session_state["suggest"] = False

def local_css(file_name):
    st.markdown(f"<!-- {file_name} -->", unsafe_allow_html=True)
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("C:/Users/Rob\Documents/randomsongen/random-song-gen/random-song-suggester/styles.css")

st.markdown (
            """
              <div class="center-txt"> 
              <h1 class="gradient-text"> Tired of TikTok Music Taste? </h1>
              </div>
              
              """,
              unsafe_allow_html=True
              
              )
st.markdown (
         """
                <div class="center-txt">
                <h3> Well then just click this button and choose your genre to get random song suggestions. Just for you! </h3>
                </div>
          """,
            unsafe_allow_html=True
            
)

st.markdown(
    """
    <div class="center-txt">
        <h3 class="subtext"> Choose your genre: </h3>
    </div>
    """,
    unsafe_allow_html=True 
) 

options = ["Pop", "Rock", "Hip-Hop", "Jazz", "Classical", "Country", "Discover a Genre!"]
selected_option = st.selectbox("", options)

st.markdown (
    f"""
    <div class = "center-txt">
      <h3 class="subtext"> You Selected: {selected_option} </h3>
    </div>
    """, unsafe_allow_html = True
)

st.markdown (
    """
        <div class="button-container">
            <a href="/?play=1" target="_self">
                <button class="pretty-gradient-button">Suggest me a song!</button>
            </a>
        </div>
""",
unsafe_allow_html=True
)

if st.query_params.get("play") == "1":
    genre_map = {
        "Pop": "pop",
        "Rock": "rock",
        "Hip-Hop": "hip-hop",
        "Jazz": "jazz",
        "Classical": "classical",
        "Country": "country",
        "Discover a Genre!": "indie-pop"
    }

    selected_genre = genre_map[selected_option].strip().lower()
    
...
   