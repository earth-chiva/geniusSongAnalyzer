import time
import datetime
import songObject
import matplotlib.pyplot as plt
import numpy as np

welcomeStr = """
*****************************************************
*    [ Welcome to genius.com analyzing project ]    *
*****************************************************
*   This program will analyze the information of    *
* each song whether it follows the ETAOIN SHRDLU in *
* the number of letters in the lyrics.              *
***************************************************** 
                                                    
                 ,----..            ,--.             
   .--.--.      /   /   \         ,--.'|  ,----..    
  /  /    '.   /   .     :    ,--,:  : | /   /   \   
 |  :  /`. /  .   /   ;.  \,`--.'`|  ' :|   :     :  
 ;  |  |--`  .   ;   /  ` ;|   :  :  | |.   |  ;. /  
 |  :  ;_    ;   |  ; \ ; |:   |   \ | :.   ; /--`   
  \  \    `. |   :  | ; | '|   : '  '; |;   | ;  __  
   `----.   \.   |  ' ' ' :'   ' ;.    ;|   : |.' .' 
   __ \  \  |'   ;  \; /  ||   | | \   |.   | '_.' : 
  /  /`--'  / \   \  ',  / '   : |  ; .''   ; : \  | 
 '--'.     /   ;   :    /  |   | '`--'  '   | '/  .' 
   `--'---'     \   \ .'   '   : |      |   :    /   
                 `---`     ;   |.'       \   \ .'    
                           '---'          `---`   
                           
*****************************************************
"""

menuStr = """
#####################################################
           __  __  ______  _   _  _    _ 
          |  \/  ||  ____|| \ | || |  | |
          | \  / || |__   |  \| || |  | |
          | |\/| ||  __|  | . ` || |  | |
          | |  | || |____ | |\  || |__| |
          |_|  |_||______||_| \_| \____/ 
#####################################################
 Option 0-3
    0 Exit The Program
    1 Retrieve Information from Website
    2 Analyze Multiple Lyrics
    3 Analyze Multiple Lyrics (by file)
"""

def warmWelcoming():
    print(welcomeStr)
    time.sleep(1)
    print("Loading program ",end="")
    for i in range(0,3):
        time.sleep(1)
        print(".",end="")
    time.sleep(1)
    print(" ( Actually, it just fancy to put on loading ) ")
    time.sleep(2)

def displayMenu():
    print(menuStr)

def songDescDisplay(song):
    print("Name : " + song.songName)
    print("Artist : " + song.bandName)
    print("Date Released : " + song.dateReleased.strftime("%d %B %Y"))
    print("Producer : " + song.producer)
    print("Lyrics : ")
    print(song.lyric)

def resultingFormat(resultCounter,resultString,lcsString):
    objects = [chr(ord('A') + i) for i in range(0,26)]
    y_pos = np.arange(len(objects))

    plt.barh(y_pos, resultCounter, align='center', alpha=0.5)
    plt.yticks(y_pos, objects)
    plt.title('Number of occurrence of each letter')

    plt.show()

    print("The order of letter shown in lyrics from the highest frequency to the lowest : " + resultString)
    print("One (from many) Longest Common Subsequences compared to ETAOIN SHRDLU : " + lcsString)
    print("The percentage of similarity compared to the ETAOIN SHRDLU : " + str(len(lcsString)*100/26) + "%")