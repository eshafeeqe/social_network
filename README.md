# Social Network Simulation

A python package for simulating social network

#Features
1) login/signup.  
2) See the other users.  
3) Sent friend requests.  
4) See the friend requests got.   
5) Check friends.  

#How to Run:
1) Download the package.   
2) Install python 2.7.  
3) Run main.py in python console.  

#Flow Diagram
![alt tag](https://raw.githubusercontent.com/eshafeeqe/social_network/master/flow_diagram.jpg)
<br>
#Few Words about architecture and files
1) Implemented as a state machine.   
2) State machine and state definition is defined in the folder StateMachine.    
3) App folder responsible for all application related functionalities.   
&nbsp;&nbsp;&nbsp;&nbsp;a) AppAction.py:- Different actions that can change state of the app is defined.  
&nbsp;&nbsp;&nbsp;&nbsp;b) AppState.py :- Different states of the application and state trasition with respect to app actions defined.  
&nbsp;&nbsp;&nbsp;&nbsp;c) AppFunctions.py :- Specific GUI functions required for different states of application defined.  
4) Data folder responsible for all database related functionalities.  
&nbsp;&nbsp;&nbsp;&nbsp;a)DataHouse.py :- Main database class defined which contains function for connecting and manipulating database.  
&nbsp;&nbsp;&nbsp;&nbsp;b)UserTable.py :- Responsible for all the user related data access functionalities.  
&nbsp;&nbsp;&nbsp;&nbsp;c)FriendshipTable.py :- Responsible for all the friendship related data access functionalities.  
5) easygui is a lightweight third party library for GUI functionalities.   
