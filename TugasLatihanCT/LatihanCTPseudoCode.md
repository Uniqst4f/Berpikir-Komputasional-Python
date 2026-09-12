# SOAL 1

![Mengisi Kotak](./Assets/Soal1.png)

## Observasi
1. Jika kita memerhatikan gambar di soal, jumlah bola yang tersedia 12 buah. Sementara itu, jumlah kotak yang tersedia hanya 11. Artiyna jumlah maksimal bola yang kita dapat masukkan hanyalah X <= 11. 
2. Kita bisa masukkan bola dalam kotak dengan 2 strategi utama. Pertama masukan sesuai dengan ukuran mereka, bola kecil akan dimasukkan ke kotak kecil dan seterusnya. Kedua kita menggunakan strategi _Greedy_, dimana saat kita temukan kotak yang lebih besar daribola yang kita ambil saat ini langsung dimasukkan.

Kalau menggunakan strategi _greedy_, kita bisa memasukkan 10 bola. Jadi kita harus membuat algoritma _greedy_

## Pseudocode dan Flowchart

 ```pseudocode
Mencari_Jumlah_Bola_Maksima(Bola-bola, Kotak-kotak) {

Untuk setiap anggota bola dari bola-bola cek setiap kotak dari Kotak-kotak {
                Jika ukuran kotak >= ukuran bola, masukan bola  
                Jumlah bola + 1

                Jika tidak, cek kotak selanjutnya
  }

Keluarkan(Jumlah Bola)

}
 ```

![Flowchart Soal 1](./Assets/FlowChartMenghitungBola.png)

# SOAL 2

![Soal 2](./Assets/Soal2.png)

## Observasi 
Bayangkan jalur yang dapat dilalui oleh kanguru sebagai matriks. Dimana setiap dinding di representasikan dengan angka 0 (tidak ada bata), 1 (1 bata), 2 (2 bata), 3 (3 bata), dan # (air) tidak bisa dilalui


 ```
0 1 0 1 0 1 0 1 0
1 # 2 # 3 # 3 # 1
0 3 0 1 0 1 0 2 0
3 # 3 # 2 # 2 # 1
0 1 0 2 0 1 0 2 0
2 # 2 # 1 # 3 # 3
0 3 0 2 0 2 0 1 0
3 # 3 # 2 # 2 # 2
0 1 0 1 0 1 0 3 X
```



Dimana X adalah titik akhir.

Kita bisa menemukan jumlah lompatan minimal dengan menggunakan algoritma BFS (Breadth First Search). BFS akan bergerak dari level ke level mengecek semua arah kemudian mengeluarkan langkah minimal.
Mengapa kita menggunakan BFS? BFS secara metematika akan mengelurkan nilai terkecil saat menemukan path dari titik mulai ke titik akhir.

## Pseudocode dan Flowchart

 ```pseudocode
Cari_Lompatan_Minimal (Matriks Peta Kanguru) {

  MatriksJarak = Matriks 2D sebesar Matriks Peta Kanguru yang diisi -1
  q = queueu kosong

  Masukan titik awal (0, 0) ke q
  MatriksJarak[0][0] = 0

  ArahLompatHorizontal = [Kiri, Kanan, 0, 0]
  ArahLompatVertikal = [0,0, Kiri, Kanan]

  Selama q belum kosong {

  Ambil titik saat ini dari q
  
  Jika X ditemukan {
    keluarkan(MatriksJarak[X saat ini][Y saat ini])
  }

  Untuk i dari 0 sampai 3 {
  
  X Selanjutnya = X saat ini + ArahLompatHorizontal[i]
  Y Selanjutnya = Y saat ini + ArahLompatVertikal[i]

  Koordinat_Batu_yang_Dilompat_X = X saat ini + (ArahLompatHorizontal[i]/2)
  Koordinat_Batu_yang_Dilompat_Y = Y saat ini + (AraahLompatVertikal[i]/2)

  Jika Matriks Peta Kanguru [Koordinat_Batu_yang_Dilompat_X][Koordinat_Batu_yang_Dilompat_Y] == 1 batu atau 2 batu
      {
          Jika Matriks Peta Kanguru belum dikunjungi
            {
                MatriksJarak[X Selanjutnya][Y Selanjutnya] = MatriksJarak[X saat ini][Y saat ini] + 1
            }

        }

    }
  }
}
 ```

