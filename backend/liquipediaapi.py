
import requests
import os
from pydantic import BaseModel
from datetime import datetime
LIQUIPEDIA_API_KEY = os.getenv("LIQUIPEDIA_API_KEY")


class PlacementResponse(BaseModel):
    pageid: int
    pagename: str
    
    placement: str
    prizemoney: int
    imageurl: str
    imagedarkurl: str
    opponentname: str
    opponentplayers: dict

    lastvsdata: dict

class TournamentResponse(BaseModel):
    pageid: int
    pagename: str
    name: str
    bannerurl: str
    bannerdarkurl: str
    iconurl: str
    icondarkurl: str
    startdate: datetime
    enddate: datetime
    sortdate: datetime
    prizepool: int
    participantsnumber: int
    liquipediatier: str
    format: str

    

def get_tournament_info(pageid):
    url = "https://api.liquipedia.net/api/v3/placement"
    
    params = {
        "wiki": "dota2",
        "conditions": f"[[pageid::{pageid}]]",
        "query": "pageid, pagename, imageurl, imagedarkurl, placement, prizemoney, lastvsdata, opponentname, opponentplayers",
        "order": "startdate DESC",
    }
    headers = {
        "authorization": f"Apikey {LIQUIPEDIA_API_KEY}",
        "accept": "application/json",
    }
    
    return TournamentInfoResponse(requests.get(url, params=params, headers=headers).json())

tournaments=[
    (183975, "ESL_One/Birmingham/2026"),
]