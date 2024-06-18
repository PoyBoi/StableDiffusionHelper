# 📸 Stable Diffusion Helper 🎨

This tool is designed to streamline the process of cropping faces from images, ensuring that you get the perfect crop every time. Whether you're working on a photo management application or simply need to process a batch of images for your next project, our tool is here to help.

## Features

- **Automatic Face Detection**: Utilizes `dlib`'s and `openCV`'s powerful face detection to identify faces in any image.
- **Smart Cropping**: Automatically crops images to focus on the detected faces, adjusting the size and aspect ratio as needed.
- **Image Standardization**: Converts and resizes images to a uniform format and size, making it easier to work with them in your projects.
- **Batch Processing**: Process an entire folder of images in one go, saving you time and effort.
- **Error Handling**: Keeps track of images that failed to process, allowing you to easily review and handle exceptions.

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.x
  - `Suggested` Python 3.10.11

### Installation

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/PoyBoi/StableDiffusionHelper.git
   ```
2. Navigate to the cloned repository:
   ```
   cd StableDiffusionHelper
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

### Usage

- Run the modules you want from ```_Helper.py```.
  - Fill out the variables inside ```Basic Image Processing/Basic Init for Image Helper``` and/or ```Image Captioning Helper/Basic Imports``` in `_Helper.py` under their respective module names (Tabs/Locations provided in this message)
- Run the modules in an order, do not skip the order of the modules and run a lower one before a higher one, it will break.
  - You can skip any modules you do not want to run, but do it in the order of the given modules.

## Contributing

We welcome contributions! If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

Don't forget to give the project a star! ⭐

## License

Distributed under the GPL-3.0 License. See `LICENSE` for more information.

## Acknowledgements


- [dlib](https://dlib.net/) for the amazing face detection model.
- [OpenCV](https://opencv.org) for providing the tools necessary for image processing.
- [Pillow](https://python-pillow.org/) for image manipulation.

Thank you for checking out our project! We hope it helps you with your image processing needs. 🚀