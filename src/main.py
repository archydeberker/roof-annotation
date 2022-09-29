import leafmap.foliumap as leafmap
import streamlit as st
from folium.plugins import Draw
from streamlit_folium import st_folium

m = leafmap.Map(google_map="SATELLITE")

Draw(export=True).add_to(m)

import numpy as np
def shoelace(x_y):
    """https://stackoverflow.com/questions/41077185/fastest-way-to-shoelace-formula"""
    x_y = np.array(x_y)
    x_y = x_y.reshape(-1,2)

    x = x_y[:,0]
    y = x_y[:,1]

    S1 = np.sum(x*np.roll(y,-1))
    S2 = np.sum(y*np.roll(x,-1))

    area = .5*np.absolute(S1 - S2)

    return area

c1, c2 = st.columns([4, 1])
with c1:
    output = st_folium(m, width=700, height=500)

with c2:
    st.write(output)

polygon = output["last_active_drawing"]["geometry"]["coordinates"]
st.header(f"Area is {shoelace(polygon)}")
