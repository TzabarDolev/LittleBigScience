import os
import moviepy.video.io.ImageSequenceClip
from natsort import natsorted

strings = ['webcam', 'dense']
fpss = [12, 20]
fps_ind = 0
for string in strings:
    image_folder = '{}'.format(string)
    sorted_list = []
    image_files = os.listdir(image_folder)
    sorted_image_files = natsorted(image_files)

    for file in range(len(image_files)):
        sorted_list.append(image_folder + '/' + sorted_image_files[file])

    clip = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(sorted_list, fps=fpss[fps_ind])
    clip.write_videofile('videos/{}.mp4'.format(string))
    fps_ind += 1

