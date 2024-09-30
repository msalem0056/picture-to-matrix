# picture-to-matrix

**Computer Vision Showcase**

A Streamlit application that showcases what a computer "sees" versus what it shows the user. This app captures an image from the user's webcam, converts it to grayscale,
and displays both versions side by side, with the original color image and its matrix representation next to each other for easy comparison.

**How It Works**

1. The app sets a page title using `st.title()`.
2. It captures an image from the user's webcam using `st.camera_input()`.
3. If an image is captured successfully, the app:
        * Converts the raw image data to a numpy array for OpenCV.
        * Decodes the bytes into a color image using `cv2.imdecode()`.
        * Converts the color image to grayscale using `cv2.cvtColor()`.
4. The original grayscale image and its matrix representation are displayed side by side, allowing users to compare the visual output of the computer with its underlying
numerical representation.

**Code Structure**

This code is organized into a single function, `main()`, which handles camera input and image processing. The app uses Streamlit's `st` API for web development and OpenCV
for computer vision tasks.

**Requirements**

* Python 3.x
* Streamlit (>=0.80.0)
* OpenCV (>=4.5.1)

**Author**

Mike Salem
[mike.f.salem@gmail.com](mailto:mike.f.salem@gmail.com)

**License**

None
