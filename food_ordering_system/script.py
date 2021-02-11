from menu_item import MenuItem

menu_item1 = MenuItem("Roti Lapis", 5)
menu_item2 = MenuItem("Kue Coklat", 4)
menu_item3 = MenuItem("Kopi", 3)
menu_item4 = MenuItem("Jus Jeruk", 2)

menu_items = [menu_item1, menu_item2, menu_item3, menu_item4]

index = 0

for menu_item in menu_items:
    print(str(index) + ". " + menu_item.info())
    index += 1

print("--------------------")

order = int(input("Masukkan nomor menu: "))
selected_menu = menu_items[order]
print("Item yang di pilih: " + selected_menu.name)

# Terima input dari console, dan Berikan input ke variable count
count = int(input("Jumlah pesanan (diskon 10% untuk 3 atau lebih): "))

# Panggil method get_total_price
result = selected_menu.get_total_price(count)

# Cetak 'Total harga adalah $____'
print("Total harga adalah $" + str(result))

# ----------------------------------------------------------------------------

# # Import class MenuItem dari menu_item.py
# from menu_item import MenuItem

# # Tambahkan 'Roti Lapis' dan 5 sebagai argument
# menu_item1 = MenuItem("Roti Lapis", 5)

# # Hapus dua baris di bawah tanpa menggunakan __init__
# # name dan price harus dideklarasikan dengan variable instance
# # menu_item1.name = 'Roti Lapis'
# # menu_item1.price = 5

# print(menu_item1.info())

# # Panggil method get_total_price
# result = menu_item1.get_total_price(4)

# # Cetak 'Total harga adalah $____'
# print("Total harga adalah $" + str(result))
