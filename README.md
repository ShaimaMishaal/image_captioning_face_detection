
## 🤖 Face Detection & Image Captioning :

A simple app to upload or capture an image, detect faces with bounding boxes, and generate a caption.

## ✨ Features :
1. Upload or capture image.
2. Detect faces and draw bounding boxes.
3. Generate image captions using a pre-trained model.

## ⚙️ Models Used :
1. For Face Detection ( face_recognition ) :
   * This model finds faces in a picture.
   * It checks the image and looks for face features.
   * It gives the position of each face so we can draw a box around it.


2. For Image Captioning ( Salesforce/blip-image-captioning-base ) :
   * This model looks at the image and writes a short description of what it sees.
   * It understands the full picture, not only objects.
   * It gives one sentence that explains what’s in the image.

## 🛠️ How to Setup and Run :
1. Clone the repository :
   ```
   git clone https://github.com/ShaimaMishaal/image_captioning_face_detection.git
2. Navigate to the project directory:
   ```
   cd image_captioning_face_detection
4. Create virtual environment :
   ```
   python -m venv venv
   ```
   Then activate the environment
   
   * For Windows :
     ```
     .\venv\Scripts\activate
   * For Linux / macOS :
     ```
     source venv/bin/activate
6. Install dependencies :
   ```
   pip install -r requirements.txt
7. Run the Streamlit app :
   ```
   streamlit run app.py
## ⚠️ Notes :
1. Installing face_recognition might require additional system packages like CMake and dlib.
2. Caption generation speed depends on your device performance and internet connection.
