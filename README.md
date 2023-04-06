# Python Project Pacman - Super Cashier

## Objective

## Requirements

| Nama | Type | Input | Output | Note |
| -- | -- | -- | -- | -- | 
| Discount | Class | `min_price` (int) <br> `discount` (int)|  |  |
| Transaction | Class | `username` <br> `order_detail` | `transaction_id` |  |
| `add_item()` | Method in Transaction | `item_name` (str) <br> `quantity` (int) <br> `price_per_item` (int) |  |  |
| `update_item_name()` | Method in Transaction | `item_name` (str) <br> `new_item_name` (str) |  |  |
| `update_item_qty()` | Method in Transaction | `item_name` (str) <br> `new_quantity` (int) |  |  |
| `update_item_price()` | Method in Transaction | `item_name` (str) <br> `new_item_price` (int) |  |  |
| `delete_item()` | Method in Transaction | `item_name` (str) |  | Ketika menghapus nama item maka quantity dan price per item juga terhapus |
| `reset_transaction()` | Method in Transaction |  |  | Menghapus semua item yang ada pada transaksi yang sedang berlangsung |
| `check_order()` | Method in Transaction |  | `item_name` (str) <br> `quantity` (int) <br> `price_per_item` (int) <br> `total_per_item` (int) | Dalam bentuk table |
| `total_price()` | Method in Transaction |  | `subtotal` (int) <br> `total_discount` (int) <br> `total` (int) | `Subtotal` : Total belanja sebelum discount <br> `Total` : Total belanja setelah diskon (nominal yang harus dibayarkan) |


## Flowchart
![Flowchart  Python Project Pacman - Super Cashier](https://user-images.githubusercontent.com/61444164/229751369-656600f5-7440-4304-b416-a5a6265a118b.jpg)
