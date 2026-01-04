import cv2
import numpy as np

def extract_ulcer_stats(mask):
    contours, _ = cv2.findContours(
        mask,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_NONE,
    )

    stats = []

    for cnt in contours:
        area = cv2.contourArea(cnt)
        perimeter = cv2.arcLength(cnt, closed = True)

        stats.append({
            'contour' : cnt,
            'area_px2' : float(area),
            'perimeter' : float(perimeter)
        })

    return stats