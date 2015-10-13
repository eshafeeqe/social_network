# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 15:20:05 2015

@author: DELLL
"""

import easygui
#import data

__all__ = ['first_box', 'login_page','signup_page','user_page','error_msg', 'friends_list', 'friends_req_sent', 'friends_req_got', 'other_users'  ]


def msg_maker(list_of_users):
    string = ""
    for i in range(0,len(list_of_users)):
        string =  string + "\n" + str(list_of_users[i][0])
    return string
 
def choice_maker(list_of_users):
    choice = []
    for i in range(0,len(list_of_users)):
        choice.append(list_of_users[i][0])
    return choice

def remove_current_user(people,username):
    for i in range(0,len(people)):
        if people[i][0] == username:
            del people[i]
            break
     

    
def first_box():
    response = easygui.buttonbox('Please Login or Sign Up', 'Login Page', ('login', 'signup'))
    return response
    
def login_page(userData):
    msg = "Enter User Name and Password"
    title = "Login Box"
    fieldNames = ["User Name","Password"]
    fieldValues = []  # we start with blanks for the values
    fieldValues = easygui.multpasswordbox(msg,title, fieldNames)
    
    # make sure that none of the fields was left blank
    while 1:
        if fieldValues == None: break
        errmsg = ""
        if userData.check_username_pssword(fieldValues[0], fieldValues[1]) == False : 
            errmsg = errmsg + ('Wrong Credentials\n')
        
        for i in range(len(fieldNames)):
          if fieldValues[i].strip() == "":
            errmsg = errmsg + ('"%s" is a required field.\n\n' % fieldNames[i])
        if errmsg == "": break # no problems found
        fieldValues = easygui.multpasswordbox(errmsg, title, fieldNames, fieldValues)
    
    
    return fieldValues

def signup_page(userData):
    msg = "Enter following details for signup"
    title = "SignUp Box"
    fieldNames = ["User Name",'Name',"Password"]
    fieldValues = []  # we start with blanks for the values
    fieldValues = easygui.multpasswordbox(msg,title, fieldNames)
    
    # make sure that none of the fields was left blank
    while 1:
        if fieldValues == None: break
        errmsg = ""
        if userData.check_username(fieldValues[0]) == False : 
            errmsg = errmsg + ('"%s" username already taken\n' % fieldValues[0])
        for i in range(len(fieldNames)):
          if fieldValues[i].strip() == "":
            errmsg = errmsg + ('"%s" is a required field.\n' % fieldNames[i])
        if errmsg == "": break # no problems found
        fieldValues = easygui.multpasswordbox(errmsg, title, fieldNames, fieldValues)
    
    return fieldValues
    
def user_page(userData):
    msg ="Hello " + userData.Name 
    title = "Welcome to Social Network"
    choices = ["Friends", "Friend Request Sent", "Friend Request got", "Other Users", "LogOut"]
    user_resp = easygui.buttonbox(msg, title, choices)
    return user_resp


def friends_list(userData, friendshipData):
    people = friendshipData.get_friends(userData.Username)
    msg ="Hello " + userData.Name +" \n" + msg_maker(people)
    title = "Friend List"
    choices = ["Back"]
    user_resp = easygui.buttonbox(msg, title, choices)
    return user_resp
    
def friends_req_sent(userData, friendshipData):
    people = friendshipData.get_friendship_reqests(userData.Username)
    msg ="Hello " + userData.Name +" \n" + msg_maker(people)
    title = "Friend req sent list"
    choices = ["Back"]
    user_resp = easygui.buttonbox(msg, title, choices)
    return user_resp

def friends_req_got(userData, friendshipData):
    people = friendshipData.get_friendship_incoming_reqests(userData.Username)
    msg ="Hello " + userData.Name +" \n" + "Please select users for accepting Freind Request"
    title = "Friend req got"
    choices = choice_maker(people)
    user_resp = easygui.multchoicebox(msg, title, choices)
    return user_resp

def other_users(userData, friendshipData):
    people = friendshipData.get_other_users(userData.Username)
    remove_current_user(people, userData.Username)
    msg ="Hello " + userData.Name +" \n\n" + "Please select users for sending Freind Request"  
    title = "Other Users"
    choices = choice_maker(people)
    user_resp = easygui.multchoicebox(msg, title, choices)
    return user_resp


def error_msg(msg):
    easygui.msgbox(msg, 'Error Message')
    

