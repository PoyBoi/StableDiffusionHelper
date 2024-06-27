[ ] Give an option to add BG to images w/o BG:
  1. White BG
  2. Black BG

[x] Remove Images which do not meet a minimum size requirement

[x] Add a CLI/.bat

[x] Add a method to change that cropping from square to any shape

[ ] Add a .txt that stores the data that the person puts

[ ] Add a gradio GUI

  [x] Add a GUI Based cropping tool for manual cropping of images

  [x] hard bound to the dimensions given

  [ ] Add a image parameter check tool inside gradio

  [x] Add a loading bar


<!--  What I have to do: 
resources: https://github.com/XavierJiezou/anime-face-detection
face landmark (p good): https://github.com/hysts/anime-face-detector
onnx install fixer: https://onnxruntime.ai/docs/install/#install-onnx-runtime-gpu-cuda-12x

correct TensorRT version: https://docs.nvidia.com/deeplearning/tensorrt/install-guide/index.html -> add python -m pip install --upgrade tensorrt to requirements.py
and
cudnn install https://developer.nvidia.com/rdp/cudnn-archive#a-collapse892-120

imp: cuda:11.8, onnxruntime: 1.18, cudnn: 8.9.2.26

pip install rembg[gpu] onnxruntime-gpu

Add manual cropping from gradio_2.py
Fix the location of the models to check for relative pathing

Have to add all new functionalities to the .ipynb, or discontinue it
 -->