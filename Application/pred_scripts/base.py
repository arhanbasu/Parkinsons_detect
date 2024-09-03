import os
import tensorflow as tf
from PIL import Image
import numpy as np

def base_predict():
    model = tf.keras.models.load_model('../Models/Basic/basic3_80.h5')
    tf.keras.utils.plot_model(model, to_file='model.png', show_shapes=True, show_layer_activations=True)

    # Image loading and reshaping
    img = Image.open('./media/upload.png')
    img = img.resize((224,224))
    img_arr = np.array(img)

    # Image pre-processing
    pre_processor = tf.keras.applications.vgg16.preprocess_input
    img_arr = pre_processor(img_arr)

    # Image normalization
    img_arr = img_arr/255

    # Image put in a batch
    img_arr = np.expand_dims(img_arr, axis=0)

    # Model prediction
    result = model.predict(img_arr)

    safe = result[0][0]
    infected = result[0][1]

    percentage = (infected/(safe+infected))*100

    print(safe, infected)
    return percentage, infected > safe

# print(os.getcwd())
# os.chdir('../Models/Basic')
# print(os.getcwd())
base_predict()