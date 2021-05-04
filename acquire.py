# environment setup

from requests import get
from bs4 import BeautifulSoup
import os

import requests
import bs4

import pandas as pd

###################################################################################################################

def process_codeup_blog_article(url):
    '''
    This function will take a url from a Codeup blog and return the title and the article content
    in the form of a dictionary
    '''
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    # Codeup only accepts requests with headers 
    
    url_response = requests.get(url, headers=headers)
    # make formal request from website
    
    url_soup = bs4.BeautifulSoup(url_response.text)
    # create soup from response
    
    title = url_soup.find('title').text
    # find the title of the article in the soup
    
    article_div = url_soup.select('.jupiterx-post-content.clearfix')[0]
    # find the content of the article in the soup
    
    paragraphs = article_div.select('p')
    # find individual paragraphs, if desired 
    
    ## return a dictionary with the requested content
    return {
        "title": title,
        "content": article_div.text,
    }

###################################################################################################################

