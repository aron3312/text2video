import cv2
import os
import glob
import subprocess

def pic2video(project_name, size=(1920, 1080)):
    """
    :param project_name:video name(Basically from text id)
    :param size: video quality . ex:(1920,1080) means 1080p
    :return: Write avi video file from image
    """
    audio_path = os.path.join('output_project', project_name, 'voice', '{}.mp3'.format(project_name))
    args = ("ffprobe", "-show_entries", "format=duration", "-i", audio_path)
    popen = subprocess.Popen(args, stdout=subprocess.PIPE)
    popen.wait()
    output = popen.stdout.read()
    img_array = []
    for filename in glob.glob('{}/*.jpg'.format(os.path.join('output_project', project_name, 'img'))):
        img = cv2.imread(filename)
        # height, width, layers = img.shape
        img = cv2.resize(img, size, interpolation=cv2.INTER_CUBIC)
        img_array.append(img)
    # cover = cv2.imread(cover_path)
    # cover = cv2.resize(cover, size, interpolation=cv2.INTER_CUBIC)
    # cover_out = cv2.VideoWriter('temp/{}_cover.mp4'.format(video_name), cv2.VideoWriter_fourcc(*'MP4V'), 10, size)
    video_path = os.path.join('output_project', project_name, 'temp')
    if not os.path.exists(video_path):
        os.makedirs(video_path)
    out = cv2.VideoWriter(os.path.join(video_path, '{}.avi'.format(project_name)), cv2.VideoWriter_fourcc('m','p','4','v'), 10, size)
    # for i in range(20):
    #     cover_out.write(cover)
    # cover_out.release()
    max_index = int(int(float(output.decode('utf-8').split('\r\n')[1].split('=')[1])) * 10 / len(img_array))
    for i in range(len(img_array)):
        j = 0
        while j < max_index:
            out.write(img_array[i])
            j += 1
    out.release()