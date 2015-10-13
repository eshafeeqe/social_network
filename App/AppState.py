# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 11:00:46 2015

@author: uidj5872
"""
import sys

from StateMachine.State import State
from StateMachine.StateMachine import StateMachine
from App.AppAction import AppAction
from App.AppFunctions import *

class Firstbox(State):

    def run(self, userData, friendshipData):
        ret = first_box()        
        if ret == "login":
            return AppAction.login_req
        elif ret == "signup":
            return AppAction.signup_req
        else:
            return AppAction.close_req
            
    def next(self, input):
        if input == AppAction.login_req:
            return AppState.loginbox
        elif input == AppAction.signup_req:
            return AppState.signupbox
        elif input == AppAction.close_req:
            return AppState.closeapp
        return AppState.firstbox

class Loginbox(State):
    
    def run(self,userData, friendshipData):
       ret = login_page(userData)
       userData.Username  = ret[0]
       userData.Name = ret[1]
       return AppAction.userpage_req
       
    def next(self, input):
        if input == AppAction.userpage_req:
            return AppState.userpage
        elif input == AppAction.close_req:
            return AppState.closeapp
        return AppState.loginbox

class Signupbox(State):
    
    def run(self, userData, friendshipData):
        ret = signup_page(userData)
        userData.add_user(ret[0],ret[1],ret[2])
        userData.Username  = ret[0]
        userData.Name = ret[1]
        return AppAction.userpage_req
        
    def next(self, input):
        if input == AppAction.userpage_req:
            return AppState.userpage
        elif input == AppAction.close_req:
            return AppState.closeapp
        return AppState.signupbox

class Userpage(State):
    def run(self, userData, friendshipData):
        ret = user_page(userData)
        
        if ret == "Friends":
            return AppAction.friendlist_req
        elif ret == "Friend Request Sent":
            return AppAction.friendreqsentlist_req
        elif ret == "Friend Request got":
            return AppAction.friendreqgotlist_req
        elif ret == "Other Users":
            return AppAction.otheruserlist_req
        elif ret == "LogOut":
            userData.Username  = ret[0]
            userData.Name = ret[1]
            return AppAction.start_req    
        else:
            return AppAction.close_req
            

    def next(self, input):
        if input == AppAction.friendlist_req:
            return AppState.friendlist
        elif input == AppAction.friendreqsentlist_req:
            return AppState.friendreqsentlist
        elif input == AppAction.friendreqgotlist_req:
            return AppState.friendreqgotlist
        elif input == AppAction.otheruserlist_req:
            return AppState.otheruserlist
        elif input == AppAction.start_req:
            return AppState.firstbox
        elif input == AppAction.close_req:
            return AppState.closeapp
        return AppState.userpage
        
class Friendlist(State):
    def run(self, userData, friendshipData):
        ret = friends_list(userData, friendshipData)
        if ret == "Back":
            return AppAction.userpage_req
        else:
            return AppAction.close_req
        

    def next(self, input):
        if input == AppAction.userpage_req:
            return AppState.userpage
        elif input == AppAction.close_req:
            return AppState.closeapp
        return AppState.friendlist   

class Friendreqsentlist(State):
    
    def run(self, userData, friendshipData):
        ret = friends_req_sent(userData, friendshipData)
        if ret == "Back":
            return AppAction.userpage_req
        else:
            return AppAction.close_req
        
    def next(self, input):
        if input == AppAction.userpage_req:
            return AppState.userpage
        elif input == AppAction.close_req:
            return AppState.closeapp
        return AppState.Friendreqsentlist   
        
class Friendreqgotlist(State):
    def run(self, userData, friendshipData):
        ret = friends_req_got(userData, friendshipData)
        if ret == None:
            return AppAction.userpage_req
        else:
            friendshipData.add_frienship(userData.Username, ret)
            return AppAction.userpage_req

    def next(self, input):
        if input == AppAction.userpage_req:
            return AppState.userpage
        elif input == AppAction.close_req:
            return AppState.closeapp
        return AppState.friendreqgotlist   

class Otheruserlist(State):
    def run(self, userData, friendshipData):
        ret = other_users(userData, friendshipData)
        if ret == None:
            return AppAction.userpage_req
        else:
            friendshipData.add_frienship_req(userData.Username, ret)
            return AppAction.userpage_req
            
    def next(self, input):
        if input == AppAction.userpage_req:
            return AppState.userpage       
        elif input == AppAction.close_req:
            return AppState.closeapp
        return AppState.otheruserlist

class Closeapp(State):
    def run(self, userData, friendshipData):
        print "Closing App"
        sys.exit(0)

class AppState(StateMachine):
    def __init__(self, userData, friendshipData):
        # Initial state
        StateMachine.__init__(self, AppState.firstbox, userData, friendshipData)
        
# Static variable initialization:
AppState.firstbox = Firstbox()
AppState.loginbox = Loginbox()
AppState.signupbox = Signupbox()
AppState.userpage = Userpage()
AppState.friendlist = Friendlist()             
AppState.friendreqsentlist = Friendreqsentlist()
AppState.otheruserlist = Otheruserlist()
AppState.friendreqgotlist = Friendreqgotlist()
AppState.closeapp = Closeapp()             


