# -*- coding: utf-8 -*-

from googleapiclient.discovery import build
import pprint
import io
import sys
import json

reload(sys)
sys.setdefaultencoding('utf8')

API_KEY = "AIzaSyDz4DTvqWz14jv46R2N-munKFSGOARTXJQ"
CSE_KEY = "017969047916958307312:yaoancnmeqe"

#NAO_IP = "127.0.0.1"
#NAO_PORT = 52867

class Search():
    """ Librairie de recherche par mot-clés via l'api Google Custom Search """
    def __init__(self):
        print("OUI")
        self.searchRaw = None # retour brut de la requête
        self.searchRes = None # resultats de la recherche

    def google_search(self, search_term, **kwargs):
        service = build("customsearch", "v1", developerKey=API_KEY)
        print(search_term)
        self.searchRaw = service.cse().list(
                                q=search_term,
                                cx=CSE_KEY,
                                #siteSearch='wikipedia.com',
                                lr='lang_fr',
                                **kwargs
                                ).execute()

        self.searchRes = self.searchRaw["items"]

        print("SEARCH DONE")
        for r in self.searchRes:
            pprint.pprint(r)

        return self.searchRes

    def toJsonFile(self, result):
        print("BEGIN FILE")
        for r in result:
            with io.open("search.json", "wb") as fdump:
                #fdump.write(unicode(json.dump(r, fdump, indent=4, ensure_ascii=False)))
                json.dump(r, fdump, indent=4, ensure_ascii=False)                
        print("JSON SAVED")
