import os
import sys
from pydub import AudioSegment


def add_voice(project_name, binaries):
    if not os.path.exists("output"):
        os.makedirs("output")
    video_path = os.path.join("temp", "{}_srt.mp4".format(project_name))
    audio_path = os.path.join("voice", "{}.mp3".format(project_name))
    output_path = os.path.join("output", "{}.mp4".format(project_name))
    command = binaries + 'ffmpeg -i %s -i %s -c:v copy -c:a aac %s'
    os.system(command % (video_path, audio_path, output_path))