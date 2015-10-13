# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 15:48:01 2015

@author: uidj5872
"""

from Data.DataHouse import DataHouse

class UserTable(DataHouse):
    
    def __usertable_create(self,):
        connecter, cursor = self.db_connect()
        sql = 'create table if not exists users (username TEXT PRIMARY KEY NOT NULL, name TEXT NOT NULL, password TEXT NOT NULL )'
        cursor.execute(sql)
        self.db_disconnect(connecter, cursor)
   
    def __init__(self,):
        self.Username = 0
        self.Name = 0
        self.__usertable_create()   
        
    def add_user(self,username,name,password):
        connecter, cursor = self.db_connect()
        sql = 'INSERT INTO users (username, name, password) VALUES ("'+ username +'","' + name + '","' + password +'");' 
        cursor.execute(sql)
        self.db_disconnect(connecter, cursor)
        
    def check_username(self,user_name):
        connecter, cursor = self.db_connect()
        sql = 'select * from users where username = "'+ user_name +'";'
        out = cursor.execute(sql)
        result = out.fetchall()
        self.db_disconnect(connecter, cursor)
        if len(result)>0:
            return False
        return True
        
    def check_username_pssword(self,username,password):
        connecter, cursor = self.db_connect()
        sql = 'select * from users where username = "'+ username +'";'
        out = cursor.execute(sql)
        result = out.fetchone()
        self.db_disconnect(connecter, cursor)
        if result != None and result[2] ==  password:
            return True
        return False
    
    def all_users(self,):
        connecter, cursor = self.db_connect()
        sql = 'select username, name FROM users;'
        out = cursor.execute(sql)
        result = out.fetchall()
        self.db_disconnect(connecter, cursor)
        return result
    