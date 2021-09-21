import base64
from io import BytesIO
from PIL import ImageColor, Image


def count_pixels_color_in_image(image, hex_color: str):
    if not hex_color.startswith('#'):
        hex_color = '#' + hex_color
    color_count = 0
    rgb_color = ImageColor.getrgb(hex_color.strip())
    for pixel in image.getdata():
        if pixel[:3] == rgb_color:
            color_count += 1
    return color_count


def get_pil_image_from_base64(img: str):
    _, img_base64 = img.split(',')
    return Image.open(BytesIO(base64.b64decode(img_base64)))