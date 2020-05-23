from keras.models import load_model
from keras.models import Model
import numpy as np
from keras.preprocessing import image
import os

def classify (img_query):
    model = load_model(os.path.dirname(__file__) + '/../modello.h5')

    img = image.load_img(img_query, target_size=(80, 60))
    img_tensor = image.img_to_array(img)
    img_tensor = np.expand_dims(img_tensor, axis=0)
    img_tensor /= 255.

    predictions = model.predict(img_tensor)
    
    y_classes= predictions.argmax(axis=-1)
    
    classi = ['Apparel Set','Bags and Wallets', 'Belts', 'Bottomwear', 'Cufflinks','Dress','Eyewear','Flip Flops','Fragrance','Headwear','Innerwear','Jewellery','Sandal','Saree','Scarves','Shoes','Socks','Ties','Topwear','Watches']
    
    print( classi[y_classes[0]])

    return classi[y_classes[0]]

