import pygame
import time
import os
import random
import datetime as dt
def main():

    songs = ["water.mp3", "eyes.mp3", "physical.mp3"]
    pygame.mixer.init()
    pygame.init()
    i = 1
    waterleft = 2.0
    now = dt.datetime.now()
    today9am = now.replace(hour=9, minute=0, second=0, microsecond=0)
    today5pm = now.replace(hour=17, minute=0, second=0, microsecond=0)

    while i == 1: #today9am >= now and today5pm <= now:
        if dt.datetime.now().minute == 0:
            pygame.mixer.music.load(songs[0])
            pygame.mixer.music.play(loops=10000, start=0.0)
            pygame.mixer.music.set_volume(10)
            text = input("Time to drink water!! Enter drank to indicate you finished 250 ml of water")
            if text.lower() == "drank":
                pygame.mixer.music.stop()
            with open("water.txt", "a+") as file:
                file.write("log time is: " + str(dt.datetime.now()) + " and I drank 250 mL right now!\n")
            waterleft = waterleft - 0.25
            print(f"I have {waterleft} more L of water to drink")
        if dt.datetime.now().minute == 55 or dt.datetime.now().minute == 30:
            pygame.mixer.music.load(songs[1])
            pygame.mixer.music.play(loops=10000, start=0.0)
            pygame.mixer.music.set_volume(10)
            text = input("Time to exercise your eyes!! Enter eye to indicate you finished 250 ml of water")
            if text.lower() == "eye":
                pygame.mixer.music.stop()
            with open("eyes.txt", "a+") as file:
                file.write("log time is: " + str(dt.datetime.now()) + " and I exercised my eyes right now!\n")

        pygame.mixer.music.load(songs[2])
        pygame.mixer.music.play(loops=10000, start=0.0)
        pygame.mixer.music.set_volume(10)

        text = input("Enter the time")
        if text == "hello":
            pygame.mixer.music.stop()
        i = 0


if __name__ == '__main__':
    main()
