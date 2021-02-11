class MenuItem:
    def info(self):
        # Cetak dengan format '____: $____'
        print(self.name + ":$" + str(self.price))


menu_item1 = MenuItem()

menu_item1.name = "Roti Lapis"
print(menu_item1.name)

# Tentukan price menu_item1 ke 5
menu_item1.price = 5

# Cetak price dari menu_item1
print(menu_item1.price)

# Buat instance dari class MenuItem
menu_item2 = MenuItem()

# Tetapkan name milik menu_item2 ke 'Kue Coklat'
menu_item2.name = "Kue Coklat"

# Cetak nama dari menu_item2
print(menu_item2.name)

# Tetapkan price dari menu_item2 ke 4
menu_item2.price = 4

# Cetak price dari menu_item2
print(menu_item2.price)
