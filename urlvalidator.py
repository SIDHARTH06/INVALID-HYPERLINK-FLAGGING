# -*- coding: utf-8 -*-
"""UrlValidator.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1SxBET7_LCQ4LE6t0eAJoasQb7bLF-GB8
"""

import validators
from bs4 import  BeautifulSoup
import requests as req

def validate(url):
  flag=validators.url(url)
  return flag

query='http://www.nitc.ac.in/' #pull from input
  content=req.get(query).text
  soup=BeautifulSoup(content,'lxml')
  urls=soup.find_all('a',href=True)
  for url in urls:
    toggler=validate(url['href'])
    if toggler==True:
      print(url['href'])