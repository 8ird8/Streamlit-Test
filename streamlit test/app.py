import streamlit as st 
from PIL import Image


st.set_page_config(
    page_title="Presentation",
    page_icon="💎",
    layout="centered",
)

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()),unsafe_allow_html=True)

image= Image.open('profile.png')
st.image(image)

video_file= open('video2.mp4', 'rb')
video_bytes = video_file.read()

st.video(video_bytes)


st.write('# `Presetation`')
st.markdown(''' 
## Achraf  `Belahbib` 
icons  https://emojikeyboard.top/

Yooooo
''' ,unsafe_allow_html=True)
st.text( '''
**Achraf   is    `mad`  but    news of the day                   2022 
there is always  hope                                            2021
''')
st.markdown( '## Summary', unsafe_allow_html=True)
## sammary 
st.info(''' 
- hello hello. 
- heloo 
- hello
- hrllo. 
- num
-dad
'''
 )

st.warning(''' 
- Attention 
- Dear you are !
- I got you 
''', icon="⚠️")


e = RuntimeError('This is an exception of type RuntimeError')
st.exception(e)
st.success('This is a success message!', icon="✅")
#############
#button
st.button('Click')


st.write(st.experimental_user['email'])
email= 'achraf.bib@hotmail.com'


