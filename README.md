# Web App implement ML Models

Proyek ini adalah implementasi aplikasi web yang memanfaatkan kekuatan berbagai model pembelajaran mesin untuk melakukan prediksi pada berbagai jenis data, termasuk data tabular, teks, dan citra. Dengan menggunakan Flask sebagai framework utama, proyek ini bertujuan untuk memberikan antarmuka yang intuitif dan mudah digunakan bagi pengguna untuk menerapkan model ML pada data mereka.

## Daftar Isi

- [Deskripsi Proyek](#Web-App-implement-ML-Models)
- [Dataset](#WOverview-Dataset)
- [Fitur Utama](#Fitur-Utama)
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
