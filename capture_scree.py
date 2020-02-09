import numpy as np
import  cv2
from PIL import ImageGrab

img = ImageGrab.grab(bbox=(100, 10, 2560, 1440)) # x, y, w, h

img.save('1.5.jpg')

img_np = np.array(img)
frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)


cv2.imshow("frame", frame)
cv2.waitKey(0)
cv2.destroyAllWindows()

