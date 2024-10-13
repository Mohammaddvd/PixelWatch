from PIL import Image
from sys import exit
from subprocess import PIPE, Popen
import cv2

borders = []

def get_b(w, h):
    #center = [w/2, h/2]
    #horizonal_b = [[ww, h] for ww in range(w)]
    #vertical_b  = [[w, hh] for hh in range(h)]

    sw = int(w/10)      # Width
    sh = int(h/10)      # Height
    bs = []             # All pixel positions
    
    for x in range(sh):
        bs.append([[xx, x*9] for xx in range(w)])
    for x in range(sw):
        bs.append([[sw*9, xx] for xx in range(h)])
    return bs

def compare(px, px2, bs):
    c = 0       # Number of changed pixel
    for b2 in bs:
        for b in b2:
            w = b[0]
            h = b[1]
            r, g, b = px[ w, h ]
            r2, g2, b2 = px2[ w, h ]
            #print(f"{r} | {r2}")
            if((-15 <= r-r2 <= 15) and (-15 <= b-b2 <= 15) and (-15<= g-g2 <= 15)):
                pass
            else:
                #print(f"{r} {g} {b} | {r2} {g2} {b2}")
                c+=1
    if(c > 300):        # Can change '300' #sensitive
        print(f"[+] movement detected")
        return True
    #print(bs)
    return False


def get_p():
    im = Image.open("./test.png")
    im2 = Image.open("./test2.png")
    px = im.load()
    px2 = im2.load()
    w = im.width
    h = im.height
    bs = get_b(w, h)
    #print(bs)
    return compare(px, px2, bs)

def cap(counter):
    cam_port = 0
    cam = cv2.VideoCapture(cam_port)
    if(counter == 0):
        bres, bimg = cam.read()             # Base Picture
        cv2.imwrite("./test.png", bimg)     # Writing base picture
    res, image = cam.read()                 # 2nd picture
    if(res):
        cv2.imwrite("./test2.png", image)
    
def check_cam():        # Check is camera plug in
    cmd = "vcgencmd get_camera"
    res = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE).communicate()[0].decode()
    if("detected=1" in res):
        print("[+] Camera detected")
        return True
    else:
        print("[-] Couldnt detect camera")
        return False
