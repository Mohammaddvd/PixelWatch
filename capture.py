from pixel import *
from sys import exit

# 1.1.0
def Banner():
    """

  _      _             _____                               
 | |    (_)           / ____|                              
 | |     ___   _____ | |     __ _ _ __ ___   ___ _ __ __ _ 
 | |    | \ \ / / _ \| |    / _` | '_ ` _ \ / _ | '__/ _` |
 | |____| |\ V |  __/| |___| (_| | | | | | |  __| | | (_| |
 |______|_| \_/ \___| \_____\__,_|_| |_| |_|\___|_|  \__,_|
                  ______                                   
                 |______|                                  
Version : 1.1.0
    """

if(__name__ == "__main__"):
    if( check_cam() == False ):
        exit()
    print(Banner.__doc__)
    w = work()
else:
    exit()

