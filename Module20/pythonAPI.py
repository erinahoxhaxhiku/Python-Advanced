# json data
# {
#   "name": "Arianita",
#   "age": "23",
#   "address": {
#     "Country": "Kosovo",
#     "City": "Prishtine",
#     "Zip Code": "10000",
#     "Street": "Rruga B"
#   },
#   "contacts":[
#     {
#       "type": "email",
#       "value": "arianita@gmail.com"
#     },
#     {
#       "type": "phone",
#       "value": "+38344123456"
#     },
#     {
#       "type": "Linkedin",
#       "value": "Arianita"
#     }
#   ]
# }

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
#tdhanat me / nuk dalin jashta file-it

def root():
    return {
        "name": "Arianita",
        "age": 23,
        "address": {
            "Country": "Kosovo",
            "City": "Prishtine",
            "Zip Code": "10000",
            "Street": "Rruga B"
        },
        "contacts": [
            {
                "type": "email",
                "value": "arianita@gmail.com"
            },
            {
                "type": "phone",
                "value": "+38344123456"
            },
            {
                "type": "LinkedIn",
                "value": "Arianita"
            }
        ]
    }











