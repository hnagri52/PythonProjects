import pygame
import webbrowser
import time
import os
import datetime as dt
with open("water.txt", "a+") as file:
    file.write("log time is: " + str(dt.datetime.now() ) + "\n")

songs = ["paani.mp3", "eyes.mp3", "physical.mp3"]

print(dt.datetime.now() )

pygame.mixer.init()
pygame.mixer.music.load("/Users/husseinnagri/Desktop/Frontend_Learning/PythonLearning/HealthyProgrammer/water.mp3")
pygame.mixer.music.play(0)
pygame.mixer.music.set_volume(0.6)
print(pygame.mixer.music.get_volume())


text = input("hello")
os.system("afplay water.mp3")
if text == "hello":
    os.system("killall iTunes")