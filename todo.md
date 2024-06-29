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

  [x] Maintain resize code inside of the cropping tool

  [x] Make it so that the images from inside folder "folder_loc" move onto "upload images from folder" and are applied to the image box via "load images"

  [x] Fix the incorrect cropping shown in the image box

    [ ] Also, fix the size of the input and output box so that they don't flare up as such (height, width)

  [ ] Find out why 240/236 were causing an issue, the issue, as i see it, is in detect_anime, inside the face detector, as far as i remember, similar issue on realistic images also