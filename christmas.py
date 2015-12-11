

##getting the lyric data

import random
import csv

print "Welcome to the Christmas Lyric Quiz!"

v1 = raw_input("Type the word 'Jolly' when you are ready to play!   ")

#f1 = open("lyrics.md")

#lyric = f1.readlines()

#random.sample(lyric,1)

#print selected_lyric.split(" ")

songs = {
	'Jingle Bells':'Oh what fun it is to ride', 
	'Rudolph the Red-nosed Reindeer':'And if you ever saw it you would even',
	'Frosty the Snowman':'With a corncob pipe and a button nose'
	}

answers = ("Jingle Bells","Rudolph the Red-nosed Reindeer","Frosty the Snowman","White Christmas","I saw grandma kissing Santa Clause")

if(v1 == "Jolly" or v1 == "jolly"):
#	random_selection = random.choice(songs.values())
	print "Your lyric is: "
#	print random_selection
	with open('christmas_songs.csv')
	print "your multiple choice options are: "
	print random.sample(answers,3)
else:
	print "no play"

