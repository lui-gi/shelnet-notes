# Hands-On Practice
- for practice when trying to hunt down important information in CTFs

## Metadata

all images contain metadata -> also known as EXIF data (see [[2026-01-27 NCL Gym OSINT and Threat Intel|OSINT techniques]] for more on metadata extraction)
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

we can use a comman to append a string to the bottom of an img file
`echo "skypiea" >> image.jpg`

"skypiea" is now part of the file's binary code

To unearth the text string, we can use 
`strings image.jpg | tail -n 5`

## Low Hanging Fruit Tips

use `file` to verify the file type of everything, extensions can be misleading

`strings` + `exiftool`

`binwalk` to scan hex code for notable bytes (use [[2026-01-27 vi Editor and Regular Expressions|regular expressions]] with grep to filter results)

sometimes text can be hidden within the visual image but is not visible to the human eye, we can use an external tool to find these
- StegSolve

### Automated Scanners
`zsteg` -> find any readable text in Least Significant Bit combos
`steghide` + `stegseek`

## Packet Capture / Wireshark

File -> Export Objects -> HTTP (or FTP or SMB)
- Save All -> analyze each object individually

Follow Stream -> TCP Stream
- Identify the Headers that indicate start of image
- example: JPEG = FF D8 FF
- Save -> switch to Raw view, save as .bin, rename with correct extension