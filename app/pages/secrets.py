import streamlit as st
import requests
from random import randint

st.title('Welcome to my page of secrets!')

###

st.markdown('Here I will show how to use secrets in Streamlit')

###


if st.button('Click me'):
    img = st.secrets.secret_images.image
    st.image(img)


###

query = st.text_input('Search a GIF')
url = 'https://api.giphy.com/v1/gifs/search'
params = {'api_key': st.secrets.api_keys.key, 'q': query}
res = requests.get(url, params).json()


while not query:
    st.stop()


gif = res['data'][randint(0, 10)]['embed_url']


st.write(
    f'<iframe src="{gif}" width="480" height="240">',
    unsafe_allow_html=True
)
