# Functionalities I have right now:
1. Captioning:
    1. Give the name/location/etc
    2. Check for same images
    3. Get most commonly used words
    4. Convert all images to PNG
    5. Resize Image to x,y
    6. Clear/Flash VRAM
    7. Replaces words with unique name
    8. Removes all variants of unique name and removes blank spaces
    9. Removes the UniqueName from the end, use for other troubleshooting also
2. Image Handling:
    1. Check for Face in image
        1. If not found, use entropy to find subject, and if not, no face
    2. Crop Image to face
        1. Use max square crop and then resize to x,y
    3. Using DLib for face crop:
        1. Making sure face is INSIDE the crop
        2. Made to crop ONLY face
        3. Crops MORE than face (BG also)
        4. Cropping W/O padding
        5. Removing black bars and images with no face
    4. Using OpenCV DNN:
        1. 3[5]
        2. Automated Image selection based on criteria
            1. Detecting sharpness of image
            2. Making sure only ONE face gets in
            3. Also checks for blurry images
            4. Removes same Images
            5. Removes background of selected images


# Optimized Workflow for Image Selection Software

## Initial Image Handling for Selection:
[x] Automated Image Selection (OpenCV DNN):
  - Remove duplicate images.
  - Detect sharpness of image.
  - Ensure only ONE face is in the image.
  - Check for blurry images.

## Cropping and Background Handling:
[x] Crop Image to Face:
  - Use DLib or OpenCV DNN for face cropping with considerations:
    - Ensure face is INSIDE the crop.
    - Crop MORE than face (include some background).
    - Crop without padding.
    - Remove black bars and images with no face.
- Remove Background of Selected Images (if required).

## Image Standardization:
[x] Convert All Images to PNG.
- Resize Image to specified dimensions (x,y).

## Captioning and Final Adjustments:
- Assign metadata (name/location/etc).
- Check for duplicate images again (if necessary).
- Get most commonly used words for tagging/categorization.
- Replace words with unique name & cleanup:
  - Remove all variants of unique name.
  - Remove blank spaces.
  - Remove the UniqueName from the end for troubleshooting.

## Post-Processing:
- Clear/Flash VRAM to free up resources.