![Flowchart Soal 2](./Assets/mermaid-diagram-1789149284181.png)

# SOAl 3

![Soal 3](./Assets/Soal3.png)

## Observasi
Dalam soal ini kita hanya perlu mengkategorikan sebuah input atau objek untuk masuk ke sebuah penampungan. Untuk memudahkan pengerjaan soal, saya akan menggunakan array sebagai penampung benda. Dari sana kita hanya perlu membuat fungsi yang memfilter balok kayu dan memasukkannya ke array benar.

Perhatikan bahwa setiap ciri dari kayu hanya memiliki 2 kemungkinan. Di komputer kita dapat memodelkan ini sebagai true and false. Jadi misalnya 2 cincin dalam menjadi true dan 3 cincin dalam false.
Kita hanya perlu membuat 4 array yang memiliki 3 input true atau false untuk setiap ciri.

Asumskikan jenis yang memiliki jumalah paling sedikit dalam kategorinya adalah true.
Ex : Cincin 2 (true), Cincin 3 (false)

Maka kita bisa melihat kategorisasi setiap array berdasarkan gambar sebagai berikut :

| Cincin Dalam | Garis Kulit | Jumlah Simpul | Array |
|--------------|-------------|---------------|-------|
| True         | True        | True          | A     |
| False        | False       | False         | D     |
| True         | False       | False         | D     |
| True         | True        | False         | B     |
| False        | True        | False         | B     |
| True         | False       | True          | C     |
| False        | False       | True          | C     |
| False        | True        | True          | A     |

Perhatikan bahwa setiap garis kulit dan jumlah simpul yang sama dalam sebuah objek kayu (Ex : GK (true), JS (true)) masuk ke dalam array yang sama. Apa artinya? Cincin dalam tidak berpengaruh sama sekali, maka dari itu kita bisa menyerdehanakan tabel menjadi :

| Garis Kulit (Bit 1) | Jumlah Simpul (Bit 0) | Binary | Integer | Target Array |
| :--- | :--- | :--- | :--- | :--- |
| False | False | `00` | `0` | **D** |
| False | True | `01` | `1` | **C** |
| True | False | `10` | `2` | **B** |
| True | True | `11` | `3` | **A** |

## Pseudocode dan Flowchart
```Pseudocode
Penyortir_Balok(Balok Kayu) {

  Indeks_Array = (BalokKayu.Garis_Kulit di ubah ke biner dan di shift ke kiri) + (BalokKayu.Jumlah_Simpul diubah ke biner)

  Kategorisasi_Array = [Array D, Array C, Array B, Array A]

  Masukkan Balok Kayu dalam array Kategorisasi_Array[Indeks_Array] 

}
```

![Flowchart Soal 3](./Assets/FlowChartSoal3.png)

# SOAL 4

![Soal 4](./Assets/Soal4.png)

## Observasi

Perhatikan dalam tabel kode sususanannya seperti sebuah matriks. Kita bisa memetakan tabel tersebut menjadi sebuah matriks 3X9. Dalam program kita hanya perlu merepresntasikan setiap string menjadi sebuah karakter misalnya kepala bulat dan rambut runcing adalah A. Gambar kepala adalah koordinat X dan angka adalah Y Setelah itu, kita tinggal memasukan semua input dan mendapat pesan rahasia. 

## Pseudocode dan Flowchart
```pseudocode
Untuk semua gambar dari gambar-gambar {
    Translasi_Kode(Gambar_Kepala, Gambar_Angka, Tabel_Kode_Dalam_Matriks, Tabel_Translasi_Gambar_Ke_Angka) {

        Koordinat_X = Tabel_Translasi_Gambar_Ke_Angka[Gambar_Kepala];
        Koorinat_Y = Tabel_Translasi_Gambar_Ke_Angka[Gambar_Angka];

        Keluarkan(Tabel_Kode_Dalam_Matriks[Koordinat_X][Koorinat_Y]) 

  }
}
```

