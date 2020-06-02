import re
import os
from datetime import timedelta
from datetime import datetime


def generate_srt(project_name, speed=0.225):
    """
    :param project_name: video name(Basically from text id)
    :param speed: Speak speed per character.(/sec)
    :return: Write Srt file
    """
    with open(os.path.join("text", "{}.txt".format(project_name)), 'r', encoding='utf-8') as f:
        text = f.read()
    paragraphs = re.split("[，。]",text)
    start = datetime.strptime(str(timedelta()), "%H:%M:%S")
    output_path = os.path.join("output_project", project_name, "srt")
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    with open(os.path.join(output_path, "{}.srt".format(project_name)), 'w', encoding='utf-8') as out:
        for index, para in enumerate(paragraphs):
            cost_time = len(re.sub('\W', '', para)) * speed
            start_time = datetime.strftime(start, "%H:%M:%S,%f")[:-3]
            start = start + timedelta(seconds=cost_time)
            end_time = datetime.strftime(start, "%H:%M:%S,%f")[:-3]
            body = "{}\n{} --> {}\n{}".format(index+1, start_time, end_time, para)
            out.write("{}\n\n".format(body))