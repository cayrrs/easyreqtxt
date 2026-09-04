import os
import sys
import json
import re
import numpy as np
import requests
from pydantic import BaseModel
import logging

logger = logging.getLogger(__name__)


def safe_request(url):
    try:
        return requests.get(url, timeout=5)
    except requests.exceptions.RequestException as e:
        logger.error(f"Request failed: {e}")
        return None


class Config(BaseModel):
    debug: bool = False
