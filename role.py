#!/usr/bin/env python3.8

minLength = 5
lowers = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
characters = ['!','@','#','$','%','^','&','*','(',')','[',']','{','}','+','-','_','=','|','/','\',''','"',':',';','<','>','.',' ','?']
numbers = [1,2,3,4,5,6,7,8,9,10]

def validate(password, score = 0) :
    if len(password) >= minLength :
        score += 1

    for node in lowers :
        # find lowercase words
        if password.find(node) != -1 :
            score += 1
        # find uppercase words
        if password.find(node.upper()) != -1 :
            score += 1

    for node in numbers :
        # find numbers
        if password.find(str(node)) != -1 :
            score += 1

    for node in characters :
        # find characters
        if password.find(node) != -1 :
            score += 1
    return score
