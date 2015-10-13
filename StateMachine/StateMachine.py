# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 10:31:21 2015

@author: uidj5872
"""

# State using a template method.

class StateMachine:
    def __init__(self, initialState, userData, friendshipData):
        self.currentState = initialState
        self.userData = userData
        self.friendshipData = friendshipData
        self.run_next(self.currentState.run(self.userData,self.friendshipData))
      
    # Template method:
    def run_next(self, inputs):
        self.currentState = self.currentState.next(inputs)
        self.run_next(self.currentState.run(self.userData,self.friendshipData))
        
        