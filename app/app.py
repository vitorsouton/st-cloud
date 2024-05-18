import streamlit as st

import pandas as pd
import matplotlib.pyplot as plt
from utils import get_spect

#########################

st.title('Hello world!')


########################

st.markdown(
    '''
    # Just like a notebook, this is a header
    ## This is a sub-header
    ### This is a sub-sub-header

    ----

    - This
    - Is a
    - List

    ----
    I want a break <br> <font color="red">Text</font>
    ----
    '''
, unsafe_allow_html=True)


########################
df = pd.read_csv('raw_data/basic_eng.csv')

line_count = st.slider('Select how may rows you want to display', 1, 10, 3)
display_df = df.head(line_count)

display_df

####################

image = get_spect()
fig, ax = plt.subplots()

ax.plot(image)

st.pyplot(fig)
# st.image(image)


###################

# @st.cache
# def get_model(path_model):
#     return tf.load(path_model)
