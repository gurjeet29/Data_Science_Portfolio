from keras.models import load_model
from flask import Flask, request, render_template, send_from_directory
import numpy as np
import os
import tensorflow as tf

UPLOAD_FOLDER = 'uploads'

model = load_model('butterfly_species_classification.h5')
model.load_weights('weights.h5')

class_names = ['ADONIS', 'AFRICAN GIANT SWALLOWTAIL', 'AMERICAN SNOOT', 'AN 88', 'APPOLLO', 'ATALA', 'BANDED ORANGE HELICONIAN',
               'BANDED PEACOCK', 'BECKERS WHITE', 'BLACK HAIRSTREAK', 'BLUE MORPHO', 'BLUE SPOTTED CROW', 'BROWN SIPROETA',
               'CABBAGE WHITE', 'CAIRNS BIRDWING', 'CHECQUERED SKIPPER', 'CHESTNUT', 'CLEOPATRA', 'CLODIUS PARNASSIAN', 'CLOUDED SULPHUR',
               'COMMON BANDED AWL', 'COMMON WOOD-NYMPH', 'COPPER TAIL', 'CRECENT', 'CRIMSON PATCH', 'DANAID EGGFLY', 'EASTERN COMA',
               'EASTERN DAPPLE WHITE', 'EASTERN PINE ELFIN', 'ELBOWED PIERROT', 'GOLD BANDED', 'GREAT EGGFLY', 'GREAT JAY',
               'GREEN CELLED CATTLEHEART', 'GREY HAIRSTREAK', 'INDRA SWALLOW', 'IPHICLUS SISTER', 'JULIA', 'LARGE MARBLE', 'MALACHITE',
               'MANGROVE SKIPPER', 'MESTRA', 'METALMARK', 'MILBERTS TORTOISESHELL', 'MONARCH', 'MOURNING CLOAK', 'ORANGE OAKLEAF',
               'ORANGE TIP', 'ORCHARD SWALLOW', 'PAINTED LADY', 'PAPER KITE', 'PEACOCK', 'PINE WHITE', 'PIPEVINE SWALLOW', 'POPINJAY',
               'PURPLE HAIRSTREAK', 'PURPLISH COPPER', 'QUESTION MARK', 'RED ADMIRAL', 'RED CRACKER', 'RED POSTMAN', 'RED SPOTTED PURPLE',
               'SCARCE SWALLOW', 'SILVER SPOT SKIPPER', 'SLEEPY ORANGE', 'SOOTYWING', 'SOUTHERN DOGFACE', 'STRAITED QUEEN',
               'TROPICAL LEAFWING', 'TWO BARRED FLASHER', 'ULYSES', 'VICEROY', 'WOOD SATYR', 'YELLOW SWALLOW TAIL', 'ZEBRA LONG WING']

app = Flask(__name__)


def classify(model, image):
    img = tf.io.read_file(image)
    img = tf.image.decode_jpeg(img, channels=3)
    img = tf.image.resize(img, [224, 224])
    # img /= 255.0  # normalize to [0,1] range
    # img_array = tf.reshape(img, (1, 224, 224, 3))

    
    img = tf.keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img, 0)

    # img = tf.keras.preprocessing.image.load_img(image, target_size=(224, 224))
    # img_array = tf.expand_dims(tf.keras.preprocessing.image.img_to_array(img), 0)

    score = tf.nn.softmax(model.predict(img_array))
    texts = "This image most likely belongs to {} ".format(class_names[np.argmax(score)])

    return texts


@app.route('/')
def welcome():
    return render_template('home.html')


@app.route('/classify', methods=['GET', 'POST'])
def upload_file():
    if request.method == "GET":
        return render_template("home.html")

    else:
        file = request.files["image"]
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        print(file_path)
        file.save(file_path)

        output = classify(model, file_path)

    return render_template("classify.html", image_file_name=file.filename, output=output)


@app.route("/classify/<filename>")
def send_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)


if __name__ == "__main__":
    app.run(debug=True,threaded=True)
