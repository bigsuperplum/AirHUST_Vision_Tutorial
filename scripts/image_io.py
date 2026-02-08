# 检查OpenCV是否正确安装
import cv2
print(f"OpenCV Version: {cv2.__version__}")

# 基本的图像读取和显示
img = cv2.imread("../data/input/hesiqi.png")
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.imwrite("../data/output/hesiqi_copy.jpg", img)


img = cv2.imread("../data/input/ranjinle.jpg")
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.imwrite("../data/output/ranjinle_copy.png", img)