#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 14:02:25 2020

@author: sebastian henao santa
"""

import datetime

last_id = 0



class Notebook:
    
    def __init__(self):
        self.notes = []
    
    def new_note(self, memo, tags = ""):
        self.notes.append(Note(memo, tags))
    
    def find_note(self, note_id):
        for note in self.notes:
            if note.id == note_id:
                return note
        return None
    
    def modify_memo(self, note_id, memo):
        self.find_note(note_id).memo = memo
        
        
               
    def modify_tags(self, note_id, tags):
    
        self.find_note(note_id).tags = tags
           
        
    def search(self, filter):
        return [note for note in self.notes if note.math(filter)]

class Note(object):
    
    def __init__(self, memo, tags = ""):
        self.memo = memo
        self.creation_date = datetime.date.today()
        self.tags = tags
        global last_id
        last_id += 1
        self.id = last_id

    def math(self, filter):
        return filter in self.memo or filter in self.tags
    
    
    







