import requests
import json
from dotenv import load_dotenv
import os
import time
from twilio.rest import Client


load_dotenv()


def main():
    YOUTUBE_SECRET_KEY = os.getenv("YOUTUBE_API")
    HAPPI_SECRET_KEY = os.getenv("HAPPI_API")
    TWI_SID = os.getenv("TWI_SID")
    TWI_TOK = os.getenv("TWI_TOK")
    client = Client(TWI_SID, TWI_TOK)

    text = input("Enter a song name, and their artist name: ")


    while(text != 'q'):
        payload = {'part': 'snippet', 'key': YOUTUBE_SECRET_KEY, 'order': 'relevance', 'q': text, 'maxResults': 1}
        resp = requests.Session().get('https://www.googleapis.com/youtube/v3/search', params=payload)
        resp_dict = json.loads(resp.content)
        youtube_id = resp_dict['items'][0]["id"]["videoId"]

        # apiurl = requests.get(f"https://www.ytvdgrabber.com/api/get?youtubeid={youtube_id}")
        # ^^ was for bollywood stuff
        # print(apiurl.content)

        apiUrl = requests.get(f"https://api.happi.dev/v1/music?q={text}&limit=1&apikey={HAPPI_SECRET_KEY}&type=track")\
            .content.decode('utf-8')
        apiUrl = json.loads(apiUrl)

        if (len(apiUrl["result"]) == 0 or apiUrl["result"][0]["haslyrics"] == False ):
            print(apiUrl, "\n")
            text = input("No lyrics found with those search results! Enter the song name you want to play!")
            continue

        lyricLink = apiUrl["result"][0]["api_lyrics"]
        lyrics = requests.get(lyricLink + f"?apikey={HAPPI_SECRET_KEY}")

        lyrics_details = lyrics.content.decode('utf-8')
        lyrics = json.loads(lyrics_details)

        if (len(lyrics["result"]) == 0):
            print("No lyrics found with those search results! \n")
            continue

        lyrics = lyrics["result"]["lyrics"]
        listOfWords = lyrics.split("\n")
        listOfWords = [x for x in listOfWords if x != '']


        #send youtube link to video
        sendMessage(f"Here is a link to the song: https://www.youtube.com/watch?v={youtube_id}", client)

        #send lyrics
        for word in listOfWords:
            sendMessage(word, client)
            time.sleep(5)



        text = input("Enter the song name you want to play!")


def sendMessage(word, client):
    message = client.messages \
        .create(
        body=f'{word}',
        from_='+18706863507',
        to='+16473088537'
    )
    print(f"Just sent: {word}")


if __name__ == '__main__':
    main()