![Flowchart Soal 4](./Assets/FlowChartSoal4.png)

# Soal 5
![Soal 5](./Assets/Soal5.png)

## Observasi

1. Untuk menyelesaikan soal ini, kita harus kembali menggunakan algoritma _greedy_, dimana setiap kali ada jalur pesawat yang masih kosong (selang waktu >15 menit), jalur pesawat tersebut langsung digunakan oleh pesawat yang datang. Jalur yang dipakai akan disimpan dalam array Jalur_Pesawat_Terpakai.
2. Kita harus memiliki standar waktu yang sama untuk setiap jam datang. Dalam soal aku akan menghitung jam dengan hitungan setelah tengah malam. Jadi misalnya 07:00 berarti 420 menit setelah tengah malam.

| Waktu Kedatangan | Jalur Pesawat Terpakai | Cek Jalur Pendaratan yang Ada | Status `assigned` | Tindakan yang Diambil | Jalur Pesawat Terpakai Setelah Tindakan |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **07:00** (420 menit) | `[]` (Kosong) | Belum ada jalur | Tetap `false` | Belum ada jalur -> **Buka Jalur 1** | `[420]` |
| **07:03** (423 menit) | `[420]` | Jalur 1: 423 - 420 = 3 menit (<= 15 menit, jalur masih sibuk) | Tetap `false` | Semua sibuk -> **Buka Jalur 2** | `[420, 423]` |
| **07:12** (432 menit) | `[420, 423]` | Jalur 1: 432 - 420 = 12 menit (sibuk)<br/>Jalur 2: 432 - 423 = 9 menit (sibuk) | Tetap `false` | Semua sibuk -> **Buka Jalur 3** | `[420, 423, 432]` |
| **07:18** (438 menit) | `[420, 423, 432]` | Jalur 1: 438 - 420 = 18 menit (> 15, jalur bebas) | Berubah ke `true` | Pakai lagi jalur 1 (ubah ke 438) | `[438, 423, 432]` |
| **07:20** (440 menit) | `[438, 423, 432]` | Jalur 1: 440 - 438 = 2 menit (sibuk)<br/>Jalur 2: 440 - 423 = 17 menit (> 15, jalur bebas) | Berubah ke `true` | Pakai lagi jalur 2 (ubah ke 440) | `[438, 440, 432]` |
| **07:21** (441 menit) | `[438, 440, 432]` | Jalur 1: 441 - 438 = 3 menit (sibuk)<br/>Jalur 2: 441 - 440 = 1 menit (sibuk)<br/>Jalur 3: 441 - 432 = 9 menit (sibuk) | Tetap `false` | Semua sibuk -> **Buka Jalur 4** | `[438, 440, 432, 441]` |

## Pseudocode dan Flowchart
```Pseudocode

Ubah_Ke_Menit_dari_Tengah_Malam(waktu) {
    Keluarkan (jam * 60) + menit
}

Hitung_Minimal_Jalur(Daftar_Penerbangan) {
    
  Daftar_Menit = Array  

  Untuk setiap waktu dalam Daftar_Penerbangan {
        Daftar_Menit.tambah(Ubah_Ke_Menit_dari_Tengah_Malam(waktu))
  }
    Urutkan(Daftar_Menit)
    
    Jalur_Pesawat_Terpakai = Array
    
    Untuk setiap kedatangan dalam Daftar_Menit {
        ditemukan_jalur = False
        
        Untuk semua Jalur_Pesawat_Terpakai{
            Jika (kedatangan - Jalur_Pesawat_Terpakai[i] > 15) {
                Jalur_Pesawat_Terpakai[i] = kedatangan
                ditemukan_jalur = True
                break
            }
        }
        
        Jika Tidak ditemukan_jalur{
            Jalur_Pesawat_Terpakai.tambah(kedatangan)
        }
  }
    Kembalikan Panjang(Jalur_Pesawat_Terpakai)
}
```

![Flow Chart Soal 5](./Assets/FlowChartSoal5.png)
