# -*- coding: utf-8 -*-
"""[Python Code] Python Project Pacman - Super Cashier.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19X_XVEnowaWVrC_Kr-d8qFbpljVpBRuG
"""

import pandas as pd
from dataclasses import dataclass
from tabulate import tabulate

import random #for random list or tupple
import string #for generate string

@dataclass
class Discount :
  text_discount : str
  min_price : int
  disc : int

  def __init__(self, text_discount, min_price, disc):
    self.text_discount = text_discount
    self.min_price = min_price
    self.disc = disc

list_disc = [Discount('Selamat Anda mendapatkan discount 10%', 500_000,0.1),
             Discount('Selamat Anda mendapatkan discount 8%', 300_000,0.08),
             Discount('Selamat Anda mendapatkan discount 5%', 200_000,0.05),
]

#untuk mengetes apakah class Discount yang dibuat sudah benar

subtotal= 599_000

for discount in list_disc:
  if subtotal >= discount.min_price :
    total = subtotal * (1 - discount.disc)
    print(total)
    break
else :
  print("Test")

class Transaction:

  __list_of_transaction_id = {}

  def __init__(self, username) :
    self.username = username
    self.transaction_id = ''.join((random.choice(string.ascii_lowercase) for x in range(4))) + self.username
    self.__list_of_transaction_id[self.username] = self.transaction_id
    self.order_detail = {}
  
  #untuk menambahkan item
  def add_item(self, item_name, quantity, price_per_item) :
    if type(quantity) != int :
      print("Masukan berapa jumlah barang yang dibeli dalam bentuk angka")
    if type(price_per_item) != int :
      print("Masukan harga barang yang dibeli dalam bentuk angka")
    else :
      total_per_item = quantity * price_per_item
      detail_item = {item_name : [quantity, price_per_item, total_per_item]}
      self.order_detail.update(detail_item)

  #untuk mengganti nama product
  def update_item_name(self, item_name, new_item_name):
    self.order_detail[new_item_name] = self.order_detail.pop(item_name)
  
  #untuk mengganti jumlah product yg dibeli
  def update_item_qty(self, item_name, new_quantity):
    self.order_detail[item_name][0] = new_quantity
    self.order_detail[item_name][2] = new_quantity * self.order_detail[item_name][1]

  #untuk mengganti harga product
  def update_item_price(self, item_name, new_price):
    self.order_detail[item_name][1] = new_price
    self.order_detail[item_name][2] = new_price * self.order_detail[item_name][0]
  
  #untuk menghapus 1 item
  def delete_item(self, item_name):
    self.order_detail.pop(item_name)

  #untuk mengecek order
  def check_order(self):
    headers = ["Item Name", "Quantity", "Price Per Item", "Total Per Item"]
    print(tabulate([[x,] + y for x, y in self.order_detail.items()], headers=headers))
  
  #untuk mereset cart
  def reset_transaction(self) :
    self.order_detail.clear()

  #untuk menampilan total price dengan Discount class
  def total_price(self):
    subtotal = 0
    for item_name in self.order_detail :
      subtotal += self.order_detail[item_name][2]

    discount = 0
    for disc in list_disc: 
      if subtotal >= disc.min_price : 
        discount = subtotal * disc.disc
        text = disc.text_discount
        break
    else :
      discount = 0 
      kurang = 200000 - subtotal
      text = f"Anda kurang Rp. {kurang} untuk mendapatkan discount min. 5%"

    total = subtotal - discount
    print(f"{text} \nSubtotal = Rp. {subtotal} \nDiscount = Rp. {discount:g}\nTotal = Rp. {total:g}")