from googleapiclient.discovery import build
import pprint
import json

API_KEY = "AIzaSyDz4DTvqWz14jv46R2N-munKFSGOARTXJQ"
CSE_KEY = "017969047916958307312:yaoancnmeqe"

def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term,
                            cx=cse_id, 
                            **kwargs
                            ).execute()
    return res['items']

def main():
    results = google_search('ta race', API_KEY, CSE_KEY, num=1)
    for result in results:
        pprint.pprint(result)

    with open('search.json', 'w') as file:
        json.dump(result, file)

if __name__ == '__main__':
    main()
