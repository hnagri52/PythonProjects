"""Will read aloud all of the top headlines from the news API"""
from gtts import gTTS
import os
import requests
import json


def readArticls(str):

    mytext = str
    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save("welcome.mp3")
    os.system("mpg321 welcome.mp3")

def main():
    random_string = "'"
    url =  ('https://newsapi.org/v2/top-headlines?'
       'country=us&'
       'apiKey=31eed951eb644d5f9f882dc05db21d11')
    response = requests.get(url)
    print(response.json() )
    data = json.loads(response.text)
    for i in range(20):
        random_string = data["articles"][i]["title"]
        readArticls(random_string)


    # for item in data["articles"][1]["title"]:
    #     print("This is what i am printing: " + item)
    #     random_string = random_string + item
    #     i = i+1


    print(random_string)










if __name__ == '__main__':
    main()