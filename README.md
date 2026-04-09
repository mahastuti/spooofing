# Data Analytics Competition FIND IT UGM 2026
> | Member of "jeruk pak bas"  | Profil |
> |------|--------|
> | Nalini Mahastuti Panunjul | 🔗 https://www.linkedin.com/in/mahastuti/ |
> | Dyah Ayu Nur Azizah | 🔗 https://www.linkedin.com/in/dyah-ayu-nur-azizah-5b428324a |
> | M. Iqbal Nurrifki | 🔗 https://www.linkedin.com/in/miqbalnurrifki |


## 📌 Deskripsi
Seiring dengan pesatnya perkembangan teknologi, sistem **<i>face recognition</i>** telah banyak diterapkan di berbagai sektor, seperti pembukaan kunci perangkat seluler, sistem absensi, verifikasi identitas pada layanan keuangan. Meskipun memberikan kemudahan dan efisiensi, sistem ini masih memiliki kerentanan terhadap ancaman keamanan, salah satunya adalah **<i>face spoofing</i>**.

<i>Face spoofing</i> merupakan bentuk serangan yang bertujuan untuk mengelabui sistem pengenalan wajah dengan memanfaatkan media visual, seperti:

- Foto cetak  
- Tampilan gambar pada layar  
- Representasi wajah lainnya  

Berbagai penelitian menunjukkan bahwa **<i>face spoofing</i>** memiliki tingkat keberhasilan yang cukup tinggi, terutama pada sistem yang belum dilengkapi dengan mekanisme **<i>liveness detection</i>** yang memadai.

## 🎯 Tujuan Kompetisi

Kompetisi ini berfokus pada pengembangan model yang mampu:

- Mengklasifikasikan wajah ke dalam **6 kelas berbeda**
- Mengidentifikasi berbagai bentuk **<i>spoofing attack</i>**
- Memiliki **<i>generalization</i>** yang baik pada kondisi dunia nyata
- Membangun model <i>computer vision</i> berbasis citra (**<i>image-based</i>**) yang <i>robust</i> terhadap variasi pencahayaan, sudut pengambilan dan jenis serangan  

## 📊 Dataset

Dataset terdiri dari citra wajah yang dibagi ke dalam **6 kategori utama**:

| Kategori         | Deskripsi |
|------------------|----------|
| **realperson**   | Wajah asli tanpa manipulasi |
| **fake_printed** | Serangan menggunakan foto cetak |
| **fake_screen**  | Serangan menggunakan tampilan layar (HP/monitor) |
| **fake_mask**    | Serangan menggunakan masker (3D/silikon) |
| **fake_mannequin** | Serangan menggunakan replika wajah (mannequin) |
| **fake_unknown** | Serangan lain di luar kategori yang telah didefinisikan |

---

## 📜 Notes

- Waktu babak penyisihan adalah 14 hari
- Batas submit adalah 3 submit per hari
- Submission output wajib: file submission sesuai format panitia.
- Tidak diperbolehkan menggunakan metadata/ data eksternal
- Tidak diperbolehkan menggunakan VLM, LLM  dan Generative AI lainnya untuk klasifikasi  
- Tidak diperbolehkan melakukan kerja sama antartim
- Diperbolehkan menggunakan lebih dari satu model machine learning
- Diperbolehkan menggunakan pretrained model (open-source saja) tanpa batasan parameter
- Menggunakan metrik Macro F1-score

## ⏳ Workflow
1. Definisikan permasalahan
2. Cleaning data
3. Explorasi data
4. Preprocessing data 
5. Training + Validation model 1
6. Training + Validation model 2
7. Training +  Validation model 3
8. Ensembling
9. Predict test data
10. Submit

## 📝 Petunjuk menjalankan notebook
1. Siapkan environment
- Install Python (≥ 3.8)
- Install dependencies:
```bash
pip install torch torchvision timm scikit-learn matplotlib seaborn optuna
```
2. Pastikan struktur data sudah sesuai
```bash
data/
  cropped/
  cropped_test/
  test/
  train/
```
3. Jalankan notebook secara berurutan
- Masuk ke folder notebook/
- Jalankan file berikut secara urut:
> 01_*.ipynb <br>
> 02_*.ipynb<br>
> 03_*.ipynb<br>
> 04_*.ipynb<br>
> ⚠️ Wajib dijalankan berurutan karena ada dependency antar notebook
4. (Opsional) gunakan GPU
```bash
device = "cuda" if torch.cuda.is_available() else "cpu"
```

## ✅ Result Summary
### <span style="color:green">A. Cleaning Data</span>
- Foto pada folder data belum tentu sudah tersortir sesuai kelasnya
> Solusi: Memindahkan secara manual terlebih dahulu ke dalam folder yang sesuai
- Cropping untuk meminimalisisr <i>noise</i> pada gambar
- Resize ke dalam ukuran yang sama, yaitu 224 x 224
- Menghilangkan gambar duplikat
- Fix file corrupt

### <span style="color:green">B. Exploratory Data</span>
- Overview dataset
- Data quality dan structure<br><br>
<b>Kesimpulan dari EDA:</b><br>
> 1. Data train didominasi oleh kelas fake (~73%) imbalance<br>
> 2. Format gambar didominasi oleh .jpg di train dan test<br>
> 3. Cropping tidak mengubah brightness secara signifikan, tetapi menurunkan contrast (lebih homogen)<br>
> 4. Distribusi RGB setelah cropping lebih terstruktur, menandakan fokus ke area wajah<br>
> 5. Antar kelas masih sangat overlap, sehingga sulit dipisahkan hanya dari brightness & contrast<br>
> 6. Tekankan augmentasi yang memperkaya tekstur dan artefak wajah, karena brightness/contrast tidak cukup membedakan kelas.

### <span style="color:green">C. Preprocessing Data
- Split data dengan komposisi 80% train dan 20% validation
- Augmentasi (training data only) difokuskan pada variasi tekstur dan kualitas citra:<br>
a. Horizontal flip secara acak (p=0.5)<br>
b. Rotasi ringan (±10°)<br>
c. Penyesuaian warna ringan menggunakan ColorJitter (brightness, contrast, saturation, hue kecil)<br>
d. Penyesuaian ketajaman (RandomAdjustSharpness) untuk variasi tekstur<br>
- Transformasi dasar:<br>
a. Konversi gambar ke tensor<br>
b. Normalisasi menggunakan mean dan std ImageNet<br>
- Validation set hanya menggunakan tensor + normalisasi (tanpa augmentasi)

### <span style="color:green">D. Modeling
1. Preprocess (augmentasi, split 90:10)
2. Hyperparameter tuning menggunakan Optuna dengan K-Fold Cross Validation
3. Pemilihan hyperparameter terbaik berdasarkan performa rata-rata
4. Training final model menggunakan seluruh data training
5. Ensemble model
6. Predict

## 🏆Evaluation & Suggestion:
- Best model:
- Skor final kaggle leaderboard: 
- Accuracy:<br>

> <b>Suggestion:
> xxxxx
