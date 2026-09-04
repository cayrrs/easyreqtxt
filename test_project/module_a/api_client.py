import requests, PIL
import json
from bs4 import BeautifulSoup
import yaml
from dotenv import load_dotenv
import os

load_dotenv()


def fetch_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup.title.string


def load_config(path):
    with open(path) as f:
        return yaml.safe_load(f)
