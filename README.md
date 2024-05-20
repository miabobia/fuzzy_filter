# fuzzy_filter

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
