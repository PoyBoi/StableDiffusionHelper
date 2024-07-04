# <div align="center"><b>📸 Stable Diffusion Helper - GUI 🎨</b></div>

</hr>

## <div align="center"> Advanced automated image processing tool for selection, cropping, and standardization</div>

## <div align="center"> 🎉 Now with a GUI 🎉 </div>

## 🤓 Features

- **Automatic Face Detection**: Utilizes `dlib`'s and `openCV`'s powerful face detection to identify faces in any image.
- **Image Type Selection**: Select between Realistic/Anime images for better face detection.
- **Smart Cropping**: Automatically crops images to focus on the detected faces, adjusting the size and aspect ratio as needed, offering a choice between Squared or Rectangular crops.
- **Image Standardization**: Converts and resizes images to a uniform format and size, making it easier to work with them in your projects.
- **Batch Processing**: Process an entire folder of images in one go, saving you time and effort.
- **Manual Cropping**: Crop Images one at a time or all at once using the cropping tool which also gives you the option to choose resizing size.
- **Caption Editing**: Edit captions for images in a batch, allowing you to quickly update or correct captions, with an easy check-box like interface.
- **Advanced Logging Tools**: Keeps track of images that failed to process, allowing you to easily review and handle exceptions, along with time taken for the total process.

## 🏃‍♂️ Getting Started

### ⚙️ Pre-requisites

Before you begin, ensure you have the following installed:
- Python 3.x
  - `Suggested` Python 3.10.11 [3.11+ discontinues `imghdr`, which is a core dependancy]
- Git

### 🚀 Installation

