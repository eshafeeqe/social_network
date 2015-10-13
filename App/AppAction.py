# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 10:46:28 2015

@author: uidj5872
"""

class AppAction:
    def __init__(self, action):
        self.action = action
    def __str__(self): return self.action
    def __cmp__(self, other):
        return cmp(self.action, other.action)
    # Necessary when __cmp__ or __eq__ is defined
    # in order to make this class usable as a
    # dictionary key:
    def __hash__(self):
        return hash(self.action)

# Static fields; an enumeration of instances:
AppAction.start_req = AppAction("App starts")
AppAction.login_req = AppAction("App login request")
AppAction.signup_req = AppAction("App signup request")
AppAction.userpage_req = AppAction("App user page request")
AppAction.logout_req = AppAction("App logout request")
AppAction.friendlist_req = AppAction("App friend list request")
AppAction.friendreqsentlist_req = AppAction("App friend reuest sent list request")
AppAction.friendreqgotlist_req = AppAction("App request for frindship req got")
AppAction.otheruserlist_req = AppAction("App other users list request")
AppAction.close_req = AppAction("App close request")

