import time,cv2, json, nltk, re, os
import numpy as np
from flask import Flask, request, redirect, render_template
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


app = Flask(__name__)

#sentiment analysis
stop_word = stopwords.words('english')
lemmatizer = WordNetLemmatizer()
sentiment_model = load_model('E:/UMM/Akademik/Semester 7/Praktikum/Modul/Praktikum ML/Modul 6/text.h5')
tokenizer = Tokenizer(num_words=5000)

file_path = os.path.join(os.path.dirname(__file__), 'word_index.json')

# Load word index from file if exists
if os.path.exists(file_path):
    with open(file_path, 'r') as json_file:
        loaded_word_index = json.load(json_file)
else:
    print(f"The file {file_path} does not exist.")

#Load model untuk klasifikasi citra
citra_model = load_model('E:/UMM/Akademik/Semester 7/Praktikum/Modul/Praktikum ML/Modul 6/citra.h5')


# Disable caching for all routes
@app.after_request
def add_header(r):
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

# Home page
@app.route("/")
def index():
    return render_template('index.html')

# Tabular data page
@app.route("/tabular")
def tabular():
    return render_template('tabular.html')

# Text analysis page
@app.route("/text")
def text():
    return render_template('text.html')

# Text analysis prediction
@app.route("/textpredict", methods=['POST'])
def predict_text():
    # Memastikan bahwa metode HTTP yang digunakan adalah POST
    if request.method == 'POST':
        # Mengambil teks dari formulir pada halaman web
        text = request.form['texts']
        print(text)
        # Menganalisis sentimen teks menggunakan fungsi analyze_sentiment
        analysis, time, prob = analyze_sentiment(text)
        print(analysis)

        # Mengubah nilai prediksi numerik menjadi label kategori yang lebih mudah dipahami
        if int(analysis) == 2:
            analysis = 'POSITIF'
        elif int(analysis) == 1:
            analysis = 'NEUTRAL'
        else:
            analysis = 'NEGATIVE'

    # Merender halaman web 'text.html' dengan hasil analisis sentimen
    return render_template('text.html', analysis=analysis, time=time, prob=prob)

# Clean and preprocess text data (lowercasing, remove punctuation, stop word removal, and lemmatize each word)
def clean_text(text):
    text = text.lower()
    text = re.sub(r'https?://\S+|www\.\S+', '', text)
    text = re.sub(r'\d+', '', text)
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    tokens = nltk.word_tokenize(text)
    cleaned_sentence = [sentence for sentence in tokens if sentence not in stop_word]
    lemma_res = [lemmatizer.lemmatize(sentence) for sentence in cleaned_sentence]
    return ' '.join(lemma_res)

# Analyze sentiment of the given text
def analyze_sentiment(text):
    cleaned_text = clean_text(text)
    sequences = [[loaded_word_index[word] for word in cleaned_text.split() if word in loaded_word_index]]
    print(sequences)
    padded_sequence = pad_sequences(sequences, maxlen=200)
    print(padded_sequence)
    # Memulai perhitungan waktu untuk mengukur kinerja
    start = time.time()
    # Melakukan prediksi sentimen menggunakan model yang telah dimuat
    prediction = sentiment_model.predict(padded_sequence)
    predicted_labels = np.argmax(prediction, axis =1)
    runtimes = round(time.time()-start,4)
    print(prediction)
    rounded_prediction = np.round(prediction * 100, 2)
    respon_model = rounded_prediction.tolist()

    # Mengembalikan label prediksi, waktu eksekusi, dan hasil prediksi
    return predicted_labels, runtimes, respon_model

# Image analysis page
@app.route("/citra")
def citra():
    return render_template('citra.html')

# Image analysis prediction
@app.route("/citrapredict", methods=['POST'])
def predict_citra():
    # Memastikan bahwa metode HTTP yang digunakan adalah POST
    if request.method == 'POST':
        # Mengambil file gambar dari formulir pada halaman web
        file = request.files["file"]        
        os.makedirs('static/img', exist_ok=True)
        file_path = 'static/img/temp.jpg'
        file.save(file_path)
        img = cv2.imread(file_path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = np.expand_dims(cv2.resize(img, citra_model.layers[0].input_shape[0][1:3] \
        if not citra_model.layers[0].input_shape[1:3] else citra_model.layers[0].input_shape \
        [1:3]).astype('float32') / 255, axis=0)

        # Memulai perhitungan waktu untuk mengukur kinerja
        start = time.time()

        # Melakukan prediksi kelas gambar menggunakan model yang telah dimuat
        pred = citra_model.predict(img)[0]
        runtimes = round(time.time()-start,4)
        respon_model = [round(elem * 100, 2) for elem in pred]
        class_list = {'Paper': 0, 'Rock': 1, 'Scissor' : 2}
        idx_pred = respon_model.index(max(respon_model))
        labels = list(class_list.keys())[idx_pred]

    # Merender halaman web 'citra.html' dengan hasil analisis gambar
    return render_template('citra.html', pred=pred, time=runtimes, prob=respon_model, label=labels, idx = idx_pred, img ='temp.jpg')


if __name__ == "__main__":
    app.run(debug=True)