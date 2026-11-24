import cv2
import numpy as np

# TASK2：将彩色图片转换成灰度图（Python 版本）
INPUT = "input.png"
GRAY_OUT = "gray_python.png"

img = cv2.imread(INPUT)
if img is None:
    h, w = 250, 486
    img = np.zeros((h, w, 3), dtype=np.uint8)
    img[:, : w // 3] = (0, 0, 255)
    img[:, w // 3 : 2 * w // 3] = (0, 255, 0)
    img[:, 2 * w // 3 :] = (255, 0, 0)
    cv2.imwrite(INPUT, img)

# 彩色转灰度：BGR 三通道合并成单通道灰度
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite(GRAY_OUT, gray)

cv2.imshow("original", img)
cv2.imshow("gray", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
print("灰度图已保存为", GRAY_OUT)
