"""
Create a queries.csv file following
https://github.com/cvlab-columbia/viper/blob/main/data/queries.csv

The query is too slow, how
"""

import pandas as pd
import os
import glob
from natsort import natsorted


def main_images():
  import pdb; pdb.set_trace()

  cwd = os.getcwd()
  base_dir = os.path.abspath("/home/ekellbuch/vits/viper/data/ibl1_images")
  os.chdir(base_dir)

  query = "What are the x-y coordinates for each fingers in the right and left paws?"
  query = "Where are the fingers in the left paw?"
  query = "What are the coordinates of the right paw?"
  # this is going to be an issue if the mouse do asereje.
  # add with respect to the animal's body

  file_list = glob.glob('images/*.png')  # Get all the pngs in the current directory
  file_list_sorted = natsorted(file_list, reverse=False)  # Sort the images
  all_datas = []
  collected_data = pd.read_csv(os.path.abspath('../ibl1/ibl1/CollectedData.csv'), header=[0, 1, 2], index_col=0)
  xy_data = collected_data.iloc[:, :].to_numpy()
  x_data = xy_data[:, ::2]
  y_data = xy_data[:, 1::2]
  x_mean, y_mean = x_data.mean(-1), y_data.mean(-1)

  for sample_id, file in enumerate(file_list_sorted):
    answers = []
    image_name = file.rstrip('/')[-1]
    data_dict = {
    'sample_id': [sample_id],
    'query': [query],
    'image_name': [image_name],
    'answer': answers,
    'possible_answers': "",
    'query_type': '',
    }

    datas = pd.DataFrame(data_dict, index=[0])
    all_datas.append(datas)
  all_datas = pd.concat(all_datas)
  datas.to_csv('queries.csv', index=False)
  os.chdir(cwd)
  return

def main_video():
  base_dir = os.path.realpath("/home/ekellbuch/vits/viper/data/ibl1_video")
  cwd = os.getcwd()
  os.chdir(base_dir)

  query = "Are both paws on the wheel?"
  sample_id = 0
  possible_answers = 0, 1
  image_name = "ibl1.mp4"
  data_dict = {
  'sample_id': [sample_id],
  'query': [query],
  'video_name': [image_name],
  'answer': '',
  'possible_answers': "",
  'query_type': '',
  }

  datas = pd.DataFrame(data_dict, index=[0])
  datas.to_csv('queries.csv', index=False)
  os.chdir(cwd)
  return


def main_images_v0():
  base_dir = os.path.realpath("/home/ekellbuch/vits/viper/data/ibl1_images/images")
  cwd = os.getcwd()
  os.chdir(base_dir)

  file_list = glob.glob('*.png')  # Get all the pngs in the current directory
  file_list_sorted = natsorted(file_list, reverse=False)  # Sort the images

  all_datas = []
  for ii in range(len(file_list_sorted)):
    query = "Are both paws in the wheel?"
    sample_id = 0
    possible_answers = 0, 1
    data_dict = {
    'sample_id': sample_id,
    'possible_answers': possible_answers,
    'query_type': '',
    'query': query,
    'answer': '',
    'video_name': 'img{}.png'.format(ii),
    }

    datas = pd.DataFrame(data_dict)
    all_datas.append(datas)
  all_datas = pd.concat(all_datas)
  all_datas.to_csv('queries.csv', index=False)
  os.chdir(cwd)
  return
#%%

if __name__ == "__main__":
  main_images()
