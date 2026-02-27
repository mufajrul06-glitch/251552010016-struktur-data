#database pengguna
user = {
    "fadhil": "password123",
    "anya": "admin456",
    "budi": "dev789"    
}

print("=== login manual ===")
input_username = input("Masukkan username: ")
input_password = input("Masukkan password: ")

if input_username in user and user[input_username] == input_password:
    print(f"Login {input_username}: BERHASIL")
else:
    print(f"Login {input_username}: GAGAL - username atau password salah")