from PIL import Image, ImageDraw, ImageFont


def task3_1():
    #print("Hello world!")
    
    width = 400
    height = 400
    
    img  = Image.new(mode = "RGB", size = (width, height), color = (209, 123, 193))
    
    draw = ImageDraw.Draw(img)
    draw.rectangle([0, 0, 200, 200])
    draw.rectangle([200, 0, 400-1, 200])
    draw.rectangle([0, 200, 200, 400-1])
    draw.rectangle([200, 200, 400-1, 400-1])

    font = ImageFont.truetype("cambria.ttc", 25)
    draw.text((10, 50), "Входи", font=font)
    draw.text((10, 100), "Матриця інверторів", font=font, fill="red")
    draw.text((10, 130), "A ⊕ B", font=font, fill="cyan")
    

    img.show()
    img.save("image.jpg", "JPEG")

if __name__ == '__main__':
    task3_1()
