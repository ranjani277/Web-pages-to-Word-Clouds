# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 11:06:23 2024

@author: user
"""

import os
os.chdir(r"D:\January\03-1-24\web scrapping\xml_single articles")

import xml.etree.ElementTree as ET

tree = ET.parse("769952.xml")
root = tree.getroot()
root = ET.tostring(root, encoding='utf8').decode('utf8')

root

import re,string,unicodedata
import nltk
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.stem import LancasterStemmer , WordNetLemmatizer

def strip_html(text):
    soup = BeautifulSoup(text,"html.parser")
    return soup.get_text()


def remove_between_square_brackets(text):
    return re.sub('\[[^]]*\]', '', text)

def denoise_text(text):
    text= strip_html(text)
    text= remove_between_square_brackets(text)
    text= re.sub(' ','',text)
    return text

para = denoise_text(root)

    