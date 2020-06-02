# Text to Video with Voice Automatically

---

## Description


Use NLP technique and video and audio tool to transfer text to video with manually or automatically picked image and voice automatically. 

---

## Process

- First, Crawl some text from 每日頭條 or uu閱讀 or 悟空問答 and process the text through NLP. Then using goolge text2speech Api transfer text to mp3 format. 

- Second, transfer text to srt files according to the speed of mp3 file.

- Third, transfer multiple images into avi video file.

- Four, combine all files(.srt ,.avi,.mp3)

## Environment

Python3.6

## Requirements

- ### Python
see requirements.txt

- ### FFmpeg

Install and add to environment path

https://ffmpeg.org/

## Command