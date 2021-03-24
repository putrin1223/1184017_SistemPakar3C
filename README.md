# 1184017_SistemPakar3C
# BFS
 Breadth-first search adalah algoritma yang melakukan pencarian secara melebar yang       
 mengunjungi simpul secara preorder yaitu mengunjungi suatu simpul kemudian mengunjungi 
 semua simpul yang bertetangga dengan simpul tersebut terlebih dahulu. Selanjutnya, 
 simpul yang belum dikunjungi dan bertetangga dengan simpulsimpul yang tadi dikunjungi, 
 demikian seterusnya. Jika graf berbentuk pohon berakar, maka semua simpul pada aras d dikunjungi 
 lebih dahulu sebelum simpul-simpul pad aras d+1.
  Algoritma ini memerlukan sebuah antrian q untuk menyimpan simpul yang telah dikunjungi. 
  Simpulsimpul ini diperlukan sebagai acuan untuk mengunjungi simpul-simpul yang bertetanggaan dengannya. 
  Tiap simpul yang telah dikunjungu masuk ke dalam antrian hanya satu kali. Algoritma ini juga membutuhkan 
  table Boolean untuk menyimpan simpul yang te lah dikunjungi sehingga tidak ada simpul yang dikunjungi lebih dari satu kali.
  
  # DFS
   Algoritma DFS (Depth First Search) adalah salah satu algoritma yang digunakan untuk pencarian jalur. 
   Contoh yang dibahas kali ini adalah mengenai pencarian jalur yang melalui semua titik. 

  Algoritma ini mirip dengan Algoritma BFS (Breadth First Search) yang sudah dijelaskan sebelumnya. 
  Jika Algoritma BFS (Breadth First Search) melakukan perhitungan secara      terurut dari urutan pertama sampai urutan terakhir,
  maka algoritma ini melakukan kebalikannya, yaitu melakukan perhitungan secara terurut dari urutan terakhir. 
  Setelah menghabiskan semua kemungkinan dari titik terakhir, barulah mundur ke titik-titik sebelumnya sampai pada titik pertama.
