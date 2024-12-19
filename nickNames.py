import requests
from bs4 import BeautifulSoup
import sqlite3
import configparser
import json

class nicknames:
    def __init__(self) -> None:

        config = configparser.ConfigParser()
        config.read("./.config")
        self.squadrons = json.loads(config.get("General", "squadrons"))


    def dataScrape(self, target: str)->str:
        r = requests.get(target)

    def dataWrite(self, data):
        pass

    def kickoff(self)->None:
        pass