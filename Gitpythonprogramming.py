#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

def tts(text):
      return os.system("espeak  -s 120 -a 300 "+text+" " )

class Place:
    def house(self):
		print ""
		print "You are in an old deserted building, where is quite dark."
		print "You dont like to stay in one place too long and you start thinking what to do next"
		print ""
		tts("'You are in an old deserted building, where is quite dark. \
		You dont like to stay in one place too long and you start thinking what to do next' ")

    def doors(self):
		print ""
		print "You are looking at two doors, one to the right and second to the left"
		print "The door to the left has some sort of scratching marks and same has doorsteps"
		print "Door to the right is a little stuck"
		print ""
		tts("'You are looking at two doors, one to the right and second to the left. \
		The door to the left has some sort of scratching marks and same has doorsteps. \
		Door to the right is a little stuck.' ")

    def right_door(self):
        print "You chose right door, it seems to be best option so far"
        tts("'You chose right door, it seems to be best option so far' ")

    def left_door(self):
		print "You wanted to look brave and still desided to pick left door. \
		After you opened the door, there was only long hallway infront of you."
		tts("'You wanted to look brave and still disided to pick left door. \
		After you opened the door, there was only long hallway infront of you.' ")


    def coridor(self):
		print " "
		print "Hallway is dark and both left and right side has 3 doors \
		Straight ahead is also a door. All doors look the same, a little damaged \
		but the door up ahead seems to be the most damaged. As you go closer \
		you hear somesort of sound"
		tts("'Coridor is dark and both left and right side has 3 doors \
		Straight ahead is also a door. All doors look the same, a little damaged \
		but the door up seems to be the most damaged. As you go closer \
		you hear somesort of sound: ssssssssss' ")

    def choice(self, choice):
        self.choice = choice
        if choice == "right":
            kht.right_door()
            
            
        elif choice == "left":
            kht.left_door()
            kht.coridor()


class Creature:
    def dark_shadow(self):
		print "Somesort of dark statuse, does not move. Just standing and nothing else \
		Looking at it from far, you understand nothing. Maybe it is somekind of creature \
		or maybe just some thing that looks like a creature"
		tts("'Somesort of dark statuse, does not move. Just standing and nothing else \
		Looking at it from far, you understand nothing. Maybe it is somekind of creature \
		or maybe just some thing that looks like a creature ")


class Player:
    
    def createname(self, name):
        self.name = name

    def display_name(self):
        return self.name

    def saying(self):
        print "welcome to game %s!" % self.name
        tts("'Welcome to the game "+str(self.name) +" : ' ")
        

    
mngja=Player()
mngja.createname(raw_input("Enter name: "))
mngja.saying()
kht=Place()
kht.house()
kht.doors()
kht.choice(raw_input("You are thinking to go to right or left: "))
