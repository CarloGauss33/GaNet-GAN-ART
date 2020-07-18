# This is a web scrapper of impressionist pieces of art
# aplogies in advance if any of the collected pieces have some type of DCMA
# All this work is for research purposes only and will not be public

from pymongo import MongoClient, ASCENDING, DESCENDING, TEXT
import pymongo.errors
import json
import load_vars

class DB_handler():
    def __init__(self):
        self.client = MongoClient(load_vars.CONN_STRING)
        self.db = self.client[load_vars.DATABASE]
        self.paintingsDB = self.db.paintings

        self.snaps = {"_id": 0, "Artist":1, 
                      "Classification":1, "URL":1,
                      "ThumbnailURL":1, "Title":1}


    def get_all_pieces(self):
        query_res = list(self.paintingsDB.find({}, self.snaps))

        return (query_res)


    def get_paints_by_author(self, author):
        query_res = list(self.paintingsDB.find({"Artist":[author], "Classification":"Painting"}, self.snaps))

        return (query_res)

