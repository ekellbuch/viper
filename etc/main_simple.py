import torch
print(torch.cuda.is_available())
import torch
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

import os
os.environ["PATH"] += os.pathsep + "/usr/local/cuda/bin"
os.environ["LD_LIBRARY_PATH"] = "/usr/local/cuda/lib64"

#%%

from main_simple_lib import *


#%%
im_path = "/home/ekellbuch/vits/viper/data/ibl1/ibl1/labeled-data/ibl1/img1.png"
#im = load_image('https://wondermamas.com/wp-content/uploads/2020/04/IMG_8950-min-1024x1024.jpg')
im = load_image(im_path)
query = 'how many times are both paws in the wheel?'

#%%
show_single_image(im)
#%%
code = get_code(query)
from vision_processes import forward, finish_all_consumers  # This import loads all the models. May take a while
from vision_processes import consumers

#%%
execute_code(code, im, show_intermediate_steps=True)

#%% #codex was only giving me an error because of openaicreadits

#model_name ="xvlm"
model_name = "codex"
args = {}
if model_name == "codex":
  #raise NotImplementedError("Codex is not supported yet")
  args["prompt"] = query
  args["input_type"] = "image"
elif model_name == "xvlm":
  args["text"] = query
  args["image"] = im
elif model_name == "gpt-3.5-turbo":
  args["text"] = query
  args["image"] = im

out = consumers[model_name](**args)
print(out)
#%%
import openai
response = openai.Completion.create(
  model="gpt-3.5-turbo",
  prompt=query,
)
#%%
code = out
#code = forward('codex', prompt=query, input_type="image")
#%%
if config.codex.model not in ('gpt-3.5-turbo', 'gpt-4'):
  code = f'def execute_command(image, my_fig, time_wait_between_lines, syntax):' + code  # chat models give execute_command due to system behaviour
code_for_syntax = code.replace("(image, my_fig, time_wait_between_lines, syntax)", "(image)")
syntax_1 = Syntax(code_for_syntax, "python", theme="monokai", line_numbers=True, start_line=0)
console.print(syntax_1)
code = ast.unparse(ast.parse(code))
code_for_syntax_2 = code.replace("(image, my_fig, time_wait_between_lines, syntax)", "(image)")
syntax_2 = Syntax(code_for_syntax_2, "python", theme="monokai", line_numbers=True, start_line=0)

#%%

import pandas as pd

sample_id =0
possible_answers=0,1
image_name = ""
data_dict = {
'sample_id': sample_id,
'possible_answers': possible_answers,
'query_type': '',
'query': '',
'answer': '',
'video_name': image_name,
}

datas = pd.DataFrame(data_dict)

data_dir= '/home/ekellbuch/vits/viper/data/ibl1/ibl1/labeled-data/ibl1'
#CONFIG_NAMES=your_config_name python main_batch.py
datas.to_csv('queries.csv', index=False)
#%%