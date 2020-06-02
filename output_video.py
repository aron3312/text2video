import os
from picture_util.create_text import generate_text_pic
from video_util.convert import *
from video_util.combine import *
from video_util.generate_srt import generate_srt
from video_util.add_voice import *
from video_util.txt2speech import *


if __name__ == '__main__':
    video_name = "95qa4qj"
    if not os.path.exists(os.path.join('output_project', video_name)):
        os.makedirs(os.path.join('output_project', video_name))
    txt2speech(project_name=video_name)
    generate_srt(project_name=video_name)
    pic2video(project_name=video_name)
    binaries = check()
    if None != binaries:
        if 'nt' == os.name:
            # Configure the fonts for the subtitles
            configure(binaries)
        # Merge the subtitles with the video
        merge(project_name=video_name, binaries=binaries)
    add_voice(video_name, binaries)