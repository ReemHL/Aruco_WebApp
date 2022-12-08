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

# add dropdown to select pages on left
app_mode = st.sidebar.selectbox('What?',
                                  ['A','B', 'C'])

# About page
if app_mode == 'A':
    st.markdown('In this app')
    
    
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
        unsafe_allow_html=True,)
    
# Load Aruco detector
parameters = cv2.aruco.DetectorParameters_create()
aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_5X5_50)

# Get Aruco marker
corners, _, _ = cv2.aruco.detectMarkers(mouse, aruco_dict, parameters=parameters)
# Draw polygon around the marker
int_corners = np.int0(corners)
cv2.polylines(mouse, int_corners, True, (0, 255, 0), 50)
st.imshow(mouse)
