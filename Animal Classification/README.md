# Animal Classification Project

## Overview
This project implements a deep learning-based animal classification system with two operational modes:
1. **Real-time classification** using a laptop webcam
2. **Manual prediction** from image files....using paths of specific images

The system classifies images into 15 animal categories using a convolutional neural network (CNN) model. The model achieves approximately 92% accuracy on the validation dataset.

## File Structure
```
Animal Classification/
├── README.md                   # Project documentation
├── image_classification_using_Webcam.py  # Real-time classification 
├── Manual_prediction.py        # Image file classification
├── animal_classifier_model.h5  # Initial trained model
├── animal_classifier_model_v2.h5  # Improved accuracy model
├── Image Classification of animals.pdf  # Project instructions report
└── dataset/                    # Animal image dataset (1,944 images across 15 classes)
    ├── Bear/
    ├── Bird/
    ├── Cat/
    ├── Cow/
    ├── Deer/
    ├── Dog/
    ├── Dolphin/
    ├── Elephant/
    ├── Giraffe/
    ├── Horse/
    ├── Kangaroo/
    ├── Lion/
    ├── Panda/
    ├── Tiger/
    └── Zebra/
```

## Technology Stack
- **Deep Learning**: TensorFlow 2.x, Keras
- **Computer Vision**: OpenCV 4.x
- **Image Processing**: Keras preprocessing utilities
- **Scientific Computing**: NumPy
- **Model Format**: HDF5 (.h5)
- **Programming Language**: Python 3.11.9 (must install it to run this project)

## Key Features
### 1. Real-time Classification (`image_classification_using_Webcam.py`)
- Captures live video feed from webcam
- Performs frame-by-frame classification at ~10 FPS
- Preprocessing:
  - Resizes frames to 224x224 pixels
  - Normalizes pixel values (0-1 range)
  - Converts to array format
- Displays prediction with confidence percentage in real-time
- Exit by pressing 'q' key

### 2. Manual Prediction/Without using Camera(`Manual_prediction.py`)
- Classifies a single image file
- Supports common image formats (JPG, PNG, etc.)
- Outputs predicted class to console
- Requires modifying `img_path` variable to target image

## Setup Instructions
1. Install required packages:
```bash
pip install tensorflow opencv-python numpy
```

2. Run real-time classification (uses improved v2 model):
```bash
python image_classification_using_Webcam.py
```

3. For manual prediction:
   1. Open `Manual_prediction.py`
   2. Modify `img_path` to target image:
      ```python
      img_path = "path/to/your/image.jpg"
      ```
   3. Run script:
      ```bash
      python Manual_prediction.py
      ```

## How It Works
1. **Image Preprocessing**:
   - Resizing to 224x224 pixels
   - Pixel normalization (0-1 range)
   - Array expansion for batch dimension

2. **Model Inference**:
   - Uses pre-trained CNN model
   - Outputs probability distribution over 15 classes
   - Selects class with highest probability

3. **Output**:
   - Real-time: Overlays prediction on video feed
   - Manual: Prints prediction to console

## Models
- `animal_classifier_model.h5`: Initial model (85% accuracy)
- `animal_classifier_model_v2.h5`: Improved model (92% accuracy)
  - Used in real-time classification script
  - Better generalization and reduced overfitting

## Dataset
- Contains 1,944 images across 15  animal classes
- 30 images per class
- Animal classes: Bear, Bird, Cat, Cow, Deer, Dog, Dolphin, Elephant, Giraffe, Horse, Kangaroo, Lion, Panda, Tiger, Zebra
- Images show animals in various poses and environments
