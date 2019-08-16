import pygame
import time
import os
import random
import datetime as dt
from datetime import time

def musiconloop(song, keyword):
    pygame.mixer.init()
    pygame.mixer.music.load(song)
    pygame.mixer.music.play()
    while True:
        inp = input(f"Please enter {keyword} to continue: ")
        if inp == keyword:
            pygame.mixer.music.stop()
            break;


def log_now(file, message):
    with open(file,  "a+") as file:
        file.write(f"log time is: " + str(dt.datetime.now()) + f" {message} \n")


def main():
    musiconloop("water.mp3", "stop")
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    watersecs = 40*60
    exsecs = 30*60
    eyessecs = 45*60

    while True:
        if time() - init_water > watersecs:
            print("Water Drinking time. Enter 'drank' to stop the alarm.")
            musiconloop('water.mp3', 'drank')
            init_water = time()
            log_now("Drank Water at")

        if time() - init_eyes >eyessecs:
            print("Eye exercise time. Enter 'doneeyes' to stop the alarm.")
            musiconloop('eyes.mp3', 'doneeyes')
            init_eyes = time()
            log_now("Eyes Relaxed at")

        if time() - init_exercise > exsecs:
            print("Physical Activity Time. Enter 'donephy' to stop the alarm.")
            musiconloop('physical.mp3', 'donephy')
            init_exercise = time()
            log_now("Physical Activity done at")

if __name__ == '__main__':
    main()






"""
First attempt:

    songs = ["water.mp3", "eyes.mp3", "physical.mp3"]
    pygame.mixer.init()
    pygame.init()
    i = 1
    waterLeft = 2.0
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
            waterLeft = waterLeft - 0.25
            print(f"I have {waterLeft} more L of water to drink")
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
"""

if __name__ == '__main__':
    main()
