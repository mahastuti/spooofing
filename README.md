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
5. Training model 1
6. Training model 2
7. Metrik evaluasi
8. Predict test data
9. Submit


## ✅ Result Summary
### <span style="color:green">A. Cleaning Data</span>
- Foto pada folder data belum tentu sudah tersortir sesuai kelasnya
> Solusi: Memindahkan secara manual terlebih dahulu ke dalam folder yang sesuai
- Cropping untuk meminimalisisr <i>noise</i> pada gambar
- Resize ke dalam ukuran yang sama, yaitu 224 x 224
- Menghilangkan gambar duplikat
- Fix file corrupt

### <span style="color:green">B. Exploratory Data</span>
- overview dataset
- data quality dan structure<br><br>
<b>Kesimpulan dari EDA:</b><br>
> 1. data train didominasi oleh kelas fake (~73%) imbalance<br>
> 2. format gambar didominasi oleh .jpg di train dan test<br>
> 3. cropping tidak mengubah brightness secara signifikan, tetapi menurunkan contrast (lebih homogen)<br>
> 4. distribusi RGB setelah cropping lebih terstruktur, menandakan fokus ke area wajah<br>
> 5. antar kelas masih sangat overlap, sehingga sulit dipisahkan hanya dari brightness & contrast<br>
> 6. tekankan augmentasi yang memperkaya tekstur dan artefak wajah, karena brightness/contrast tidak cukup membedakan kelas.

### <span style="color:green">C. Preprocessing Data
- Split data dengan komposisi 80% train dan 20% validation
- Normalization
- Preprocessing
- Augmentation

### <span style="color:green">D. Model
halo
### <span style="color:green">E. Tuning
halo

## 🏆 Evaluation

