# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 07:54:48 2021

@author: Quina
"""

print(" @@@    @   @  @@@  @    @      @@")
print("@   @   @   @   @   @@   @     @  @")
print("@ @ @   @   @   @   @ @  @    @@@@@@")
print("@   @   @   @   @   @  @ @   @      @")
print(" @@@ @  @ @ @  @@@  @    @  @        @")

print("-----------DERET FIBONACCI------------")
jumlah = int(input("masukan jumlah bilangan : "))
bil1 = int(input("masukan bilangan pertama : "))
bil2 = int(input("masukan bilangan kedua : "))
hitung = 0
while hitung < jumlah:
    print(bil1)
    angka = bil1 + bil2
    bil1 = bil2
    bil2 = angka
    hitung += 1