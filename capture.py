from pixel import *
from os import system
from sys import exit
# 1.0.0
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
Version : 1.0.0
    """

if( check_cam() == False ):
    exit()

counter = 0        # Counter for How many pictures taken
detected = 0       # Counter for How many pictures taken which not the same with base
# c = 0            # For testing the speed

while(counter < 20):
    cap(counter)
    res = get_p()
    if(res == True):
        cmd = f"mv ./test2.png ./{detected}_movement.png"
        system(cmd)
        detected+=1
    counter+=1
    if(counter== 20):
        counter = 0
    # print(c)
    # c+=1
