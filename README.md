# Pothole Detection Using Image Processing

## Project Overview
This project detects potential pothole regions in road images using traditional digital image processing techniques. It is developed as a mini-project for the Signal and Image Processing (SIP) subject.

The project uses image processing methods rather than Machine Learning or Deep Learning.

## Objectives
- Process road images using digital image processing techniques.
- Detect edges and dark regions that may indicate potholes.
- Highlight potential pothole regions with red bounding boxes.
- Save the processed images for visual analysis.

## Technologies Used
- Python
- OpenCV
- NumPy
- Matplotlib

## Image Processing Techniques
1. **Grayscale Conversion:** Converts the input image into grayscale.
2. **Gaussian Blur:** Reduces noise and small variations in the image.
3. **Canny Edge Detection:** Detects edges in the road image.
4. **Otsu Thresholding:** Separates darker regions from brighter regions.
5. **Contour Detection:** Identifies candidate regions in the thresholded image.
6. **Area Filtering and Bounding Boxes:** Filters regions by size and marks candidate pothole regions with red rectangles.

## Project Structure
```text
Pothole-Detection-SIP/
├── images/
│   ├── road.jpg
│   ├── road2.jpg
│   └── road3.jpg
├── outputs/
│   └── .gitkeep
├── pothole_detection.py
└── README.md
```

## Requirements
Install Python and the required libraries:

```bash
pip install opencv-python numpy matplotlib
```

## How to Run
1. Clone or download this repository.
2. Open the project folder in VS Code.
3. Open `pothole_detection.py`.
4. Set the input image path to one of the available images, for example:

```python
IMAGE_PATH = "images/road.jpg"
```

5. Run the script:

```bash
python pothole_detection.py
```

6. Check the `outputs/` folder for the processed images and final result.

## Output
The program generates intermediate and final images, including grayscale conversion, filtering, edge detection, thresholding, and a final image with candidate regions highlighted.

## Limitations
This is a basic image-processing approach. It identifies dark regions that may resemble potholes, so shadows, road markings, and other dark objects can also be detected. The detected regions are candidates and are not guaranteed to be actual potholes.

## Conclusion
This project demonstrates how traditional digital image processing techniques can be combined to identify and highlight potential pothole regions in road images without using Machine Learning or Deep Learning.

---
**Subject:** Signal and Image Processing (SIP)  
**Project:** Pothole Detection using Traditional Image Processing
