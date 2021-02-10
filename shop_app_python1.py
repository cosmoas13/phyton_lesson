apple_price = 2
# Berikan 10 ke variable money
money = 10

input_count = input("Mau berapa apel?: ")
count = int(input_count)
total_price = apple_price * count

print("Anda akan membeli " + str(count) + " apel")
print("Harga total adalah " + str(total_price) + " dollar")

# Tambahkan control flow berdasarkan perbandingan
# antara money dan total_price

if money > total_price:
    print("Anda telah membeli " + str(count) + " apel")
    print("Uang Anda tinggal " + str(money - total_price) + " dollar")
elif money == total_price:
    print("Anda telah membeli " + str(count) + " apel")
    print("Dompet Anda Kosong")
else:
    print("Uang Anda tidak mencukupi")
    print("Anda tidak dapat membeli apel sebanyak itu")
