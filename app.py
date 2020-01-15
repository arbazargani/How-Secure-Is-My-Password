#!/usr/bin/env python3.8

import role
import state

password = ""

print ("enter password", end = ': ')
password = str(input())

score = role.validate(password)

state.ShowState(score)