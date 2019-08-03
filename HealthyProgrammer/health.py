import pygame
import time
import os
import datetime as dt
with open("water.txt", "a+") as file:
    file.write("log time is: " + str(dt.datetime.now() ) + "\n")

songs = ["paani.mp3", "eyes.mp3", "physical.mp3"]

print(dt.datetime.now() )



pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('water.mp3')
i = 0
while i<1:
    pygame.mixer.music.load('water.mp3')
    pygame.mixer.music.play(loops=10, start=0.0)
    time.sleep(35)
    pygame.mixer.music.set_volume(10)

    text = input("Enter the time")
    if text == "hello":
        i = i + 1