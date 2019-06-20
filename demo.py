
import json
from elasticsearch import Elasticsearch
import requests


esConn = Elasticsearch(json.loads('["http://??????????"]'))


body = { "_source":['meta'],
             "query":
                    {
                        "match": {"search_id": "?????????"}
                    }
        }

res = esConn.search(index="????????????",body=body)

# print(" doc id is" , res['hits']['hits'][0]['_id'])

docId = res['hits']['hits'][0]['_id']


print("the docId from es is ", docId)
# passing the docID to the api

api = "http://???????????????????????????" + str(docId)

access_token ="????????????????????????????????"

head = {'access_token':  access_token}

resp = requests.get(api, headers= head)

op = resp.json()
# print(op)

nId = op['data']['iconData'][0]['nodeId']

nText = op['data']['iconData'][0]['nodeText']

print("the node id is " , nId)
print()
print("The name is ", nText)

# Replace ??????????????????  with your extries
