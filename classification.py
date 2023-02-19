from apiclient.discovery import build 
from apiclient.errors import HttpError 
from oauth2client.tools import argparser
import pandas as pd


youTubeApiKey="AIzaSyBmTVAD8XU4NOnJaZJrTD7w4y0UTC-yILg" #Input your youTubeApiKey
youtube=build('youtube','v3',developerKey=youTubeApiKey)

videos = []

next_page_token = None

while 1:
    res = youtube.videos().list(part="snippet,statistics",
                                chart="chartUnspecified",
                                regionCode="US",maxResults=50,
                                pageToken=next_page_token).execute()
    videos += res['items']
    
    next_page_token = res.get('nextPageToken')

    if next_page_token is None:
        break


print(videos)