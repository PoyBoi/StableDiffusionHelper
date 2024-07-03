import gradio as gr

from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

import time, datetime

from numba import cuda

from scripts.gradio_code import f, ratio_check, get_files, set2zero, change_tab

from scripts.caption_list import get_most_common_words
from scripts.delete_words import process_files
from scripts.img_processing import convert_images_to_png, process_images, select_best_images, remove_background_from_images, main_call

# Clearing VRAM
def clear_vram():
    # torch.cuda.empty_cache()

    # CUDA (via Numba)
    cuda.select_device(0)
    cuda.close()

# ================================================================================================================================
# ----- IMAGE -----
# ================================================================================================================================

# __Main__ call
def main_call_g(folder_loc, ratio_select, x_thresh, y_thresh, process_select, adv_process_select, blur_thresh, min_sharp, min_size, min_conf, top_n, h, w, crop_select, zoom2face, face_type, progress = gr.Progress()):
    progress(0, desc="Starting...")
    time.sleep(1)
    
    # LOGGING
    log_file = "sdh_log.txt"
    start_time = time.strftime('%Y-%m-%d %H:%M:%S')

    with open(log_file, "w") as g:
        g.write("""
====================StableDiffusionHelper====================
====================      by PoyBoi      ====================
=============== Started @ {} ===============
=============================================================

""".format(start_time))
        g.close()
    
    start_time = datetime.datetime.now()
    
    convert_images_to_png(folder_loc)
    if "Duplicate Check" in process_select:
        process_images(folder_path = folder_loc, x = x_thresh, y = y_thresh)
    if "Suitability Check" in process_select:
        folder_loc = select_best_images(folder_loc, face_type, float(min_conf), float(min_size), float(min_sharp), float(blur_thresh), int(top_n))
    if "Remove Background" in adv_process_select:
        folder_loc = remove_background_from_images(folder_loc, "No_BG")
    if crop_select == "Face Crop[Auto]":
        main_call(folder_loc, h, w, zoom2face, ratio_select, face_type)
    elif crop_select == "Face Crop[Manual]":
        return "❤️ All Processing Done ❤️", gr.Button(value="Click to go to Manual Cropping", visible=True)
    
    end_time = datetime.datetime.now()
    time_taken = end_time - start_time

    with open(log_file, "a") as g:
        g.write(f"""
\n
=============================================================
======================= Process took: =======================
                       {time_taken}                        
======================== ~ THANKS ~ =========================
""")

    return "❤️ All Processing Done ❤️", gr.Button(visible=False)

# Confirm Buttons
def launch_check(folder_loc, process_select, adv_process_select, ratio_select, ratio_int, thresh, zoom2face, crop_select="None"):
    try:
        w, h = int(ratio_int.split(",")[0]), int(ratio_int.split(",")[1])
        x_thresh, y_thresh = int(thresh.split(",")[0]), int(thresh.split(",")[1])
        # return "Folder Location: \t\t\t\t\t\t\t\t\t\t\t" + folder_loc + "\n\nBasic Processes Selected: \t\t\t\t\t\t" + ', '.join(process_select) + "\n\nAdvanced Proccesses Selected: \t\t\t" + ', '.join(adv_process_select) + "\n\nRatio Selected: \t\t\t\t\t\t\t\t\t\t\t{} with Height: {} Pixels, Width: {} Pixels".format(ratio_select, h, w) + "\nRemove Images smaller than: \t\t\t\t{}x{}".format(x_thresh, y_thresh) + "\nCrop Method: \t\t\t\t\t\t\t\t\t\t\t\t{}".format(crop_select) + "\nZoom Ratio: \t\t\t\t\t\t\t\t\t\t\t\t\t{}".format(zoom2face)
        data = [
            ["Folder Location", folder_loc],
            ["", ""],
            ["Basic Processes", process_select],
            ["Advanced Processes", adv_process_select], 
            ["", ""],
            ["Image Resize Size", f"Height: {h}, Width: {w}"],
            ["Crop Ratio", ratio_select],
            ["Image Size Threshold", f"Height: {y_thresh}, Width: {x_thresh}"],
            ["Crop Method", crop_select],
            ["", ""],
            ["Face Zoom-Out Multiplier", zoom2face]
        ]
        
        return gr.Dataframe(value=data, visible=True)
    except Exception as e:
        return "⭕ ERROR ⭕: Cause: \n\n🔧{}🔧".format(e)

