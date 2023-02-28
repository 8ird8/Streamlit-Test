import streamlit as st 
from PIL import Image


st.set_page_config(
    page_title="Presentation",
    page_icon="💎",
    layout="centered",
)

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()),unsafe_allow_html=True)
col1,col2=st.columns(2)
with col1 :
    st.header('Image')
    image= Image.open('profile.png')
    st.image(image)
with col2:
    st.header('Video')
    video_file= open('video2.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)



st.sidebar.success('select page')





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

## sammary 
st.markdown( '## Summary')

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


e = RuntimeError('Error')
st.exception(e)
st.success('This is a success message!', icon="✅")
#############
#button
st.button('Click')
st.checkbox('I agree')
st.radio("Pick one" ,('cat','dog','horse'))

date= st.date_input(
    'your birthday' ,
)

st.write(st.experimental_user['email'])
email= 'achraf.bib@hotmail.com'

import time

with st.empty():
    for seconds in range(30):
        st.write(f"⏳ {seconds} seconds have passed")
        time.sleep(1)
    st.write("✔️ 30 seconds over!")


