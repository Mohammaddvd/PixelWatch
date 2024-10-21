from sys import exit
from subprocess import PIPE, Popen
import cv2
import threading

borders = []

def get_b(w, h):
    sw = int(w/10)      # Width
    sh = int(h/10)      # Height
    bs = []             # All pixel positions
    
    for x in range(sh):
        bs.append([[xx, x*9] for xx in range(w)])
    for x in range(sw):
        bs.append([[sw*9, xx] for xx in range(h)])
    return bs

    
def check_cam():        # Check is camera plug in
    cmd = "vcgencmd get_camera"
    res = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE).communicate()[0].decode()
    if("detected=1" in res):
        print("[+] Camera detected")
        return True
    else:
        print("[-] Couldnt detect camera")
        return False



class work:
    def __init__(self) -> None:
        self.captured = []
        self.basepic = []
        self.counter = 0
        self.changes = 0
        t_cap = threading.Thread(target=self.start_cap)
        t_chk = threading.Thread(target=self.start_chk)
        
        t_cap.start()
        t_chk.start()

        t_cap.join()
        t_chk.join()

    def start_cap(self) -> None:
        while(True):
            self.capture()
            self.counter+=1
            if(self.counter== 20):
                self.counter = 0

    def start_chk(self) -> None:
        while(True):
            if(len(self.captured) > 0):
                res = self.check()
                if(res):
                    pass # DO what
                else:
                    pass
            else:
                pass

    def capture(self) -> None:
            cam = cv2.VideoCapture(0)
            if(self.counter == 0):
                bres, self.basepic = cam.read()             # Base Picture
            res, image = cam.read()                 # 2nd picture
            self.captured.append(image)
            cam.release()

    def check(self) -> bool:        
        # Check if there are captured images
        if not self.captured:
            return False  # Exit early if there are no images

        im = self.captured.pop(0)
        
        # Ensure im has the expected dimensions
        if len(im.shape) != 3:
            print("Captured image does not have the expected 3 dimensions.")
            return False

        h, w, _ = im.shape  # Get height and width from the captured image
        c = 0  # Number of changed pixels

        bs = get_b(w, h)  # Get the border positions

        for b2 in bs:
            for b in b2:
                w_idx = b[0]
                h_idx = b[1]

                # Extract pixel values
                r, g, b = self.basepic[h_idx, w_idx]
                r2, g2, b2 = im[h_idx, w_idx]

                # Calculate differences
                r_diff = int(r) - int(r2)
                g_diff = int(g) - int(g2)
                b_diff = int(b) - int(b2)

                # Check for significant differences
                if not (-15 <= r_diff <= 15 and -15 <= g_diff <= 15 and -15 <= b_diff <= 15):
                    c += 1

        if c > 300:  # Sensitivity threshold
            print(f"[+] Movement detected")
            return True

        return False




