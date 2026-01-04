import cv2
import numpy as np 
from core.model_loader import get_model
from utils.images import encode_image_to_base64
from utils.masks import extract_ulcer_stats

def run_inference(image_bytes):

    model = get_model()

    np_img = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(np_img, cv2.IMREAD_COLOR)

    result = model.predict(
        source = img,
        conf = 0.25,
        imgsz = 640,
        verbose = False
    )[0]

    output = img.copy()
    ulcer_data = []
                
    for box in result.boxes.xyxy.cpu().numpy():
        x1, y1, x2, y2 = map(int, box)
        cv2.rectangle(
            output,
            (x1, y1),
            (x2, y2),
            (0, 0, 255),
            2
        )

    if result.masks is not None:
        masks = result.masks.data.cpu().numpy()

        for m in masks:
            m = (m > 0.5).astype(np.uint8)*255
            stats = extract_ulcer_stats(m)

            for s in stats :
                cnt = s['contour']

                # Draw Contours

                cv2.drawContours(
                    output,
                    [cnt],
                    -1,
                    (255,0,0),
                    2
                )

                # Draw stats text

                x, y = cnt[0][0]

                cv2.putText(
                    output,
                    f"A:{int(s['area_px2'])} px^2 P:{int(s['perimeter'])} px",
                    (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5,
                    (0, 0, 0),
                    1
                )

                ulcer_data.append({
                    'area_px2' : float(s['area_px2']),
                    'perimeter_px' : float(s['perimeter'])
                })

    encoded_img, img_type = encode_image_to_base64(output)
    return {
        'annotated_image': encoded_img,
        'img_type': img_type,
        'ulcer_data' : ulcer_data
    }