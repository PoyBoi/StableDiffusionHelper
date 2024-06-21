# 📸 Stable Diffusion Helper 🎨

This tool is designed to streamline the process of cropping faces from images, ensuring that you get the perfect crop every time. Whether you're working on a photo management application or simply need to process a batch of images for your next project, our tool is here to help.

## 🤓 Features

- **Automatic Face Detection**: Utilizes `dlib`'s and `openCV`'s powerful face detection to identify faces in any image.
- **Smart Cropping**: Automatically crops images to focus on the detected faces, adjusting the size and aspect ratio as needed.
- **Image Standardization**: Converts and resizes images to a uniform format and size, making it easier to work with them in your projects.
- **Batch Processing**: Process an entire folder of images in one go, saving you time and effort.
- **Error Handling**: Keeps track of images that failed to process, allowing you to easily review and handle exceptions.

## 🏃‍♂️ Getting Started

### ⚙️ Pre-requisites

Before you begin, ensure you have the following installed:
- Python 3.x
  - `Suggested` Python 3.10.11 [3.11+ discontinues `imghdr`, which is a core dependancy]
- Git

### 🚀 Installation

Check for troubleshooting here: [Troubleshooting](https://github.com/PoyBoi/StableDiffusionHelper/edit/main/README.md#%EF%B8%8F-troubleshooting)

- Download and run the `install.bat` from [releases](https://github.com/PoyBoi/StableDiffusionHelper/releases/tag/v0.1-beta)
  - Will automatically install dependancies and open the ipynb

### 🔧 Usage
- Run the `Run.bat` file (Will open the .ipynb inside a jupytner notebook on localhost[8888].
- Once Inside the editor of you choice:
  - To generate captions for the images, use the [WebUI of stable diffusion](https://github.com/AUTOMATIC1111/stable-diffusion-webui)
    - Then move the images AND captions to a folder, and that is the location you should provide for `folder_loc` inside ```Image Captioning Helper/Basic Imports```
  - Run the modules you want from ```_Helper.py```.
    - Fill out the variables inside ```Basic Image Processing/Basic Init for Image Helper``` and/or ```Image Captioning Helper/Basic Imports``` in `_Helper.py` under their respective module names (Tabs/Locations provided in this message)
  - Run the modules in an order, do not skip the order of the modules and run a lower one before a higher one, it will break.
    - You can skip any modules you do not want to run, but do it in the order of the given modules.
   
### ‼️ [Troubleshooting]:
If your `Run.bat` file does not have a `::test test` at the end of it, follow these steps:
- Delete the old repository, download and run the `install.bat` from [releases](https://github.com/PoyBoi/StableDiffusionHelper/releases/tag/v0.1-beta)

#### Or

- Open git bash in the repo location
- Run these commands:
- ```
  git add *
  git stash
  git pull
- And then run the `run.bat` file, everything should work as expected



## ✍️ Contributing

We welcome contributions! If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

Don't forget to give the project a star! ⭐

## 📝 License

Distributed under the GPL-3.0 License. See `LICENSE` for more information.

## 🫂 Acknowledgements


- [dlib](https://dlib.net/) for the amazing face detection model.
- [OpenCV](https://opencv.org) for providing the tools necessary for image processing.
- [Pillow](https://python-pillow.org/) for image manipulation.

#### 🖼️ Thank you for checking out my project !!
