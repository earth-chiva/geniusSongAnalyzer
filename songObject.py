
##############################################################################
# songObject.py
# |- def lyricExtracter(soup) >> BeautifulSoup
# |- class songInfo
#   |- __init__ (string [url])
#       |- soup           >> BeautifulSoup
#       |- lyric          >> String
#       |- songName       >> String
#       |- bandName       >> String
#       |- producer       >> String
#       |- dateReleased   >> DateTime
##############################################################################

import numpy as np
import lxml
import re
from bs4 import BeautifulSoup
from requests import get
import datetime

def lyricExtracter(soup):
    lyricTag = str(soup.find_all("div", class_="Lyrics__Container-sc-1ynbvzw-2 jgQsqn"))[1:-1]
    return BeautifulSoup(lyricTag, 'lxml')

class songInfo(object):
    def __init__(self, urlString):
        '''
        Check until get the correct type of website into Soup (in url)
        '''
        validateSoup = 'Pls change this'
        retryCounter = 0
        while validateSoup == 'Pls change this' and retryCounter < 10:
            self.soup = BeautifulSoup(get(urlString).content, 'lxml')
            retryCounter = retryCounter + 1
            try:
                validateSoup = str(self.soup.find("h1", class_="SongHeader__Title-sc-1b7aqpg-7 jQiTNQ").get_text())
            except:
                continue
        assert(retryCounter < 10)
        self.lyric = lyricExtracter(self.soup).get_text(separator='\n').replace(', \n, \n','')
        self.songName = "Could not retrieve ..."
        self.bandName = "Could not retrieve ..."
        self.dateReleased = datetime.date(1, 1, 1)
        self.producer = "Could not retrieve ..."
        tmpString = "\0"
        try:
            self.songName = str(self.soup.find("h1", class_="SongHeader__Title-sc-1b7aqpg-7 jQiTNQ").get_text())
        except:
            pass
        try:
            self.bandName = str(self.soup.find("a", class_="Link-h3isu4-0 dpVWpH SongHeader__Artist-sc-1b7aqpg-8 DYpgM").get_text())
        except:
            pass
        try:
            '''
            Extract the content from the header part (The website is dynamic so the class changes)
            '''
            tmpString = str(self.soup.find("div", class_="HeaderMetadata__Grid-sc-1p42fnf-1 LAJX").get_text(separator='\n'))
            tmpString = tmpString.split()
            idx = 3
            self.producer = tmpString[2]
            for i in range(3, len(tmpString)):
                if tmpString[i] != 'Release':
                    self.producer = self.producer + " " + tmpString[i]
                else:
                    idx = i+2
                    break
            dateString = tmpString[idx] + " " + tmpString[idx+1] + " " + tmpString[idx+2]
            self.dateReleased = datetime.datetime.strptime(dateString, "%B %d, %Y")
        except:
            pass
    def lyricLetterCount(self):
        tmpString = self.lyric.replace(',', ' ').replace('(',' ').replace(')',' ').replace(', \n, \n','')
        tmpString = re.sub(r'\[[a-zA-Z0-9\-\s]+\]',r' ',tmpString) # Delete all [...] format
        tmpString = tmpString.upper()
        hash = [0] * 26
        for i in tmpString:
            numLetter = ord(i)-ord('A')
            if numLetter in range(0,26):
                hash[numLetter] = hash[numLetter] + 1
        return hash
    def convertToEtaoin(self):
        seqArrLetter = np.argsort(self.lyricLetterCount())
        seqLetter = ""
        for i in range(0, 26):
            seqLetter = seqLetter + chr(seqArrLetter[i] + ord('A'))
        return seqLetter