import requests
import re
import json
import streamlit as st
from bokeh.models.widgets import Div
from streamlit.components.v1 import html

def open_page(url):
    open_script= """
        <script type="text/javascript">
            window.open('%s', '_blank').focus();
        </script>
    """ % (url)
    html(open_script)
#2.4.3
st.text("Youtube Video Downloader")
link = st.text_input(label="Paste Link Here", value="", max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, args=None, kwargs=None, placeholder=None, disabled=False, label_visibility="visible")
st.info("HOW TO USE: Paste youtube link into the textbox, and click the button that appears. It will lead you to a video player. From there you can right click and save the video. Make sure to allow popups from this page, or the button won't work", icon="ℹ")

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
            linkbut = st.button(label="Open Downloadable Link", key=None, help=None, on_click=open_page(mp4_url), args=None, kwargs=None, type="primary", disabled=False)
            
    except:
        st.text("Invalid Link")

    else:
        st.text("Failed to locate player")