- Fresh Install:
  - Download and run the `install.bat` from [releases](https://github.com/PoyBoi/StableDiffusionHelper/releases/tag/v1.0-GUI)
    - Will automatically install dependancies and launch GUI/IPYNB    

### 🔧 Let's get things running !!

- To run the GUI, simply run the `GUI.bat` file.
  - The file will prompt you if you want to install remBG with GPU support, follow the on screen instructions for the same
  - If the browser does not auto-open, a link will appear on your screen, `ctrl + right click` on it to open it on your browser
- To run the .ipynb file, run `IPYNB.bat`, more info [here](https://github.com/PoyBoi/StableDiffusionHelper/blob/main/README_ipynb.md)

- To update if other methods fail: run the `troubleshoot.bat` file
  - Before making an issue or a report, please check the [Troubleshooting]()

## 🧠 Usage
There are 3 tabs to choose from:

<p align="center">
  <img src="https://raw.githubusercontent.com/PoyBoi/StableDiffusionHelper/main/images/static/Tabs.png">
  <br>
</p>

#### 🖼️ Image Processing

<p align="center">
  <img src="https://raw.githubusercontent.com/PoyBoi/StableDiffusionHelper/main/images/static/img.png">
  <br>
</p>

1:
- Image Folder Location: Enter the name of the folder containing the images you want to process, this will be where the process creates folders inside of.

2:
- Image Crop Type: Choose between `Square` or `Rectangle` for the type of crop you want
- Image Crop Dimensions: Enter the dimensions for the crop, in a `Width, Height` format. For Sqaure, stick to 1:1, and for rectangle, stick to 3:4 or alternatively use `Manual Cropping`
- Image Size Threshold: Removes all images smaller than size `Width, Height`

3:
- Basic Processing:
  - Duplicate Check: Check for duplicate images in the folder and moves them to a separate folder inside the folder location you provided.
  - Suitabilty Check: With references to values you define below, will get top N images that match the criteria.
  - Top N: These top N images will be selected from the folder

- Advanced Processing:
  - Remove Background: Removes the background from the images using remBG, with an option to use GPU support.

4: 
- Style Select: Select between `Realistic` or `Anime` for the type of images in the dataset (Only used for Suitabilty Check and Face Auto-Crop).
- Face Crop Method: Choose between `Auto` or `Manual` for the type of face cropping you want to use.
  - Face Crop[Auto]: Automatically crops image with respect to the zoom out variable defined via slider.
    - 1: Gives HIGHLY zoomed in images
    - 2: Default, Image cropped around face
    - 2+ The higher you go, the further away the crop is from the face, and if the size exceeds the image, it will be limited by the image size, so try not to go overboard
  - Face Crop[Manual]: Manually crop the image using the cropping tool, with an option to resize the image to a specific size
    - NOTE: Cropping is the last prcess in the pipeline, after all the other processes are done, a button guiding you to the manual cropping tab will appear underneath the `Start Processing` button, named `Click to go to Manual Cropping`

5:
- Values for Crop2Face and Suitability Check:
  - Minimum Confidence: The minimum confidence level for the face detection model to consider a face
  - Minimum Size: The minimum ratio of area of the face to the total image size
  - Minimum Threshold(Image Sharpness): The minimum threshold for the image sharpness, highest value is at 100
  - Blurriness Threshold: The maximum threshold for the image blurriness, lowest value is at 100, lower the value, the more blurry the image

6:
- Check Choices: Click the button to go through the values you've entered
- Start Processing: This will start the processes in the pipelined order, along with a loading bar
  - Pipeline Order: `Image Conversion to PNG -> Duplicate Check -> Suitability Check -> Background Removal -> Face Crop[Manual/Auto] -> Image Resize`


#### 📝 Caption Editing

<p align="center">
  <img src="https://raw.githubusercontent.com/PoyBoi/StableDiffusionHelper/main/images/static/cap.png">
  <br>
</p>

1:
- Caption Folder Location: Enter the name of the folder containing the text files you want to process

2: 
- Character Name: Enter the unique name of the character you want to train your model on
- Max Count: The maximum number of captions you will see retrieved from the text files en masse
- See Most Used Words: Click the button to see the most used words in the text files, this will open up a checkbox list below the button

3: 
- Selecting the words to delete: Select the checkbox next to each word that you would like removed
- Process the files: Click this to press the changes onto the files [This is a permanant change, so be sure to check before you press, and keep a backup if you're unsure]


#### 📸 Manual Cropping

<p align="center">
  <img src="https://raw.githubusercontent.com/PoyBoi/StableDiffusionHelper/main/images/static/crop.png">
  <br>
</p>

1: 
- Ratio Value: Enter the crop box ratio in a `Height, Width` format, this will be the final size of the image
- Apply Sizes: Click this button on every change of `Ratio Value`'s
- Upload Images: Upload either a single image or bulk images
- Load Images: This will load the images selected, and if you are coming from `Image Processing`, Click this to load in the images

2:
- Cropping: Click and drag the box to crop the image, and click `Crop` to crop the image
  - Troubleshooting: If the cropping box looks incorrect, drag one corner and that should snap to the ratio that you've entered

3:
- Next Image: Clicking on this will load the next image (if any), and will save the image you've cropped to `StableDiffusionHelper/Images/Outputs/ManualCrop`

## 😖 Troubleshooting

Sometimes the GUI might crash due to unexpected reasons (has not been patched yet). Each run of this code writes a `sdh_log.txt` file in the root of this project, which contains the error logs. If you encounter an error, please open an issue with the log file attached.
- Basic Fixes: 
  - If the GUI crash takes place during "Suitability Check", try removing the file from the folder and proceed, as of now, it's a known issue.

## ✍️ Contributing

I welcome contributions! If you have a suggestion that would make this better, please fork the repo and/or create a Pull Request/Issue.

Don't forget to give the project a star! ⭐

## 📝 License

Distributed under the GPL-3.0 License. See `LICENSE` for more information.

## 🫂 Acknowledgements


- [dlib](https://dlib.net/) for the amazing face detection model.
- [OpenCV](https://opencv.org) for providing the tools necessary for image processing.
- [Pillow](https://python-pillow.org/) for image manipulation.

#### 🖼️ Thank you for checking out my project !!