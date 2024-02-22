import os
import glob
from natsort import natsorted
from moviepy.editor import ImageClip, concatenate, VideoFileClip
import shutil

def main():
  base_dir = os.path.realpath("/home/ekellbuch/vits/viper/data/ibl1_video/videos")
  cwd = os.getcwd()
  os.chdir(base_dir)
  fps = 30
  file_list = glob.glob('*.png')  # Get all the pngs in the current directory
  file_list_sorted = natsorted(file_list, reverse=False)  # Sort the images
  clips = [ImageClip(m).set_duration(1/fps) for m in file_list_sorted]

  video = concatenate(clips, method="compose")
  video.write_videofile('ibl1.mp4', fps=fps)

  clip = VideoFileClip("ibl1.mp4")
  assert clip.fps == fps
  n_frames = sum(1 for _ in clip.iter_frames())
  #assert n_frames - 1 == len(file_list_sorted) # check set duraction
  clip.close()
  shutil.mv("ibl1.mp4", "../ibl1.mp4")
  os.chdir(cwd)


if __name__ == "__main__":
  main()