import os
import cv2
import numpy as np

import imagehash
from PIL import Image, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

from rembg import remove
import imghdr
import dlib

from tqdm import tqdm

import io
import time
import gradio as gr
from shutil import move
import io
from IPython.display import clear_output

from tqdm import tqdm

import re
import pandas as pd
from collections import Counter

def delete_iccfile(image_path):
    img = Image.open(image_path)
    img.info.pop('icc_profile', None)
    img.save(image_path)
    img.close()

def convert_images_to_png(source_folder, progress=gr.Progress()):
    progress(0, desc="Starting Image Conversion to .PNG ...")
    time.sleep(1)
    image_count, count = 0, 0
    image_extensions = ['.jpg', '.jpeg', '.bmp', '.gif', '.tiff', '.webp', '.png']

    # LOGGING
    log_file = "sdh_log.txt"

    with open(log_file, "r") as g:
        textb4 = g.read()

    with open(log_file, "w") as f:
        f.write(textb4)
        f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')}, Process Name: Conversion to PNG\n")
        f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')}, Current File: None\n") 
    # /LOGGING

    try:
        for filename in os.listdir(source_folder):
            if any(filename.lower().endswith(ext) for ext in image_extensions):
                image_count += 1

        for filename in os.listdir(source_folder):
            
            with open(log_file, "w") as f:
                f.write(textb4)
                f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')}, Process Name: Conversion to PNG\n")
                f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')}, Current File: {filename}\n") 

            if filename.lower().endswith(('.jpg', '.jpeg', '.bmp', '.gif', '.tiff', '.webp')):
                file_path = os.path.join(source_folder, filename)
                with Image.open(file_path) as img:
                    img.info.pop('icc_profile', None)
                    new_filename = os.path.splitext(filename)[0] + '.png'
                    new_file_path = os.path.join(source_folder, new_filename)
                    try:
                        img.info.pop('icc_profile', None)
                        img.save(new_file_path, 'PNG')
                        # os.remove(file_path)
                    except:
                        img.info.pop('icc_profile', None)
                        img.convert('RGB').save(new_file_path, "PNG", optimize=True)
                os.remove(file_path)
                count += 1
                progress(count / image_count, desc=f"Converting {filename} to .png")
        
        with open(log_file, "w") as f:
                f.write(textb4)
                f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')}, Process Name: Conversion to PNG\n")
                f.write(f"===================== Process  Finished =====================\n\n") 

        return "❣️ All Images Converted to .PNG ❣️"
    except Exception as e:

        with open(log_file, "w") as f:
                f.write(textb4)
                f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')}, Process Name: Conversion to PNG\n")
                f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')}, Ran into Error -> {e}\n") 

        return "Error: {}".format(e)

