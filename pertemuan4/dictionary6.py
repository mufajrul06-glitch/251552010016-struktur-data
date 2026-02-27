## Aplikasi Lain: Data Inventory
inventory = {
"laptop": 10,
"mouse": 25,
"keyboard": 15
}

# Menambahkan stok baru
inventory["monitor"] = 8

# Mengurangi stok
inventory["laptop"] = 2
print(inventory)

if barang in inventory: # pyright: ignore[reportUndefinedVariable]
    print(f"Stok {barang}: {inventory[barang]}")