# Launch Execution
def launch_confirm(folder_loc, process_select, adv_process_select, ratio_select, ratio_int, thresh, blur_thresh, min_sharp, min_size, min_conf, top_n, crop_select, zoom2face, face_type):
    try:
        h, w = int(ratio_int.split(",")[0]), int(ratio_int.split(",")[1])
        x_thresh, y_thresh = int(thresh.split(",")[0]), int(thresh.split(",")[1])
        zoom2face = int(zoom2face)

        _, button = main_call_g(folder_loc, ratio_select, x_thresh, y_thresh, process_select, adv_process_select, blur_thresh, min_sharp, min_size, min_conf, top_n, h, w, crop_select, zoom2face, face_type)

        return "❤️ All Processing Done ❤️" , button, gr.Textbox(visible=False, value=folder_loc)

    except Exception as e:
        return "Processing Status: ⭕ ERROR ⭕: Cause: \n\n🔧{}🔧".format(e)

# ================================================================================================================================
# ----- CAPTION -----
# ================================================================================================================================

# To read the files, get the captions, and show them as a checkbox
def read_files(folder_loc, max_count, category):
    text_choices = get_most_common_words(folder_loc, max_count)
    return gr.CheckboxGroup(choices=text_choices, interactive=True)

def process_text_files(folder_loc, words_list, charName):
    process_files(folder_loc, words_list, charName)
    return "Processing status: ⭐ Done ⭐"

