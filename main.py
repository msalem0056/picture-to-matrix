"""
This code captures an image from the user's webcam using Streamlit's `camera_input` function and then converts it to grayscale. The grayscale image and the matrix representation version
version are then displayed side by side on a web page, showcasing what the computer "sees" versus what the computer shows the user.
"""

# -- Standard Imports

# -- Third-Party Imports
import cv2
import numpy as np
import streamlit as st

# -- Local Imports

__author__ = "Mike Salem"
__email__ = "mike.f.salem@gmail.com"


def main() -> None:  # Main function to handle camera input and image processing

    """
    Display a title, capture an image from the user's webcam,
    convert it to grayscale, and display both the original image and its grayscale version.
    """

    # Set page title
    st.title("What does a computer 'see'?")

    # Capture image from webcam
    camera_capture = st.camera_input("")


    if camera_capture is not None:  # Check if an image was captured

        # Get raw image data as bytes
        bytes_data = camera_capture.getvalue()

        # Convert bytes to numpy array for opencv
        color_img = cv2.imdecode(
            np.frombuffer(bytes_data, dtype=np.uint8),
            flags=cv2.IMREAD_COLOR
        )

        # Convert color to grayscale
        gray_img = cv2.cvtColor(
            color_img,
            code=cv2.COLOR_BGR2GRAY
        )


        computer, human, canny = st.tabs(['Computer Sees', 'You See', 'Canny'])
        # Display section title and grayscale image
        with computer:
            st.write("# What the computer sees")
            st.write(gray_img)

        # Display section title and original (grayscale) image with specified width
        with human:
            st.write("# What the computer shows you")
            st.image(gray_img)

        # Apply Gaussian blur to reduce noise
        with canny:
            blurred = cv2.GaussianBlur(gray_img, (5, 5), 0)
            st.image(blurred)

            # Apply Canny edge detection
            edges = cv2.Canny(blurred, 10, 250)
            st.image(edges)




if __name__ == "__main__":
    main()
