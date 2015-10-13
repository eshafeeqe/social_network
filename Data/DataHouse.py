# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 13:40:36 2015

@author: uidj5872
"""


import sqlite3

database_name = 'example.db'

class DataHouse:
    def db_connect(self,):
        connecter = sqlite3.connect(database_name)
        cursor = connecter.cursor()
        return connecter, cursor
    def db_disconnect(self,connecter,cursor):
        connecter.commit()
        cursor.close()
        connecter.close()

        


        
        
