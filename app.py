import streamlit as st # For building web app
import cv2 # For image processing
import face_recognition # To detect faces
from PIL import Image  # To handle images
import numpy as np  # For array manipulation
from transformers import pipeline # For image captioning

# ---------------------- PAGE CONFIGURATION ------------------------

# Set up the Streamlit app page with title and icon
st.set_page_config(page_title="Face Detection & Image Captioning", page_icon="🤖") 

# Display the main header of the app
st.header("🧑Face Detection & Image Captioning", divider="blue")

# Show a brief description
st.markdown("**A simple app to upload or capture an image, detect faces with bounding boxes, and generate a caption.**")
st.markdown("**Please uploead :blue-background[or] take picture :**")

# ---------------------- IMAGE INPUT SECTION -----------------------

# Create two columns for file upload and camera input
col1, col2 = st.columns(2)

# First column for file uploader to upload an image 
with col1:
    uploaded_file = st.file_uploader("📥Upload an image", type=["jpg", "jpeg", "png"])

# Second column for camera input to take a photo 
with col2:
    camera_image = st.camera_input("📸Take a photo")

# Initialize variable to hold the final image to process
final_image = None

# Choose the image source
if camera_image is not None:
    final_image = camera_image
elif uploaded_file is not None:
    final_image = uploaded_file
    
# ---------------------- RESULTS SECTION -----------------------

# Subheader for showing detection and caption results
st.subheader("Detection & Caption Results :", divider="blue")

# Process image if provided 
if final_image is not None:
    # Open the image and convert to RGB format
    image = Image.open(final_image).convert("RGB")   
    
    # Convert image to a NumPy array for face detection
    img_array = np.array(image)
    
    # Detecting faces using a built-in model from the face_recognition library
    face_locations = face_recognition.face_locations(img_array)
    
    # Copy image array to draw bounding boxes on it
    image_with_boxes = img_array.copy()
    
    # Draw green rectangles around detected faces
    for top, right, bottom, left in face_locations:
        cv2.rectangle(image_with_boxes, (left, top), (right, bottom), (0, 255, 0), 2)
        
    # Show loading spinner while generating results
    with st.spinner("Generating the image with face bounding boxes and text caption ..."):
        # Create two columns to display images side by side
        col1, col2 = st.columns(2)
        
        # Display original image 
        with col1:
            st.write("🖼️ Original Uploaded Image :")
            st.image(image) 
        
        # Using a pre-trained image captioning model to generate a caption     
        with col2:
            captioner=pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")
            caption = captioner(image)[0]['generated_text']
            
            # Display image with face bounding boxes and generated caption
            st.write("🔍 Image With Face Boxes :")
            st.image(image_with_boxes, caption= caption)
