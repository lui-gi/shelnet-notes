# Hands-On Practice
- for practice when trying to hunt down important information in CTFs

## Metadata

all images contain metadata -> also known as EXIF data
- contains information about GPS location, timestamp, etc.
- we can inject custom text into these fields without changing the visual image 

Use `exiftool`
I am using an ubuntu-based VM, so I ran
`sudo apt install libimage-exiftool-perl`

Now we download any image of choice.
Use the -Comment flag to inject custom text into image

`exiftool -Comment="i was watching one piece" image.png`

To see hidden text, we can right click the image and go to properties -> details. This MAY show up under Comments

Alt: run `exiftool image.png`

## Appending Strings




