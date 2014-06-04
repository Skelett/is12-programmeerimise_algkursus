#!/usr/bin/env python
# -*- coding: cp1257 -*-
import os
import sys


class Place:
    def vahe(self):
        print " "

    def house(self):
        kht.vahe()
        print """Olete mahaj�etud majas, kus on suhteliselt pime.
V�ga eriti �he koha peale olla ei taha. Hakata m�tlema kuhu edasi minna."""

    def doors(self):
        kht.vahe()
        print"""Teie silmate kahte ust. �ks ustest on paremal ja teine vasakul.
Vasakul olev uks on natuke kriibitud ja �ksepiita on ka kraabitud. Paremal olev
uks see pastab olevat natuke kinni kiilunud."""

    def right_door(self):
        kht.vahe()
        print """Valisite parema ukse. Parem uks tundus olevat parem valik.
Esialgu muidugi oli natuke raske sisse saada, aga tugeva l�kkamise peale see
�nnestus."""

    def left_door(self):
        kht.vahe()
        print"""Tahtsite n�ida julge ning otsustasite siiski valida vasaku ukse.
Avasite ukse ning ees oli pikk koridor."""

    def coridor(self):
        kht.vahe()
        print"""Koridor on pime ning paremal ja vasakul on 3 ust. K�ige otse
samuti mingi uks. K�ik uksed v�ga �ksteisest ei erine. K�ll aga k�ik otse ees
olev uks n�ib olevat k�ige rohkem kahju saanud. L�hemale minnes kuulete mingit
heli <sound>"""

    def choice(self, choice):
        self.choice = choice
        if choice == "right":
            kht.right_door()
            
            
        elif choice == "left":
            kht.left_door()
            kht.coridor()


class Creature:
    def dark_shadow(self):
        print"""Mingisugune tume kuju, liikumatu. Lihtsalt seisab ja
ei tee midagi. Eemalt vaadates ei saa midagi aru. Ei saa aru kas on mingi olend
v�i mingi ese."""


class Player:
    
    def createname(self, name):
        self.name = name

    def display_name(self):
        return self.name

    def saying(self):
        print "welcome to game %s!" % self.name
        

    
mngja=Player()
mngja.createname(raw_input("Enter name: "))
mngja.saying()
kht=Place()
kht.house()
kht.doors()
kht.choice(raw_input("M�tlete kas minna right or left: "))

