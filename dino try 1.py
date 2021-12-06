import pyautogui
from PIL import ImageGrab, ImageDraw
from datetime import datetime

if __name__ == "__main__":
  
     # 1st split your monitor with 2 screens, 1 with python code and other with Dino game
     # Afte press play in the code, select dino screen to activate it
    print("Click on screen window to start")   
    pyautogui.write('  ', interval=1) 
    
    scr_position = [860, 280]
    area = (scr_position[0], scr_position[1], scr_position[0] + 300, scr_position[1] + 170)

    while True:
        dino_capture = ImageGrab.grab()
        cropped_img = dino_capture.crop(area)
        cropped_img.convert('1')
        crop_cactus = cropped_img.crop((143,80,190,110))
        ptero = cropped_img.getpixel((193, 50))
        colors_cactus = crop_cactus.getcolors()

        print(" - cactus - ", cactus, " - ptero - ", ptero, ' - rect cactus - ',colors_cactus)

        if colors_cactus[0][0] <1350:
            pyautogui.keyDown('space')
            print("--------- CACTUS ---------")

        draw = ImageDraw.Draw(cropped_img)
        draw.rectangle((143,80,190,110), fill=None, outline='green', width=1)

        date_string = datetime  .now().strftime("%H-%M-%S-%f")
        date_string = 'shots/' +date_string + ".jpg"
        cropped_img.save(date_string, "JPEG")
