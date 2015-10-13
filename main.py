# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 14:58:15 2015

@author: DELLL
"""


from App.AppState import AppState
from Data.UserTable import UserTable
from Data.FriendshipTable import FriendshipTable

userdata = UserTable()
frienshipdata = FriendshipTable() 
app = AppState(userdata,frienshipdata)