def remove_black_bars(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        largest_contour = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(largest_contour)
        cropped_image = image[y:y+h, x:x+w]
        return cropped_image
    return image

def process_images(folder_path, x, y, progress=gr.Progress()):

    # LOGGING
    log_file = "sdh_log.txt"

    with open(log_file, "r") as g:
        textb4 = g.read()

    with open(log_file, "w") as f:
        f.write(textb4)
        f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')}, Process Name: Duplicate Check\n")
        f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')}, Current File: None\n") 
    # /LOGGING

    progress(0, desc="Starting Duplicate Image Check ...")
    time.sleep(1)

    duplicate_images_folder = os.path.join(folder_path, "Duplicate_Images")
    if not os.path.exists(duplicate_images_folder):
        os.makedirs(duplicate_images_folder)

    small_images_folder = os.path.join(folder_path, "Small_Images")
    if not os.path.exists(small_images_folder):
        os.makedirs(small_images_folder)
    
    image_hashes = {}
    files = [f for f in os.listdir(folder_path) if f.endswith(('.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.webp'))]
    image_count, count = len(files), 0
    
    # print(type(x), type(y))

    for filename in files:
        
        # print("Inside", count)
        with open(log_file, "w") as f:
            f.write(textb4)
            f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')}, Process Name: Duplicate Check\n")
            f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')}, Current File: {filename}\n") 

        file_path = os.path.join(folder_path, filename)
        # delete_iccfile(file_path)
        # img.info.pop('icc_profile', None)
        delete_iccfile(file_path)
        image = cv2.imread(file_path)
        if image is None:
            continue
        
        image_no_black_bars = remove_black_bars(image)
        
        pil_image = Image.fromarray(cv2.cvtColor(image_no_black_bars, cv2.COLOR_BGR2RGB))
        h,w = pil_image.size
        # print(filename, "\n",h*w, x*y)            
        
        hash = str(imagehash.average_hash(pil_image))
        
        # Check for duplicates
        if hash in image_hashes:
            # print(f"Duplicate found: {filename} is a duplicate of {image_hashes[hash]}")
            os.rename(file_path, os.path.join(duplicate_images_folder, filename))
        else:
            image_hashes[hash] = filename
            if h*w < x*y:
                os.rename(file_path, os.path.join(small_images_folder, filename))
        
        count += 1
        progress(count / image_count, desc=f"Checking for Duplicates, on: {filename}")
        
        # return "❣️ All Images Converted to .PNG ❣️"
        with open(log_file, "w") as f:
            f.write(textb4)
            f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')}, Process Name: Duplicate Check\n")
            f.write(f"===================== Process  Finished =====================\n\n") 
    
    if len([i for i in os.listdir(duplicate_images_folder)]) == 0:
        os.rmdir(duplicate_images_folder)

# net = cv2.dnn.readNetFromTensorflow(modelFile, configFile)

def calculate_image_sharpness(image):
    
    """
    Calculate the sharpness of an image using the variance of the Laplacian
    """
    
    if image is None or image.size == 0:
        return 0
    return cv2.Laplacian(image, cv2.CV_64F).var()

def is_image_blurry(image, blur_threshold):
    
    """
    Check if an image is blurry using the variance of the Laplacian method.
    """
    
    variance_of_laplacian = cv2.Laplacian(image, cv2.CV_64F).var()
    return variance_of_laplacian < blur_threshold

def detect_faces_and_evaluate(image, min_confidence, min_size, min_sharpness, blur_threshold, net):
    
    if image is None or image.size == 0:
        return []
    if is_image_blurry(image, blur_threshold):
        return []
    (h, w) = image.shape[:2]
    blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 1.0, (300, 300), (104.0, 177.0, 123.0))
    net.setInput(blob)
    detections = net.forward()
    faces_detected = []
    for i in range(0, detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > min_confidence:
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")
            startX, startY, endX, endY = max(0, startX), max(0, startY), min(w, endX), min(h, endY)
            if startX >= endX or startY >= endY:
                continue
            face_region = image[startY:endY, startX:endX]
            if face_region.size == 0:
                continue
            face_size = (endX - startX) * (endY - startY)
            face_sharpness = calculate_image_sharpness(face_region)
            if face_size > min_size and face_sharpness > min_sharpness:
                faces_detected.append((confidence, face_size, face_sharpness))
    return faces_detected

def detect_anime(img, min_confidence, min_size, min_sharpness, blur_threshold, mode, face_detector):

    # PORTED CODE FROM DFAE (ABOVE)
    if img is None or img.size == 0:
        return []
    if is_image_blurry(img, blur_threshold):
        return []
    
    # END

    # print("in_1")
    try:
        faces = face_detector(img)
    except Exception as e:
        faces = []
    
    # print("in_2")
    faces_detected = []
    face_crd = []
    if len(faces) > 0:
        for rect in faces:
            x_start = rect.left()
            x_end = rect.right()
            y_start = rect.top()
            y_end = rect.bottom()
            face_width = x_end - x_start
            face_height = y_end - y_start
            # print("in_3")
            if abs(face_width - face_height) > 3:
                continue
            face = img[y_start:y_end, x_start:x_end]
            face_crd = [x_start, y_start, face_width, face_height]
            # cv2.rectangle(image, (x_start, y_start), (x_end, y_end), (0, 0, 255), thickness=10)
        if mode == "select":
            face_sharpness = calculate_image_sharpness(face)
            face_size = face_width*face_height
            if face_size > min_size and face_sharpness > min_sharpness:
                faces_detected.append((face_size, face_sharpness))
    else:
        None

    # print("in_4")
    if mode == "crop":
        return face_crd
    if mode == "select":
        return faces_detected

def select_best_images(
        folder_path: str,
        face_type: str,
        min_confidence: float = 0.9,
        min_size: float = 0.009,
        min_sharpness: float = 100,
        blur_threshold: float = 100,
        top_n: int = 0,
        progress=gr.Progress()
):
    try:
        # LOGGING
        log_file = "sdh_log.txt"

        with open(log_file, "r") as g:
            textb4 = g.read()

        with open(log_file, "w") as f:
            f.write(textb4)
            f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')}, Process Name: Image Selection\n")
            f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')}, Current File: None\n") 
        # /LOGGING

        current_folder = os.getcwd()

        modelFile = os.path.join(current_folder, "models", "opencv_face_detector_uint8.pb")
        configFile = os.path.join(current_folder, "models", "opencv_face_detector.pbtxt")

        modelFile_x = os.path.join(current_folder, "models", "detector_face.svm")

        face_detector = dlib.simple_object_detector(modelFile_x)

        if os.path.exists(modelFile) != True or os.path.exists(configFile) != True:
            with open(log_file, "a") as f:  # Open in append mode to add to the log file
                f.write("ERROR: KEY FILES FOR RUNNING THIS MODEL NOT FOUND, PLEASE FIND THEM AND INSTALL THEM\n")
        else:
            net = cv2.dnn.readNetFromTensorflow(modelFile, configFile)
            selected_images_folder = os.path.join(folder_path, "SelectedImages")
            if not os.path.exists(selected_images_folder):
                os.makedirs(selected_images_folder)

            image_ratings = []  # List to store ratings and file paths

            files = [f for f in os.listdir(folder_path) if f.endswith(('.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.webp'))]
            progress(0, desc="Starting Image Selection ...")
            time.sleep(1)
            image_count, count = len(files), 0
            # print(2.1)
            for filename in files:
                
                # LOGGING
                with open(log_file, "w") as f:
                    f.write(textb4)
                    f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')}, Process Name: Image Selection\n")
                    f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')}, Current File: {filename}\n") 
                # /LOGGING

                file_path = os.path.join(folder_path, filename)
                delete_iccfile(file_path)  # Assuming this is a defined function
                image = cv2.imread(file_path)
                if image is None:
                    continue
                # print(2.2, filename)
                image_no_black_bars = remove_black_bars(image)  # Assuming this is a defined function

                with open(log_file, "a") as f:
                    f.write(f"Processing image: {filename} - {time.strftime('%Y-%m-%d %H:%M:%S')}\n")

                try:
                    if face_type == "Realistic":
                        faces_detected = detect_faces_and_evaluate(
                            image_no_black_bars,
                            min_confidence,
                            min_size * image_no_black_bars.size,
                            min_sharpness,
                            blur_threshold,
                            net
                        )
                    elif face_type == "Anime-like":
                        faces_detected = detect_anime(
                            image_no_black_bars,
                            min_confidence,
                            min_size * image_no_black_bars.size,
                            min_sharpness,
                            blur_threshold,
                            "select",
                            face_detector
                        )
                except Exception as e:
                    with open(log_file, "a") as f:
                        f.write(f"Error during face detection: {e} - {time.strftime('%Y-%m-%d %H:%M:%S')}\n")

                if faces_detected:
                    rating = sum([face[0] + face[1] for face in faces_detected])
                    image_ratings.append((rating, file_path))
                count += 1
                progress(count / image_count, desc=f"Checking Images for Suitability, on: {filename}")
            # print(2.5)
            # Sort images based on ratings
            if top_n == 0:
                top_n = len(files)
            
            top_images = image_ratings[:top_n]  

            # Sort the top_images based on ratings
            top_images = sorted(top_images, key=lambda x: x[0], reverse=True) 
            # print(2.6)

            with open(log_file, "w") as f:
                    f.write(textb4)
                    f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')}, Process Name: Image Selection\n")
                    f.write(f"===================== Process  Finished =====================\n\n") 

            for _, top_image_path in top_images:
                filename = os.path.basename(top_image_path)
                move(top_image_path, os.path.join(selected_images_folder, filename))  # Assuming this is a defined function

            return selected_images_folder
    except Exception as e:
        with open(log_file, "a") as f:
            f.write(f"Ran into an issue: {e} - {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        print("Ran into an issue: ", e)

def remove_background_from_images(input_folder, o_p, progress = gr.Progress()):
    output_folder = os.path.join(input_folder, o_p)
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    progress(0, desc="Starting Background Removal ...")
    time.sleep(1)
    image_count, count = len(image_files), 0
    # print(input_folder, image_count, count)
    # LOGGING
    log_file = "sdh_log.txt"

    with open(log_file, "r") as g:
        textb4 = g.read()

    with open(log_file, "w") as f:
        f.write(textb4)
        f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')}, Process Name: Background Removal\n")
        f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')}, Current File: None\n") 
    # /LOGGING
    
    for filename in image_files:
        
        with open(log_file, "w") as f:
            f.write(textb4)
            f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')}, Process Name: Background Removal\n")
            f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')}, Current File: {filename}\n") 

        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        with open(input_path, 'rb') as input_file:
            input_image = input_file.read()

            output_image = remove(input_image)

            output_image = Image.open(io.BytesIO(output_image))
            output_image.save(output_path)
        
        count += 1
        progress(count / image_count, desc=f"Removing Image Background, on: {filename}")
        with open(log_file, "w") as f:
            f.write(textb4)
            f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')}, Process Name: Background Removal\n")
            f.write(f"===================== Process  Finished =====================\n\n") 
        
    return output_folder

def faceCrop(folder_dir, failed_img, face_failed, fName, img, imp=1, x=512, y=512, face_type = "Realistic", face_detector = "None"):
    
    # current_folder = os.getcwd()
    # modelFile = os.path.join(current_folder, "models", "detector_face.svm")

    # face_detector = dlib.simple_object_detector(modelFile)
    detector = dlib.get_frontal_face_detector()

    _, ext = os.path.splitext(fName)

    # print(os.path.join(folder_dir, fNameOg))

    fName = fName.split(".")[0]
    if ext.lower() not in ['.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.webp']:
        print(f"Unsupported image format: {ext}")
        failed_img.append(fName)
        return
    
    # print("HIIIEEE")
    # print(f"\n {face_type}")
    if face_type == "Realistic":
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        oh, ow = len(gray), len(gray[0])
        faces = detector(gray)

    else:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        oh, ow = len(gray), len(gray[0])
        faces = face_detector(img)
        

    if len(faces) == 0:
        face_failed.append(fName)
    else:
        # print("1.0 in")
        if face_type == "Anime-like":
            ae = detect_anime(img, 0.7, 0.009, 100, 100, "crop", face_detector)
            fx, fy, fw, fh = ae[0], ae[1], ae[2], ae[3]
        elif face_type == "Realistic":
            areas = [face.width() * face.height() for face in faces]
            max_area_index = np.argmax(areas)
            fx, fy, fw, fh = faces[max_area_index].left(), faces[max_area_index].top(), faces[max_area_index].width(), faces[max_area_index].height()
            # print(f"1.5 in {fx, fy, fw, fh}")

        # print("2.0 in")
        fx, fy, fw, fh = max(0, fx), max(0, fy), max(0, fw), max(0, fh)
        # Calculate desired dimensions for rectangular crop (3:4 aspect ratio)
        h = fh
        w = fh

        cx, cy = fx + fw//2, fy + fh//2

        # print(0, ow, oh)
        # print(1, fx, fy, "\n", fw, fh, "\n", h, w)

        # Apply zoom out factor
        w = int(w * imp)
        h = int(h * imp)
        # print(2, w, h)

        # print(2.2, "{}/2, {}+{}/2".format(fx, oh, fy))
        fx, fy = fx//imp, fy//imp
        # print(2.5, fx, fy)

        mid_x = (cx-fx)*2
        mid_y = mid_x
        # print(3, mid_x, mid_y)

        if fy+mid_y > oh:
            # print(1, "{} + {} > {}".format(fy, mid_y, oh))
            mid_y = oh-fy
            mid_x = mid_y
            # print(1.5, mid_x, mid_y)
        if fx+mid_x > ow:
            # print(2, "{} + {} > {}".format(fx, mid_x, ow))
            mid_x = ow-fx
            mid_y = mid_x
            # print(2.5, mid_x, mid_y)

        # print("3.0 in")
        # Crop the rectangular region
        cropped = img[fy:fy+mid_y, fx:fx+mid_x]

        # cropped = cv2.rectangle(img, (fx, fy), (fx+fw, fy+fh), (0, 255, 0), 2)

        # Convert BGR to RGB
        # print(f"4.0 in \n{cropped}")
        cropped_rgb = cv2.cvtColor(cropped, cv2.COLOR_BGR2RGB)

        # Resize the cropped image to the specified dimensions
        # print(f"5.0 final {cropped_rgb}")
        cropped_resized = cv2.resize(cropped, (x, y))

        # Save the image in RGB format
        cv2.imwrite(os.path.join(folder_dir, fName + '_rectangular.png'), cropped_resized)

        # print("6.0 done")
        return cropped_rgb

def main_call(folder_path, x=512, y=512, imp = 1, ratio_select = "Square", face_type = "Realistic", progress = gr.Progress()):
    
    failed_img = []
    face_failed = []

    resized_folder_path = os.path.join(folder_path, "Cropped_Images")

    current_folder = os.getcwd()
    modelFile_x = os.path.join(current_folder, "models", "detector_face.svm")

    face_detector = dlib.simple_object_detector(modelFile_x)

    # LOGGING
    log_file = "sdh_log.txt"

    with open(log_file, "r") as g:
        textb4 = g.read()
        g.close()

    with open(log_file, "w") as f:
        f.write(textb4)
        f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')}, Process Name: Automatic Cropping\n")
        f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')}, Current File: None\n") 
        f.close()
    # /LOGGING
    
    if not os.path.exists(resized_folder_path):
        print(r"Made /resized folder")
        os.makedirs(resized_folder_path)

    if os.path.isdir(folder_path):
        print("Valid Folder Location")
        files = os.listdir(folder_path)
        files_img = [i for i in files if not i.endswith('.txt') and not os.path.isdir(os.path.join(folder_path, i))]

        progress(0, desc="Starting Face Cropping ...")
        time.sleep(1)
        image_count, count = len(files_img), 0
        print("Number of files: ", len(files_img))

        itr = 0
        for i in files_img:
            # print(i)
            itr += 1
            file_loc = os.path.join(folder_path, i)
            if os.path.isfile(file_loc) and imghdr.what(file_loc):
                # delete_iccfile(file_loc)
                img = cv2.imread(file_loc)
                if img is None:
                    print(f"Failed to load image: {i}:", "Cause: Empty !")
                    failed_img.append(i)
                    continue
                else:

                    with open(log_file, "w") as f:
                        f.write(textb4)
                        f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')}, Process Name: Automatic Cropping\n")
                        f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')}, Current File: {i}\n") 
                    
                    if ratio_select == "Square":
                        # print("Square Selected")
                        # print("Going in")
                        faceCrop(resized_folder_path, failed_img, face_failed, i, img, imp, x, y, face_type, face_detector)
                    elif ratio_select == "Rectangle":
                        # print("Rectangle Selected")
                        rectangularCrop(resized_folder_path, failed_img, face_failed, i, img, imp, x, y, face_type, face_detector)

            elif os.path.isdir(file_loc):
                print(i, ": Is a folder")
            elif i.endswith('.txt'):
                None
            else:
                print(i, ": Is not a supported Image File")
            count += 1
            progress(count / image_count, desc=f"Cropping Images to Face, on: {i}")

    # clear_output(wait=True)

    # time.sleep(3)

    print("Image Cropping Completed")

    # time.sleep(2)

    if len(failed_img) != 0:
        print("\nThese images failed: \nReason: Invalid to load: \n", failed_img, "\nCount:", len(failed_img))

    if len(face_failed) != 0:
        print("\nThese images failed: \nReason: Face not found: \n", face_failed, "\nCount:", len(face_failed))

    with open(log_file, "w") as f:
        f.write(textb4)
        f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')}, Process Name: Automatic Cropping\n")
        f.write(f"===================== Process  Finished =====================\n\n")

def rectangularCrop(folder_dir, failed_img, face_failed, fName, img, imp=1, x=512, y=683, face_type = "Realistic", face_detector = "None"):
    
    # current_folder = os.getcwd()
    # modelFile = os.path.join(current_folder, "models", "detector_face.svm")

    # face_detector = dlib.simple_object_detector(modelFile)
    detector = dlib.get_frontal_face_detector()
    
    _, ext = os.path.splitext(fName)
    fName = fName.split(".")[0]
    if ext.lower() not in ['.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.webp']:
        print(f"Unsupported image format: {ext}")
        failed_img.append(fName)
        return

    if face_type == "Realistic":
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        oh, ow = len(gray), len(gray[0])
        faces = detector(gray)

    else:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        oh, ow = len(gray), len(gray[0])
        faces = face_detector(img)

    if len(faces) == 0:
        face_failed.append(fName)
    else:
        if face_type == "Anime-like":
            ae = detect_anime(img, 0.8, 0.009, 100, 100, "crop", face_detector)
            # print(ae)
            fx, fy, fw, fh = ae[0], ae[1], ae[2], ae[3]
        elif face_type == "Realistic":
            areas = [face.width() * face.height() for face in faces]
            max_area_index = np.argmax(areas)
            fx, fy, fw, fh = faces[max_area_index].left(), faces[max_area_index].top(), faces[max_area_index].width(), faces[max_area_index].height()

        # Calculate desired dimensions for rectangular crop (3:4 aspect ratio)
        h = fh
        w = int(h * 3 / 4)

        cx, cy = fx + fw//2, fy + fh//2

        # print(0, ow, oh)
        # print(1, fx, fy, "\n", fw, fh, "\n", h, w)

        # Apply zoom out factor
        w = int(w * imp)
        h = int(h * imp)
        # print(2, w, h)

        # print(2.2, "{}/2, {}+{}/2".format(fx, oh, fy))
        fx, fy = fx//imp, fy//(4*imp)//3
        # print(2.5, fx, fy)

        mid_x = (cx-fx)*2
        mid_y = (4*mid_x)//3
        # print(3, mid_x, mid_y)

        if fy+mid_y > oh:
            # print(1, "{} + {} > {}".format(fy, mid_y, oh))
            mid_y = oh-fy
            mid_x = (3*mid_y)//4
            # print(1.5, mid_x, mid_y)
        if fx+mid_x > ow:
            # print(2, "{} + {} > {}".format(fx, mid_x, ow))
            mid_x = ow-fx
            mid_y = (4*mid_x)//3
            # print(2.5, mid_x, mid_y)

        # Crop the rectangular region
        cropped = img[fy:fy+mid_y, fx:fx+mid_x]

        # cropped = cv2.rectangle(img, (fx, fy), (fx+fw, fy+fh), (0, 255, 0), 2)

        # Convert BGR to RGB
        cropped_rgb = cv2.cvtColor(cropped, cv2.COLOR_BGR2RGB)

        # Resize the cropped image to the specified dimensions
        cropped_resized = cv2.resize(cropped, (x, y))

        # Save the image in RGB format
        cv2.imwrite(os.path.join(folder_dir, fName + '_rectangular.png'), cropped_resized)

        return cropped_rgb
    