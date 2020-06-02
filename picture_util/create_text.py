from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import os


def generate_text_pic(text):
    font_path = os.path.join(os.path.dirname(__file__), 'font', 'RiiT_F.otf')
    width = len(text) * 120
    image_size = (width, 600)
    font_size = 100
    # background color
    image = Image.new('RGB', image_size, (255, 255, 255))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(font_path, font_size)
    draw.fontmode = '1'
    text_size = draw.textsize(str(text),font)
    # center
    text_position = ((image_size[0]-text_size[0])//2, (image_size[1]-text_size[1])//2)
    # font color
    draw.text(text_position, str(text), 0, font)
    image.save(str(text)+'.jpg')

if __name__ == '__main__':
    generate_text_pic("外星人真的存在嗎？")