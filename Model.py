import cv2
import numpy as np


def analyze_color_coverage(image_path, color_range_lower, color_range_upper):
    # 读取图像
    image = cv2.imread(image_path)

    # 将图像从BGR转换到HSV色彩空间
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # 根据颜色范围创建掩码
    mask = cv2.inRange(hsv_image, color_range_lower, color_range_upper)

    # 计算指定颜色的覆盖率
    coverage = np.sum(mask == 255) / (image.shape[0] * image.shape[1])

    # 可视化结果
    result_image = cv2.bitwise_and(image, image, mask=mask)
    cv2.namedWindow('Original Image', cv2.WINDOW_NORMAL)
    cv2.namedWindow('Color Detected Image', cv2.WINDOW_NORMAL)
    cv2.imshow('Original Image', image)
    cv2.imshow('Color Detected Image', result_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return coverage



color_range_lower = np.array([9, 34, 174])
color_range_upper = np.array([65, 90, 255])

# 调用函数
coverage = analyze_color_coverage('./TestingPic/test.jpg', color_range_lower, color_range_upper)
print(f"Color coverage: {coverage * 100}%")