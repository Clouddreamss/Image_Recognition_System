import cv2
import numpy as np


def rgb_to_hsv(rgb_color):

    rgb_color_np = np.uint8([[rgb_color]])

    # 使用cv2.cvtColor将RGB颜色空间转换为HSV颜色空间
    hsv_color = cv2.cvtColor(rgb_color_np, cv2.COLOR_RGB2HSV)

    return hsv_color[0][0]



rgb_color = (219, 196, 155)  # 红色
hsv_color = rgb_to_hsv(rgb_color)

print(f"RGB: {rgb_color} -> HSV: {hsv_color}")