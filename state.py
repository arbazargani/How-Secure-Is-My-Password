#!/usr/bin/env python3.8

lowScore = 2
middScore = 6
highScore = 8

def ShowState(score) :
    if score < middScore :
        print("Your password is very poor !")
    if score >= middScore and score < highScore :
        print("Your password is good, but it can be better.")
    if score >= middScore :
        print("Great, Your password is secure.")