# Image Aspect Ratios and Common Dimensions

This table lists common image aspect ratios and their corresponding dimensions. Remember that you can scale these dimensions up or down as long as the ratio between width and height is maintained.

| Aspect Ratio (W:H) | Description | Common Dimensions (Pixels; W x H ) | Suitable For |
|---|---|---|---|
| **1:1** | Square | 1080x1080, 1500x1500 | Lora Face Training |
| **4:3** | Traditional Screen | 800x600, 1024x768, 1600x1200 | ... |
| **3:2** | Classic Photography | 2048x1365, 3008x2008, 4032x2688 | ... |
| **16:9** | Widescreen | 1280x720, 1920x1080, 3840x2160 | ... |
| **21:9** | Ultrawide | 2560x1080, 3440x1440, 5120x2160 | ... |
| **9:16** | Portrait (Vertical Video) | 720x1280, 1080x1920 | Lora Body Training |
| **5:4** | Large Format Photography | 1200x960, 2048x1638 | Lora Style Training |
| **2:3** | Portrait (Print) | 4x6 inches, 8x12 inches | ... |
| **13:19** | Super Wide Cinema |  832x1216, 4096x2160 |  SDXL Training  | 

## Image Sizes for Training Image-Based Models

Image sizes for training can vary depending on the model and dataset complexity. Here are some common sizes:

* **224x224:** A widely used size for many image classification models (e.g., MobileNet, some ResNet variants).
* **299x299:** Used in models like Inception.
* **384x384, 512x512:** Larger sizes often used in object detection and segmentation models for better feature extraction (e.g., some ResNet and EfficientNet variants).

**Considerations:**

* **Computational cost:** Larger sizes require more memory and processing power.
* **Dataset size:** Smaller datasets may benefit from smaller image sizes to avoid overfitting.
* **Feature scale:** The chosen size should be large enough to capture relevant features for the task.

It's common to experiment with different sizes to find the best trade-off between accuracy and computational efficiency.