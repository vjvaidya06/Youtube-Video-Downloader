import requests
import re
import json
import streamlit as st
from bokeh.models.widgets import Div
#2.4.3
st.text("Youtube Video Downloader")
link = st.text_input(label="Paste Link Here", value="", max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, args=None, kwargs=None, placeholder=None, disabled=False, label_visibility="visible")
st.info('HOW TO USE: Paste youtube link into the textbox, and click the button that appears. It will lead you to a video player. From there you can right click and save the video.', icon="ℹ")

if link != "":
    try:
        response = requests.get(link)
        html_content = response.text
        player_response_pattern = r'ytInitialPlayerResponse\s*=\s*({.+?});'
        match = re.search(player_response_pattern, html_content)
        if match:
            player_response_json = match.group(1)
            player_response_dict = json.loads(player_response_json)
            mp4_url = player_response_dict["streamingData"]["formats"][0]["url"]
            linkbut = st.button(label="Open Downloadable Link", key=None, help=None, on_click=None, args=None, kwargs=None, type="primary", disabled=False)
            if linkbut:
                js = f"window.open('{mp4_url}')"
                js = f"window.location.href = '{mp4_url}'"
                html = '<img src onerror="{}">'.format(js)
                div = Div(text=html)
                st.bokeh_chart(div)
    except:
        st.text("Invalid Link")

    else:
        print("Failed to locate player")