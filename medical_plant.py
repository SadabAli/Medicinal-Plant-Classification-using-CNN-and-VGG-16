import numpy as np
import tensorflow as tf
from flask import Flask, render_template, request
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import os

app = Flask(__name__)

# Load the Keras model
model = tf.keras.models.load_model(r'D:\MedicalPlant\VGG16_version_2.keras')

# Define the class labels for prediction
class_labels = [
    'Arive-Dantu', 'Basale', 'Betel', 'Crape_Jasmine', 'Curry', 'Drumstick', 
    'Fenugreek', 'Guava', 'Hibiscus', 'Indian_Beech', 'Indian_Mustard', 
    'Jackfruit', 'Jamaica_Cherry-Gasagase', 'Jamun', 'Jasmine', 'Karanda', 
    'Lemon', 'Mango', 'Mexican_Mint', 'Mint', 'Neem', 'Oleander', 'Parijata', 
    'Peepal', 'Pomegranate', 'Rasna', 'Rose_apple', 'Roxburgh_fig', 
    'Sandalwood', 'Tulsi'
]

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def predict_image():
    # Access the image file
    imagefile = request.files['imagefile']
    
    # Define the path to save the image
    image_path = os.path.join('./static/images', imagefile.filename)  # Save image in 'static/images' folder
    
    # Ensure the images directory exists
    os.makedirs('./static/images', exist_ok=True)
    
    # Save the image
    imagefile.save(image_path)
    
    # Load and preprocess the image
    image = load_img(image_path, target_size=(224, 224))  # Load the image with target size
    image = img_to_array(image)  # Convert image to array
    image = np.array([image])  # Add batch dimension

    # Perform prediction
    yhat = model.predict(image)  # This returns an array of probabilities for each class
    
    # Get the index of the highest probability
    predicted_index = np.argmax(yhat, axis=1)[0]
    
    # Map the predicted index to the corresponding class label
    predicted_label = class_labels[predicted_index]
    
    # Get the probability of the predicted label
    predicted_probability = yhat[0][predicted_index] * 100  # Convert to percentage
    
    # Format the classification output
    classification = '%s (%.2f%%)' % (predicted_label, predicted_probability)
    
    # Return the result to the web page with the image path
    return render_template('index.html', prediction=classification, image_file=imagefile.filename)

if __name__ == '__main__':
    app.run(debug=True)
