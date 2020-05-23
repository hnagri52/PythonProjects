import requests
import json
from dotenv import load_dotenv
import os
load_dotenv()



def main():
    YOUTUBE_SECRET_KEY = os.getenv("YOUTUBE_API")
    HAPPI_SECRET_KEY = os.getenv("HAPPI_API")

    text = input("Enter the song name you want to play!")

    while(text != 'q'):
        # delete youtube api get youtube id cuz other api not working as well
        # payload = {'part': 'snippet', 'key': YOUTUBE_SECRET_KEY, 'order': 'relevance', 'q': text, 'maxResults': 1}
        # resp = requests.Session().get('https://www.googleapis.com/youtube/v3/search', params=payload)
        # resp_dict = json.loads(resp.content)
        # youtube_id = resp_dict['items'][0]["id"]["videoId"]

        # apiurl = requests.get(f"https://www.ytvdgrabber.com/api/get?youtubeid={youtube_id}")
        #
        # print(apiurl.content)

        apiUrl = requests.get(f"https://api.happi.dev/v1/music?q={text}&limit=1&apikey={HAPPI_SECRET_KEY}&type=track")

        print(apiUrl.content)




        text = input("Enter the song name you want to play!")


if __name__ == '__main__':
    main()



