from PIL import Image, ImageDraw, ImageFont
from textwrap import fill

def create_intro(title):
    image = Image.open("./assets/template.png")
    d = ImageDraw.Draw(image)
    font = ImageFont.truetype("./main/TMSans.ttf", 45)
    text = title
    wrapped_text = fill(text, width=40)
    text_pos = (120, 925)
    text_color = (0,0,0)

    d.text(text_pos,text=wrapped_text, fill=text_color, font=font)
    image.save(f"./temp/title_page.png")
    

# create_intro("AITA for telling my sister our parents are not crossing her boundaries?")