# fuzzy_filter
This software applies a static fuzzy filter to an image! This was inspired by this post https://twitter.com/yupd0wn/status/1791490451574579431 . This is my attempt to recreate this effect using Python's PIL library
## Image Filter Modes
Using this image as an example ![](https://github.com/mamamia96/fuzzy_filter/hello_world.png?raw=true)
There are two modes of filters that can be applied to this image.
### Mode 1 - FUZZY FOREGROUND
![](https://github.com/mamamia96/fuzzy_filter/output/hello_world_mode_1.gif?raw=true)

### Mode 2 - FUZZY BACKGROUND
![](https://github.com/mamamia96/fuzzy_filter/output/hello_world_mode_2.gif?raw=true)

## Configure Software
```txt
-- config.json
{
"FILE_NAME": "hello_world.png", -- path to the image
"GIF_FRAMES": 60,               -- how many frames long the gif is
"FRAME_DURATION": 1,            -- how many milliseconds each frame of the gif is
"MODE": 1                       -- what mode of filter the gif should use
-- MODE 1 (FUZZY FOREGROUND)
-- MODE 2 (FUZZY BACKGROUND)
}
```
## Install Requirements
```bash
$ pip install -r /path/to/requirements.txt
# skip if using fuzzy_filter.exe
```

## Usage
```bash
$ python -m fuzzy_filter.py
# or
$ fuzzy_filter.exe
```
