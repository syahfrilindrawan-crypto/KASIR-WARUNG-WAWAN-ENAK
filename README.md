# 🧾 Kasir Warung Wawan Enak (WWE)

Aplikasi kasir sederhana berbasis GUI menggunakan Python (`tkinter`) dengan fitur login, pencatatan pesanan, dan cetak nota.

---

## 🚀 Fitur Utama

* 🔐 Login & Register (data disimpan di JSON)
* 🍽️ Pilihan menu makanan & minuman
* ➕ Input jumlah pesanan
* 🧾 List pesanan (real-time)
* ❌ Hapus pesanan
* 💰 Total harga otomatis
* 🖨️ Cetak nota ke file `.txt`

---

## 🛠️ Teknologi yang Digunakan

* Python 3
* Tkinter (GUI)
* JSON (penyimpanan data akun)
* File handling (nota.txt)

---

## 📂 Struktur Project

```
kasir-warung/
│
├── main.py
├── akun.json
└── README.md
```

---

## ▶️ Cara Menjalankan

1. Pastikan Python sudah terinstall
2. Jalankan file:

```
python main.py
```

---

## 🔑 Default Login

Jika file `akun.json` belum ada, otomatis dibuat dengan akun:

* Username: `admin`
* Password: `123`

---

## 🧠 Cara Kerja Aplikasi

1. User login / register
2. Masuk ke halaman kasir
3. Pilih menu → input jumlah
4. Pesanan masuk ke list
5. Total harga dihitung otomatis
6. Klik "Cetak Nota" → file `nota.txt` dibuat

---

## 📸 Screenshot (Opsional)

Tambahkan screenshot di sini untuk memperjelas tampilan aplikasi.

---

## ⚠️ Catatan

* Data akun masih sederhana (belum terenkripsi)
* Belum menggunakan database (masih JSON)
* Belum ada fitur edit pesanan

---

## 📌 Pengembangan Selanjutnya

* Tambah database (SQLite / MySQL)
* UI lebih modern
* Fitur edit pesanan
* Export ke PDF
* Multi user role (admin/kasir)

---

## 👤 Author

**Mochamad Syahfril Indrawan**
Learning Python & Fullstack Development 🚀
