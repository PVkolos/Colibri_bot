from PIL import Image, ImageGrab
import pyautogui
pyautogui.FAILSAFE = False

while True:
    img2 = ImageGrab.grab((545, 340, 1378, 777))
    img2.save("screen2.jpg")
    a = [[0, 0]]
    img = Image.open('screen2.jpg')
    pix = img.load()
    x, y = img.size
    r, g, b = 0, 0, 0
    for i in range(0, x, 3):
        for j in range(0, y, 3):
            r, g, b = pix[i, j]
            if ((r in range(0, 10) and g in range(185, 190) and b in range(200, 210) and r < 50) or
                (r in range(178, 205) and g in range(200, 255) and b in range(90, 155))) and \
                    a[-1][0] != i and i - a[-1][0] >= 14:
                a.append([i, j])

    for el in a:
        if el != [0, 0]:
            pyautogui.moveTo(el[0] - 35 + 545, el[1] - 45 + 340)
            pyautogui.moveTo(el[0] + 32 + 545, el[1] + 19 + 340)
            pyautogui.moveTo(el[0] - 24 + 545, el[1] + 17 + 340)
            pyautogui.moveTo(el[0] + 20 + 545, el[1] - 50 + 340)

