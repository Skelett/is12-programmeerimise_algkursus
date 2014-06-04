#!/usr/bin/env python
# -*- coding: cp1257 -*-
import os
import sys


class Place:
    def vahe(self):
        print " "

    def house(self):
        kht.vahe()
        print """Olete mahajäetud majas, kus on suhteliselt pime.
Väga eriti ühe koha peale olla ei taha. Hakata mõtlema kuhu edasi minna."""

    def doors(self):
        kht.vahe()
        print"""Teie silmate kahte ust. Üks ustest on paremal ja teine vasakul.
Vasakul olev uks on natuke kriibitud ja üksepiita on ka kraabitud. Paremal olev
uks see pastab olevat natuke kinni kiilunud."""

    def right_door(self):
        kht.vahe()
        print """Valisite parema ukse. Parem uks tundus olevat parem valik.
Esialgu muidugi oli natuke raske sisse saada, aga tugeva lükkamise peale see
õnnestus."""

    def left_door(self):
        kht.vahe()
        print"""Tahtsite näida julge ning otsustasite siiski valida vasaku ukse.
Avasite ukse ning ees oli pikk koridor."""

    def coridor(self):
        kht.vahe()
        print"""Koridor on pime ning paremal ja vasakul on 3 ust. Kõige otse
samuti mingi uks. Kõik uksed väga üksteisest ei erine. Küll aga kõik otse ees
olev uks näib olevat kõige rohkem kahju saanud. Lähemale minnes kuulete mingit
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
või mingi ese."""


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
kht.choice(raw_input("Mõtlete kas minna right or left: "))

