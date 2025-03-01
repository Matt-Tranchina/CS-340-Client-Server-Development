#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 00:33:45 2025

@author: matthewtranch_snhu
"""
import pymongo
from pymongo import MongoClient
from pymongo import ReturnDocument

# CRUD operations for Animal collection in MongoDB
class AnimalShelter(object):
    def __init__(self, USER, PASS, HOST, PORT, DB, COL):
        
        # Initialize Connection, take in username and password and 
        # attempt to access database with credentials
        try:        
            self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
            self.database = self.client['%s' % (DB)]
            self.collection = self.database['%s' % (COL)]
            self.client.server_info()
            
        # If test has failed
        except pymongo.errors.OperationFailure:
            return 0
            
        
    # Create method
    def create(self, data):
        
        try:
            # If parameters are valid, a new document is created
            if data is not None:
                self.collection.insert_one(data)
                return 1
                
            # If parameter is empty, display error code
            else:
               raise Exception("Error due to parameter being empty")
        except Exception as e:
            print("Error: ", e)
            
            
    # Read method
    def read(self, data):
        
        # Attempt to search database with provided parameters
        try:
            if data is not None:
                return self.collection.find(data)
            
            # If parameter is empty, display all documents 
            elif data is None:
                return self.collection.find()
            
            else:
                return 0
        
            # Catch-all for any other violation, display error 
        except Exception as e:
           return print("Error:", e)
        
            
    # Update Many method
    def updateMany(self, keyword, newData):
        # Finds multiple documents and updates them all
        try:
            if keyword is not None:
                if newData is not None:
                    newDocuments = self.collection.update_many(keyword, {'$set': newData})
                    
                    # Displays number of documents updated
                    return (newDocuments.modified_count)
                
                # Displays error if parameter is empty
                else:
                    return 0
            
            # Displays error if filter parameter is invalid
            else:
                return 0
                
        
        # Catch-all for any other violation, displays error
        except Exception as e:
            return print("Error: ", e)
            
    
    
    # Update One method
    def updateOne(self, ID, newData):
        # Finds a single document and updates it
        try:
            if ID is not None:
                if newData is not None:
                    
                    # Updates and displays newly updated document
                    return (self.collection.find_one_and_update(ID, 
                            {'$set': newData}, return_document=ReturnDocument.AFTER))
            
            # If document was not found or parameter is empty
            else:
                return 0
                
        # Catch-all for any other violation, displays error
        except Exception as e:
            return print("Error: ", e)
            
    
    # Delete Many method
    def deleteMany(self, data): 
        # Finds and deletes all matching documents
        try:
            if data is not None:
                deletions = self.collection.delete_many(data)
                
                # Displays number of documents deleted
                return (deletions.deleted_count)
            
            # If data is empty, display error
            else:
                return 0
            
        # Catch-all for any other violation, display error
        except Exception as e:
            return print("Error: ", e)
        
        
    # Delete One method
    def deleteOne(self, data):
        # Finds a single document and deletes from database
        try:
            if data is not None:
                deletion = self.collection.delete_one(data)
                
                # Displays number of documents deleted, should always be 1
                return (deletion.deleted_count)
                
            # If data is empty, display error
            else:
                return 0
        
        # Catch-all for any other violation, display error
        except Exception as e:
            return print("Error: ", e)
                
            
