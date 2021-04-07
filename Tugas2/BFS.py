# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 16:50:04 2021

@author: Putri Nella
"""
#kode program BFS (Breadth First Search)
#contoh Peta
peta =  {'A':set(['B']),
         'B':set(['A','C','D']),
         'C':set(['B','E']),
         'D':set(['B','G','H']),
         'E':set(['C','F','G']),
         'F':set(['E']),
         'G':set(['D','E','I','J']),
         'H':set(['D','J']),
  'I':set(['G'])}
    

def bfs(graf, mulai, tujuan):
    queue = [[mulai]]
    visited = set()

    while queue:     
        # masukkan antrian paling depan ke variabel jalur
        jalur = queue.pop(0)

        # simpan node yang dipilih ke variabel state, misal jalur = C,B maka simpan B ke variabel state
        state = jalur[-1]

        # cek state apakah sama dengan tujuan, jika ya maka return jalur
        if state == tujuan:
            return jalur
        # jika state tidak sama dengan tujuan, maka cek apakah state tidak ada di visited
        elif state not in visited:
            # jika state tidak ada di visited maka cek cabang
            for cabang in graf.get(state, []): #cek semua cabang dari state
                jalur_baru = list(jalur) #masukkan isi dari variabel jalur ke variabel jalur_baru
                jalur_baru.append(cabang) #update/tambah isi jalur_baru dengan cabang
                queue.append(jalur_baru) #update/tambah queue dengan jalur_baru

            # tandai state yang sudah dikunjungi sebagai visited
            visited.add(state)

        #cek isi antrian
        isi = len(queue)
        if isi == 0:
            print("Tidak ditemukan")
