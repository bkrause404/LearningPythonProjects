import time
import webbrowser
import random
import sys

def addVideo():
	videoToAdd = raw_input("Enter the url of the video to add: ")
	with open('alarmVideos.txt', 'a') as f:
		f.write(videoToAdd + '\n')

def pickVideo():
	with open('alarmVideos.txt') as file:
		videosToUse = file.readlines()
	useVideo = random.choice(videosToUse)
	return useVideo


alarmTime = raw_input("When would you like to set your alarm to?: \nPlease use this format: 01:00 (24hr clock)\n")
localTime = time.strftime("%H:%M") 

add_Video = raw_input("Would you like to add a video to your list? (y/n): ")

if add_Video == 'y':
	addVideo()

print "\nYour alarm is set to:", alarmTime

while alarmTime != localTime:
	localTime = time.strftime("%H:%M") 
	time.sleep(1)

if alarmTime == localTime:
	controller = webbrowser.get()
	controller.open(pickVideo())
	sys.exit()