# bridge_date.py
"""

"""
from datetime import date
import logging

def get_date_path():

    today = date.today()
    # dd/mm/YY
    return today.strftime("%Y%m%d")


