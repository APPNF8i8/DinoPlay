import pyautogui
from PIL import ImageGrab, ImageDraw
from datetime import datetime

if __name__ == "__main__":

    # 1st split your monitor with 2 screens, 1 with python code and other with Dino game
    # After press play in the code, select dino screen to activate it
    print("Click on screen window to start")

    scr_position = [845, 280]
    area = (scr_position[0], scr_position[1], scr_position[0] + 300, scr_position[1] + 170)

    while True:
        dino_capture = ImageGrab.grab()
        cropped_img = dino_capture.crop(area)
        cropped_img.convert('1')
        crop_cactus = cropped_img.crop((158, 80, 215, 110))
        crop_passed = cropped_img.crop((5, 80, 18, 110))
        crop_jump = cropped_img.crop((15, 112, 25 , 119 ))
        colors_cactus = crop_cactus.getcolors()
        colors_passed = crop_passed.getcolors()
        collors_jump = crop_jump.getcolors()

        print(datetime.now().strftime("%S-%f"), "-  passed - ",colors_passed[0][0], ' - rect cactus - ', colors_cactus, ' - jump - ',collors_jump[0])

        if colors_cactus[0][0] < 1700:
            pyautogui.keyDown('space')
            print("------- CACTUS -------")
        if colors_passed[0][0] < 380 or  (collors_jump[0][0] <60 and collors_jump[0][0] >7):
            pyautogui.keyDown('down')
            pyautogui.keyUp('down')
