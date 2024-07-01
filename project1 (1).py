#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 16:45:12 2024

@author: israelrenfro_snhu
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from pymongo import MongoClient, errors  
from urllib.parse import quote_plus

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        USER = username
        PASS = password
        HOST = 'nv-desktop-services.apporto.com'
       
        PORT = 31837
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
        
# Complete this create method to implement the C in CRUD.
    def create(self, data):
        try:
            if data is not None:
                self.database.animals.insert_one(data)
                return True 
            else: 
                raise Exception("Nothing to save, because data parameter is empty") 
        except Exception as e: 
            print(e) 
            return False
            
    def read(self, query):
            """
            Query for documents in the collection.
            :param query: A dictionary representing the query criteria.
            :return: A list of documents matching the query, or an empty list if no matches.
            """
            if not isinstance(query, dict):
                raise ValueError("Query must be a dictionary")
            
            try:
                cursor = self.collection.find(query)
                return list(cursor)
            except errors.PyMongoError as e:
                print(f"Error querying documents: {e}")
                return []
    def update(self, criteria, update_data):
            try:
                if criteria is not None:
                    result = self.collection.update_many(criteria, {'$set': update_data})
                    return result.modified_count
                else:
                    raise Exception("No criteria provided for update operation")
            except Exception as e:
                print(e)
                return 0
    
    def delete(self, criteria):
        try:
            if criteria is not None:
                result = self.collection.delete_many(criteria)
                return result.deleted_count
            else:
                raise Exception("No criteria provided for delete operation")
        except Exception as e:
            print(e)
            return 0

