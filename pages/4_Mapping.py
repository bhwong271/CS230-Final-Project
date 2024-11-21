import pydeck as pdk
import pandas as pd
import streamlit as st

MAP_STYLES = {
    "Streets": 'mapbox://styles/mapbox/streets-v11',
    "Outdoors": 'mapbox://styles/mapbox/outdoors-v11',
    "Light": 'mapbox://styles/mapbox/light-v10',
    "Dark": 'mapbox://styles/mapbox/dark-v10',
    "Satellite": 'mapbox://styles/mapbox/satellite-v9',
    "Satellite Streets": 'mapbox://styles/mapbox/satellite-streets-v11',
    "Navigation Day": 'mapbox://styles/mapbox/navigation-day-v1',
    "Navigation Night": 'mapbox://styles/mapbox/navigation-night-v1'
}

df=pd.read_csv("Fortune_500_Corporate_Headquarters.csv")
df_map = df.filter(["NAME", "LATITUDE", "LONGITUDE"])
#create map (largely taken from the example, but I understand where it comes from)
def custom_map(df):

    st.header("Map of the Fortune 500 Companies")
    custom_map_style = st.selectbox("Select Map Style",
                                     list(MAP_STYLES.keys()))
    st.write("Using Map Style", custom_map_style)
    view_state = pdk.ViewState(
        latitude=df["LATITUDE"].mean(),
        longitude=df["LONGITUDE"].mean(),
        zoom=2.75,
        pitch=0)

    layer1 = pdk.Layer('ScatterplotLayer',
                      data=df,
                      get_position='[LONGITUDE, LATITUDE]',
                      get_radius=50000,
                      get_color=[0,0,255],   # big red circle
                      pickable=True
                      )
    # simple tool tip
    tool_tip = {"html" : "This is:<br><b>{NAME}</b>",'Style': {'backgroundColor': 'steelblue', 'color': 'white'}}
    # stylish tool tip

    map = pdk.Deck(
        map_style= MAP_STYLES[custom_map_style],
        initial_view_state=view_state,
        layers=[layer1],
        tooltip= tool_tip
    )

    st.pydeck_chart(map)
custom_map(df_map)
#[MAP]