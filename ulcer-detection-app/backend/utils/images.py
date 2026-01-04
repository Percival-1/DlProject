import base64
import cv2

def encode_image_to_base64(img, ext = '.png'):
    success, buffer = cv2.imencode(ext, img)
    if not success:
        raise ValueError("Image encoding failed")
    
    return (
        base64.b64encode(buffer).decode('utf-8'),
        f"image/{ext[1:]}"
    )