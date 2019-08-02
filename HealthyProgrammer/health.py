import pygame
import time
import datetime as dt
with open("water.txt", "a+") as file:
    file.write("log time is: " + str(dt.datetime.now() ) + "\n")

songs = ["paani.mp3", "eyes.mp3", "physical.mp3"]

print(dt.datetime.now() )
pygame.init()
pygame.display.set_mode((200,100))

pygame.mixer.init()
pygame.mixer.music.load("paani.mp3")
pygame.mixer.music.play(0,0)
pygame.mixer.music.set_volume(0.6)
print(pygame.mixer.music.get_volume())
