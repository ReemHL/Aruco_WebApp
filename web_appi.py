import streamlit as st
import numpy as np # constructing arrays 
import skimage.io as io # read images in from files on your computer, to a form usable in a Python program
#import matplotlib.pyplot as plt # what does?
from PIL import Image # data visualization, typically in the form of plots, graphs and charts
import glob # list of pics
from PIL.ExifTags import TAGS # what does?
import cv2 as cv2 # what does?

logo = 'logo.png'

# main page
st.set_page_config(page_title='Bring It', page_icon = logo , layout = 'wide', initial_sidebar_state = 'auto')
st.title('Image Something Using Somewhat by Reem Har Levi')

# side bar
st.markdown(
    """
    <style>
    [data-testid="stSidebar"][aria-expanded="true"] . div:first-child{
        width: 350px
    }
    
    [data-testid="stSidebar"][aria-expanded="false"] . div:first-child{
        width: 350px
        margin-left: -350px
    }    
    </style>
    
    """,
    unsafe_allow_html=True,


)

st.sidebar.title('Segmentation Sidebar')
st.sidebar.subheader('Site Pages')