#__main__
with gr.Blocks(theme=gr.themes.Default(primary_hue="orange", secondary_hue="orange", neutral_hue="gray")) as UI:
    with gr.Row():
        gr.Markdown("# 🚀StableDiffusionHelper🚀 by [PoyBoi](https://github.com/PoyBoi)")
        vram_clear_btn = gr.Button("Clear VRAM")
        vram_clear_btn.click(
            fn = clear_vram
        )

    # ================================================================================================================================
    # IMAGE PROCESSING TAB
    # ================================================================================================================================
    with gr.Tabs() as tabs:
        with gr.TabItem("Image Processing", id=0):
            with gr.Row():
                folder_loc = gr.Textbox(label="Image Folder Location", visible=True, interactive=True, placeholder="C:\Downloads")
            
            with gr.Row():
                ratio_select = gr.Radio(["Square", "Rectangle"], label="Select Image Crop Type", info="Select the ratio between 1:1 or 3:4")
                ratio_int = gr.Textbox(label= "Image Crop Dimensions", info="Enter the dimensions of the image you want it cropped to, eg: 512,512 [1:1] or 512,683 [3:4] [width, height]", value="512, 512")
                thresh = gr.Textbox(label= "Image Size Threshold", info="Enter the dimensions of the images which smaller than are moved to a different folder, eg: 700,700 - Removes all images smaller than this size", value="700, 700")

            with gr.Row():
                with gr.Column():
                    process_select = gr.CheckboxGroup(choices=["Duplicate Check", "Suitability Check"], label="Select either one, or both")
                    adv_process_select = gr.CheckboxGroup(choices=["Remove Background"], label="Select removal of background from images")
                    top_n = gr.Textbox(label="These are the top n Images selected from your folder", info="Only enter values if you are using Suitabilty Check", value=50)
                with gr.Column():
                    face_type = gr.Radio(choices=["Realistic", "Anime-like"], label="Select the face type found in the dataset")                
                    with gr.Row():
                        crop_select = gr.Radio(choices=["Face Crop[Auto]", "Face Crop[Manual]"], label="Choose Cropping Method", info="Selecting Manual Cropping will open a tab")
                        zoom_ratio = gr.Slider(minimum=1, maximum=10, label="Controls how much the crop should zoom out of the face", info="Values abpve 1 will multiply the crop'ers dimension box", step=1, value=2)
            gr.Markdown("Below are values for 'Crop Image to Face' ")

            with gr.Row():
                min_conf = gr.Textbox(label="Minimum Confidence of the face in the image", info="Leave at Default if you don't know what you're doing", value = 0.8)
                min_size = gr.Textbox(label="Minimum Size of face in image", info="Leave at Default if you don't know what you're doing", value = 0.009)
                min_sharp = gr.Textbox(label="Minimum Threshold for Image Sharpness", info="Leave at Default if you don't know what you're doing", value = 100)
                blur_thresh = gr.Textbox(label="Threshold for Image Blurriness", info="Leave at Default if you don't know what you're doing", value = 100)


            check_btn = gr.Button("Check Choices")
            outputs_check = gr.Dataframe(label="Selected Value", headers=["Choice", "Value"], interactive=False, visible=False)

            final_check = gr.Button("Start processing")
            btn_mc = gr.Button(visible=False)
            final_output = gr.Textbox("Processing Status: Inactive", label="Processing Status", info="Updates will come here")
            file_loc = gr.Textbox(value=" ", visible=False)

            check_btn.click(
                fn=launch_check, 
                inputs=[folder_loc, process_select, adv_process_select, ratio_select, ratio_int, thresh, zoom_ratio, crop_select], 
                outputs=[outputs_check]
            )

            # Final check was here
            final_check.click(
                fn = launch_confirm,
                inputs = [folder_loc, process_select, adv_process_select, ratio_select, ratio_int, thresh, blur_thresh, min_sharp, min_size, min_conf, top_n, crop_select, zoom_ratio, face_type], 
                outputs = [final_output, btn_mc, file_loc]
            )

        # ================================================================================================================================
        # CAPTION PROCESSING TAB
        # ================================================================================================================================

        # with gr.Accordion("Caption Processing Tab", open=False):
        with gr.TabItem("Caption Processing", id=1):

            #Enter Folder Location
            with gr.Row():
                folder_loc = gr.Textbox(label="Caption Folder Location")

            # Enter char name and max count
            with gr.Row():
                charName = gr.Textbox(label="Enter your Character Name here", info="This is the UNIQUE name of the character/style that you want to train.")
                word_count = gr.Textbox(label="Max count of captions", info="Select how many n top captions you want to see from the caption files")

            desc_btn = gr.Button("See Most Used words")
            word_select = gr.CheckboxGroup(choices=["NaN"], label="Select the words to delete", info="This will display the most used words in order of count")
            
            desc_btn.click(
                fn=read_files, 
                inputs=[folder_loc, word_count, desc_btn], 
                outputs=[word_select]
            )

            # Update the text files
            start_update_caption = gr.Button("Process the Caption Files")
            status_txt = gr.Textbox("Processing status: Inactive", label="Processing Status", info="Once done, you can run the \"See Most Used Words\" to see that the change has taken place")
            start_update_caption.click(
                fn = process_text_files,
                inputs = [folder_loc, word_select, charName],
                outputs = status_txt
            )

        # ================================================================================================================================
        # MANUAL CROPPING TAB
        # ================================================================================================================================

        with gr.TabItem("Manual Cropping", id=2):
            with gr.Row():
                check_box = gr.Radio(choices=["Square", "Rectangle"], label="Select Crop Ratio [1:1], [9:16]", visible=False)
                value_box = gr.Textbox(label="Enter your ratio value here [Height, Width]", info="Enter the dimensions of the image you want it cropped to, eg: 512,512 [1:1] or 683,512 [4:3] [height, width]", value="512, 512")

            with gr.Row():
                check_btn = gr.Button("Apply Sizes")
                load_images = gr.UploadButton("Upload Images from Folder", file_count="multiple")
                check_images = gr.Button("Load Images")

            with gr.Row():
                inputs = gr.ImageEditor(type="filepath", crop_size="1:1")
                output = gr.Image(type="filepath", label="Output Image", height = 500, width = 500)
            with gr.Row():
                next_button = gr.Button("Next Image")
            
            count_box = gr.Textbox(value = -1, visible=False)
            old_file = gr.Textbox(value=" ", visible=False)
            
            load_images.click(
                fn = set2zero,
                inputs = count_box,
                outputs = count_box
            )

            check_btn.click(
                fn = ratio_check,
                inputs = [check_box, value_box, check_btn],
                outputs = [inputs]
            )
            inputs.change(fn = f, outputs=output, inputs=inputs)

            check_images.click(
                fn = get_files,
                inputs = [load_images, file_loc, inputs, count_box, old_file, value_box],
                outputs = [inputs, count_box, old_file]
            )

            next_button.click(
                fn = get_files,
                inputs = [load_images, file_loc, inputs, count_box, output, value_box],
                outputs = [inputs, count_box, old_file]
            )
            
            # =====================================================================
            # MISC BUTTONS FROM ABOVE
            # =====================================================================
            
            btn_mc.click(
                change_tab, 
                [gr.Number(2, visible=False), file_loc, ratio_select, ratio_int], 
                [tabs, check_box, value_box, load_images]
            )

try:
    UI.queue()
    UI.launch()
except Exception as e:
    print("HARD ERROR:", e)