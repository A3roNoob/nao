# -*- coding: utf-8 -*-

from naoqi import ALProxy
from naoqi import ALBroker
from naoqi import ALModule

from googleapiclient.discovery import build
import pprint
import json

API_KEY = "AIzaSyDz4DTvqWz14jv46R2N-munKFSGOARTXJQ"
CSE_KEY = "017969047916958307312:yaoancnmeqe"

NAO_IP = "127.0.0.1"
NAO_PORT = 52867

Search = None
memory = None

class SearchModule(ALModule):
    """ Module de recherche par termes déclenché par la voix """

    def __init__(self, name, searchterm):

        # chargement du broker
        ALModule.__init__(self, name)

        # module speech reco pour plus tard
        self.listenForOrder = ALModule("ALSpeechRecognition")
        self.listenForOrder.setLanguage("French")
        self.listenForOrder.setVocabulary(triggerTerm, True)
        self.listenForOrder.subscribe("SpeechReco")

        global memory
        memory = ALProxy("ALMemory")
        memory.subscribeToEvent("WordRecognized", "Search", "onSearchOrdered")

        pprint("OUI")

    def onSearchOrdered(self, *_args):
        """ appelé a chaque terme reconnu """

        raw = self.google_search('ok', API_KEY, CSE_KEY, num=1)

        result = json.loads(raw)

        # log dans la console pour debug
        for r in result:
            pprint.pprint(r)

        # log dans json because
        with open('search.json', 'w') as file:
            json.dump(r, file)


    def google_search(search_term, api_key, cse_id, **kwargs):
        """ execute une recherche google custom search """

        service = build("customsearch", "v1", developerKey=api_key)
        res = service.cse().list(q=search_term,
                                cx=cse_id,
                                filter=1, 
                                **kwargs
                                ).execute()
        return res['items']

def main():
    """ entry point """

    broker = ALBroker("pythonBroker","127.0.0.1",52000,NAO_IP,NAO_PORT)
    global Search
    Search = SearchModule("Search","oui")

if __name__ == "__main__":
     main()