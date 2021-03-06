from flask import Flask, request, render_template
from flask_cors import CORS
from jinja2.exceptions import TemplateNotFound
from flask.logging import default_handler
from pythonjsonlogger import jsonlogger
import logging
import base64
from io import BytesIO
from PIL import ImageColor, Image

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
app.config.from_object(__name__)

werkzeug_logger = logging.getLogger('werkzeug')
file_handler = logging.FileHandler("json_logs.log")
json_formatter = jsonlogger.JsonFormatter(
    '%(levelname)s %(message)s %(msecs)s')
file_handler.setFormatter(json_formatter)

werkzeug_logger.handlers.append(file_handler)
werkzeug_logger.handlers.append(default_handler)





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


@app.route('/api/black_or_white_more', methods=['POST'])
def black_or_white_more():
    img_string = request.json['image']
    im = get_pil_image_from_base64(img_string)
    white_pixels = count_pixels_color_in_image(im, 'FFFFFF')
    black_pixels = count_pixels_color_in_image(im, "000000")
    return 'Black' if black_pixels > white_pixels else 'White'


@app.route('/api/count_pixels_of_color', methods=['POST'])
def count_pixels_of_color():
    data = request.json
    img_string, color = data['image'], data['color']
    im = get_pil_image_from_base64(img_string)
    return str(count_pixels_color_in_image(im, color))


@app.route('/')
def hello():
    try:
        return render_template("index.html")
    except TemplateNotFound:
        return "You should load vue frontend"


if __name__ == '__main__':
    app.run()
