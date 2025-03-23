import gradio as gr
import os
from PIL import Image

def f(image):
    return image["composite"]

def change_tab(id, folder_root, canvas_size, crop_value):
    final_loc = []
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp']
    for i in os.listdir(folder_root):
        full_path = os.path.join(folder_root, i)
        if os.path.isfile(full_path) and os.path.splitext(i)[1].lower() in image_extensions:
            final_loc.append(full_path)
    check_box = gr.Radio(choices=["Square", "Rectangle"], label="Select Crop Ratio [1:1], [3:4]", value=canvas_size)
    value_box = gr.Textbox(label="Enter your ratio value here [Height, Width]", info="Enter the dimensions of the image you want it cropped to, eg: 512,512 [1:1] or 512,683 [3:4] [height, width]", value=crop_value)

    return gr.Tabs(selected=id), check_box, value_box, final_loc

def ratio_check(Value_Radio, Value_Box, check_btn):
    try:
        h, w = int(Value_Box.split(",")[0]), int(Value_Box.split(",")[1])
    except:
        h, w = 0, 0
    if h == 0 or w == 0:
        return gr.ImageEditor(type="filepath", interactive=True, canvas_size="1:1") if Value_Radio=="Square" else gr.ImageEditor(type="filepath", interactive=True, canvas_size="9:16")
    else: 
        return gr.ImageEditor(type="filepath", interactive=True, canvas_size="{}:{}".format(w, h))

def get_files(files_list, folder_loc, im, count, old_file, value_box):
    # print(value_box)
    h, w = int(value_box.split(",")[0]), int(value_box.split(",")[1])
    current_folder = os.getcwd()

    counter = int(count) + 1

    list_len = len(files_list) - 1 if files_list != "" else len(os.listdir(folder_loc)) - 1
    folder_path_mc = os.path.join(current_folder, "images", "outputs", "manualCrop") if files_list != "" else os.path.join(folder_loc, "manualCrop")

    if not os.path.exists(folder_path_mc):
        os.makedirs(folder_path_mc)
        file_count = 0
    else:
        file_count = len(os.listdir(folder_path_mc))

    if counter > list_len:
        print("End of List Reached")
        if old_file != " ":       
            with Image.open(old_file) as img_old:
                img_old = img_old.resize((w, h))
                img_old.save(os.path.join(folder_path_mc, "img_cropped_{}.png".format(file_count)))
        # im["composite"] = os.path.join(current_folder, "images", "static", "Designer.png")
        return gr.ImageEditor(interactive=False), counter, old_file

    else:
        filename = files_list[counter]
        im["background"] = None
        im["composite"] = filename
        im["layers"] = None

    # Save the previous image only if it exists
    if old_file != " ":
      with Image.open(old_file) as img_old:
        img_old = img_old.resize((w, h))
        img_old.save(os.path.join(folder_path_mc, "img_cropped_{}.png".format(file_count)))
    old_file = im["composite"]

    return gr.ImageEditor(value=im), counter, old_file

def check_files(images):
    a = images[0]
    return a

def set2zero(countbox):
    countbox = -1
    return countbox