# Web App implement ML Models

Proyek ini adalah implementasi aplikasi web yang memanfaatkan kekuatan berbagai model pembelajaran mesin untuk melakukan prediksi pada berbagai jenis data, termasuk data tabular, teks, dan citra. Dengan menggunakan Flask sebagai framework utama, proyek ini bertujuan untuk memberikan antarmuka yang intuitif dan mudah digunakan bagi pengguna untuk menerapkan model ML pada data mereka.

## Daftar Isi

- [Deskripsi Proyek](#Web-App-implement-ML-Models)
- [Dataset](#WOverview-Dataset)
- [Fitur Utama](#Fitur-Utama)
- [Project Flow Data Teks](#Project-flow-Data-Text)
- [Project Flow Data Citra](#Project-flow-Data-Citra)
- [Instalasi](#instalasi)
- [Cara Penggunaan](#cara-penggunaan)
- [Kontribusi](#kontribusi)
- [Author](#Author)
- [Bash](#bash)

## Overview Dataset
Dataset yang digunakan mencakup data Tabular, Teks, dan Citra. data tabular memiliki jumlah kelas sebanyak 2 (binary) yang menentukan data termasuk kedalam kelas Income_>50K atau dibawah. Data Teks memiliki jumlah kelas sebanyak 3(Muli kelas) sebagai penentu teks termasuk kedalam label Negative, Neutral, atau Positive. Data Citra yang digunakan adalah data Rock, paper, Scissors (3 Kelas) sebagai penentu gambar termasuk kedalam kelas (R/P/S). Agar dapat meningkatkan pemahaman lebih terhadap dataset yang saya jelaskan, dataset tersebut dapat dilihat di [sini](https://drive.google.com/drive/folders/1LLWPaI13a5hDUFocoFy6BxHQRmtH3QRm?usp=drive_link)

## Fitur Utama
1. Prediksi Multitipe Data: Aplikasi ini mendukung prediksi pada data berjenis tabular, teks, dan citra. Pengguna dapat mengunggah dataset mereka sesuai jenis data 
  yang diinginkan dan mendapatkan hasil prediksi menggunakan model yang sesuai.

2. Model Pembelajaran Mesin Terkemuka: Proyek ini menggunakan beberapa model pembelajaran mesin unggulan, termasuk:
 - TABNET: Model yang efisien untuk data tabular dengan kemampuan pembelajaran yang mendalam.
 - RNN: Model rekuren untuk memproses dan memahami data teks secara kontekstual.
 - DENSENET169: Model konvolusional untuk mengatasi tugas prediksi pada data citra.

3. Interface yang digunakan adalah HTML, CSS, dan JavaScript.


## Project Flow Data Text
1. Load Dataset Text

Pada tahapan ini, data yang diperoleh diload kedalam program. Berikut merupakan contoh dari masing - masing fitur dalam dataset.

![image](https://github.com/RahmatPrakoso276/deploy-ml-project1/assets/79794844/3b3884ca-1faa-4150-8e60-2433ade7e842)

Distribusi target kelas nya dapat dilihat sebagai berikut:

![image](https://github.com/RahmatPrakoso276/deploy-ml-project1/assets/79794844/4af657ea-62a5-46ac-b03e-61018632766b)

3. Data Preprocessing 
   
Data Preprocessing teks dalam project ini meliputi : 
- Removing null & duplicated Values
  Null values dalam dataset tersebut sebanyak 3 instance pada kolom 'cleaned_review' sedangkan uplicated values dalam dataset tersebut sebanyak 1348 instance. untuk handlingnya adalah dengan melakukan penghapusan instance yang memiliki nilai tersebut.
  
- removing unrelevant feature
  Perlu dilakukan penhapusan feature/kolom yang tidak memiliki pengaruh terhadap model klasifikasi yang kita ingin buat. dalam kasus ini feature yang dihapus adalah 'cleander_review_length' dan 'review_score'

- removing punctuation
  Tanda baca seperti koma, titik, tanda tanya, dan lainnya seringkali tidak memberikan informasi yang signifikan dalam analisis teks. Oleh karena itu, langkah ini melibatkan penghapusan tanda baca dari setiap token untuk membersihkan teks dari karakter yang tidak relevan.
  
- stopword removal
  Stopword adalah kata-kata umum yang sering muncul dalam teks namun tidak menyimpan informasi yang signifikan. Contoh stopwords dalam Bahasa Inggris termasuk "the", "and", "is", dan sebagainya. Proses ini melibatkan penghapusan stopwords untuk meningkatkan kualitas analisis teks.
  
- lemmatization
  Tujuan lemmatization adalah untuk menyederhanakan kata-kata sehingga variasi morfologis dari kata tidak mempengaruhi analisis teks. Proses ini membantu dalam mengatasi perbedaan bentuk kata yang sebenarnya memiliki makna yang sama.

Hasil dari preprocessing tersebut dapat dilihat dari gambar di bawah ini :

![image](https://github.com/RahmatPrakoso276/deploy-ml-project1/assets/79794844/29e026dc-bc15-46c9-bf55-cde7d6de226b)

5. Modelling

- tokenization
  Pada tahap ini kalimat dipecah menjadi kata. kata kata yang dipecah kemudian dilakukan indexing dan dimuat kedalam dictionary kata. jumlah maximum kata untuk dictionary adalah 5000 kata

- Padding
  Pada tahap ini dilakukan padding pada setiap sequence kalimat, hal ini dilakukan untuk memberikan input shape yang konsisten pada saat diinput ke model. jumlah panjang setiap sequence di set = 200 kata
   
Model yang digunakan pada project ini merupakan RNN. berikut adalah arsitekturnya:

![image](https://github.com/RahmatPrakoso276/deploy-ml-project1/assets/79794844/c05d1f79-a180-4383-97e1-af974141385e)

7. Evaluation
   
Hasil dari pelatihan dapat dilihat pada graf berikut:

![image](https://github.com/RahmatPrakoso276/deploy-ml-project1/assets/79794844/e3b7a60c-0a0e-421b-b154-bb6799a59258)

Metrik penelitian yang digunakan adalah metrik umum yang biasa digunkan untuk task klasifikasi yaitu accuracy. hasil evaluasi kinerja model diatas sebagai berikut :

![image](https://github.com/RahmatPrakoso276/deploy-ml-project1/assets/79794844/47d3b944-88a2-4927-a52f-5e4e717f6b3f)


## Project Flow Data Citra
1. Load Dataset Citra

Pada tahapan ini, data yang diperoleh diload kedalam program. Berikut merupakan contoh dari masing - masing citra dalam setiap kategori dataset.

![image](https://github.com/RahmatPrakoso276/deploy-ml-project1/assets/79794844/22d6b2b9-c9c0-45a8-bbb7-f968d5312e72)

3. Data Preprocessing and augmentation
   
Data augmentasi dilakukan untuk mendapat lebih banyak data pada pelatihan yang akan dilakukan, data yang diproleh dari augmentasi yang dilakukan pada project ini bersifat sintetis dengan begitu jumlah data     pada dataset tidak berubah. Adapun beberapa parameter dalam proses augmentasi yang dilakukan adalah: rescale=1./255, rotation_range=30, zoom_range=0.2, height_shift_range=0.2, horizontal_flip=True, fill_mode='nearest'. Hasil dari augmentasi dapat dilihat pada gambar dibawah:

![image](https://github.com/RahmatPrakoso276/deploy-ml-project1/assets/79794844/4e297932-d796-483b-8b1b-9982931cd18d)

5. Modelling
   
Model yang digunakan pada project ini merupakan DenseNet-169. Berikut merupakan summery model dari DenseNet-169:

![image](https://github.com/RahmatPrakoso276/deploy-ml-project1/assets/79794844/a3994381-b78e-4461-9976-165acffe3c61)

pada model tersebut, dilakukan fine tuning dengan melakukan unfreez pada 2 layer terakhir pada model, dengan begitu 2 layer terakhir akan ikut dilatih kembali. Berikut merupakan implementasi fine tuning pada model pre trained.

![image](https://github.com/RahmatPrakoso276/deploy-ml-project1/assets/79794844/f7d55de8-bacb-4098-8cf0-8c1f172bd152)

Setelah dilakuakn fine tuning pada model, model akan digabungkan dengan fully connected layer yang digunakan untuk memberikan hasil akhir klasifikasi machine learning yang dilakukan. Adapun beberapa layer dalam fully connected layer yang digunakan adalah, GlobalMaxPooling2D(), Dense(512, activation='relu'), Dropout(0.5), Dense(128, activation='relu'), Dropout(0.3), Dense(3, activation='softmax'). Adapun hasil akhir dari model yang digunakan setelah melalui preses fine tuning dan implementasi fully connected layer adalah sebagai berikut:

![image](https://github.com/RahmatPrakoso276/deploy-ml-project1/assets/79794844/ebe1baf7-e8fa-4d49-8e95-7918ccd319c6)

Setelah arsitektur machine learning dibuat, selanjutnyya adalah tahap pelatihan model. pada tahapan ini data dibangi menjadi 3 kategori yaitu data train, data test, dan juga data validation. setelah itu dilakukan pelatihan dengan data train sebagai bahan pelatihan dan data validation sebagai indikator penilaian. Pelatihan model dilakukan sebanyak 5 epoch pelatihan yang dapat dilihat pada gamabr dibawah ini:

![image](https://github.com/RahmatPrakoso276/deploy-ml-project1/assets/79794844/dfb37fab-1a54-4af1-96a6-d811fc5a6bb0)

7. Evaluation
   
Hasil dari pelatihan dapat dilihat pada graf berikut:

![image](https://github.com/RahmatPrakoso276/deploy-ml-project1/assets/79794844/57545df9-d7d5-44c6-84b6-679dc968e596)

Metrik penelitian yang digunakan adalah metrik umum yang biasa digunkan untuk task klasifikasi yaitu accuracy. hasil evaluasi kinerja model diatas sebagai berikut :

![image](https://github.com/RahmatPrakoso276/deploy-ml-project1/assets/79794844/ab24d08a-be5a-4b10-9c51-7e7606341232)


## Instalasi

[Petunjuk instalasi dan persyaratan sistem]

## Author
- Rahmat Prakoso

## Kontribusi
Dalam proyek ini, kontribusi sepenuhnya dilakukan oleh Author, mencakup pengembangan ide, implementasi, hingga dokumentasi proyek.

```bash
$ git clone https://github.com/RahmatPrakoso276/deploy-ml-project1
$ cd deploy-ml-project1
$ npm install
```
