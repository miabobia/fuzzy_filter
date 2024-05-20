from PIL import Image
import random
import copy
import json

# global config values
FILE_NAME: str
GIF_FRAMES: int
FRAME_DURATION: int
MODE: int

# pixels that stay the same
static = []
# pixels that change every frame
fuzzy = []
# frames of gif
frames = []

def get_random_grayscale_color():
    #random.seed(seed)
    c_val = random.randint(0,255)
    return (c_val, c_val, c_val)

def main():

    mode_info: str
    # == MODE 1 (FUZZY FOREGROUND) == 
    if MODE == 1:
        fuzzy_px = (255, 255, 255)
        mode_info = "FUZZY FOREGROUND"
    # == MODE 2 (FUZZY BACKGROUND) ==
    elif MODE == 2:
        mode_info = "FUZZY BACKGROUND"
        fuzzy_px = (0, 0, 0)
    else:
        print('Invalid mode! Choose:\nMODE 1 (STATIC BACKGROUND)\nMODE 2 (STATIC FOREGROUND)')
        return()

    print(f"Executing MODE {MODE}: {mode_info} ")
    
    print(f'opening {FILE_NAME}')
    im = Image.open(FILE_NAME)

    pixels = list(im.getdata())
    width, height = im.size
    pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]

    # make a frame of static pixels that never change
    static_frame = Image.new(size=(width, height), mode='RGB')

    for i in range(len(pixels)):
        for j in range(len(pixels[i])):
            if im.getpixel((j, i))[0:3] == fuzzy_px:
                #splice is here in case of alpha pixel in pixel val eg (0,0,0,0)
                fuzzy.append((j, i))
            else:
                static_frame.putpixel((j, i), get_random_grayscale_color())

    # copy static frame for every gif frame
    frames = [copy.deepcopy(static_frame) for i in range(GIF_FRAMES)]

    loading_bar_full = 0
    loading_bar_empty = 20
    print(f"{'.' * (20)} 0%")

    # draw fuzzy pixels
    for i in range(GIF_FRAMES):
        for f_px in fuzzy:
            frames[i].putpixel(f_px, get_random_grayscale_color())

        # print loading bar
        if ((i+1)/GIF_FRAMES * 100) % 25 == 0:
            loading_bar_full += 5
            print(f"{'#' * loading_bar_full}{'.' * (loading_bar_empty-loading_bar_full)} {int((i+1)/GIF_FRAMES * 100)}%")

    gif_path = f'{FILE_NAME[:len(FILE_NAME)-4]}.gif'

    print(f'SAVING FILE: {gif_path}\n')

    frames[0].save(gif_path, save_all=True, append_images=frames[1:], loop=0, duration=FRAME_DURATION, optimize=True)

if __name__ == '__main__':

    print("""
====================
= FUZZY_FILTER 1.0 =
====================

by mia_bobia\n\n        
          """)

    cfg = open('config.json')
    data = json.load(cfg)
    if data: print("config loaded")

    FILE_NAME = data['FILE_NAME']
    GIF_FRAMES = data['GIF_FRAMES']
    MODE = data['MODE']
    FRAME_DURATION = data['FRAME_DURATION']

    main()

    input('press any key to exit...')