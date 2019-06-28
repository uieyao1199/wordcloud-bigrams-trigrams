#################################################
## Author：github.com/uieyao1199
#################################################

import pandas as pd
import numpy as np
import os
import requests, zipfile, io
import re
import string
import pickle
import time
import glob
from glob import iglob
from newspaper import Article
from datetime import datetime
import pickle
import csv
from langdetect import detect
from time import ctime
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords
from nltk import word_tokenize
from nltk.util import ngrams
from wordcloud import WordCloud, STOPWORDS
import time
from PIL import Image

def wordcloud_Returner(text):
    start_time=time.time()
    text = str(text)
    stops = set(STOPWORDS)
    stops.add('None')jj

    text_wc = WordCloud(
    background_color='white',
    max_words=1000,
    stopwords=stops)
    text_wc.generate(text)

    fig = plt.figure()
    fig.set_figwidth(10)
    fig.set_figheight(15)
    plt.imshow(text_wc, interpolation='bilinear')
    plt.axis('off')
    print('--wordcloud run for % seconds--'% (time.time() - start_time))
    return fig

def bigrams_Returner(text):
    start_time=time.time()
    text = str(text)
    text = text.lower()
    text = text.split()
    stops = set(stopwords.words('english'))
    token =[]
    for i in text:
        if i in stops:
            continue
        else:
            token.append(i)
    bigrams = list(nltk.bigrams(token))
    print('--bigrams run for % seconds--'% (time.time() - start_time))
    return bigrams

def trigrams_Returner(text):
    start_time=time.time()
    text = str(text)
    text = text.lower()
    text = text.split()
    stops = set(stopwords.words('english'))
    token =[]
    for i in text:
        if i in stops:
            continue
        else:
            token.append(i)
    trigrams = list(nltk.trigrams(token))
    print('--trigrams run for % seconds--'% (time.time() - start_time))
    return trigrams

def wordcloud_mask_Returner(mask_name, text):
    start_time=time.time()
    mask = np.array(Image.open(mask_name))
    text = str(text)
    stops = set(STOPWORDS)

    text_wc = WordCloud(
    background_color='white',
    max_words=2000,
    mask=mask,
    stopwords=stops)
    text_wc.generate(text)

    fig = plt.figure()
    fig.set_figwidth(17)
    fig.set_figheight(25)
    plt.imshow(text_wc, interpolation='bilinear')
    plt.axis('off')
    fig.savefig(path_out+'wc_mask.png')
    print('--wordcloud_mask run for % seconds--'% (time.time() - start_time))
    return fig
