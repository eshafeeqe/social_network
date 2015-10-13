# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 15:49:21 2015

@author: uidj5872
"""
from Data.DataHouse import DataHouse

class FriendshipTable(DataHouse):
    def __friendship_table_create(self,):
        connecter, cursor = self.db_connect()
        sql = 'create table if not exists friendship (id INT PRIMARY KEY, username1 TEXT NOT NULL, username2 TEXT NOT NULL)'
        cursor.execute(sql)
        self.db_disconnect(connecter, cursor)

    def __friendship_req_table_create(self,):
        connecter, cursor = self.db_connect()
        sql = 'create table if not exists friendship_request (id INT PRIMARY KEY, username1 TEXT NOT NULL, username2 TEXT NOT NULL)'
        cursor.execute(sql)
        self.db_disconnect(connecter, cursor)

    def __init__(self,):
        self.__friendship_table_create()      
        self.__friendship_req_table_create()    
    
    def add_frienship_req(self, username1, username2_list):
        connecter, cursor = self.db_connect()
        for i in range(0,len(username2_list)):
            sql = 'INSERT INTO friendship_request (username1, username2) VALUES ("'+ username1 +'","' + username2_list[i] +'");' 
            cursor.execute(sql)
            
        self.db_disconnect(connecter, cursor)
       
    def add_frienship(self, username1, username2_list):
        
        print username1, username2_list
        for i in range(0,len(username2_list)):
            connecter, cursor = self.db_connect()
            sql = 'INSERT INTO friendship (username1, username2) VALUES ("'+ username1 +'","' + username2_list[i] +'");' 
            cursor.execute(sql)
            sql = 'INSERT INTO friendship (username1, username2) VALUES ("'+ username2_list[i] +'","' + username1 +'");' 
            cursor.execute(sql)
            self.db_disconnect(connecter, cursor)
            connecter, cursor = self.db_connect()
            sql = 'DELETE FROM friendship_request WHERE username1 = "' + username2_list[i] +'" and username2 ="' + username1 +'";'     
            cursor.execute(sql)
            self.db_disconnect(connecter, cursor)
    
    def get_friends(self, username):
        connecter, cursor = self.db_connect()
        sql = 'select username, name FROM users where username in  ( select username2 FROM friendship where username1 = "' + username + '");'
        out = cursor.execute(sql)
        result = out.fetchall()
        self.db_disconnect(connecter, cursor)
        return result    
        
    def get_friendship_reqests(self, username):
        connecter, cursor = self.db_connect()
        sql = 'select username, name FROM users where username in  ( select username2 FROM friendship_request where username1 = "' + username + '");'
        out = cursor.execute(sql)
        result = out.fetchall()
        self.db_disconnect(connecter, cursor)
        return result 
        
    
    def get_friendship_incoming_reqests(self, username):
        connecter, cursor = self.db_connect()
        sql = 'select username, name FROM users where username in  ( select username1 FROM friendship_request where username2 = "' + username + '");'
        out = cursor.execute(sql)
        result = out.fetchall()
        self.db_disconnect(connecter, cursor)
        return result 
    
    def get_other_users(self, username):
        connecter, cursor = self.db_connect()
        #sql = 'select username, name FROM users where username not in  ( select username2 FROM friendship where username1 = "' + username + '");'
        sql = 'select username, name FROM users where username not in (select username2 FROM friendship where username1 = "' + username + '" union select username2 FROM friendship_request where username1 = "' + username + '" union select username1 FROM friendship_request where username2 = "' + username + '" );'
        out = cursor.execute(sql)
        result = out.fetchall()
        self.db_disconnect(connecter, cursor)
        return result 
