# Database pengguna sederhana
users = {
"fadhli": "password123",
"Anya": "admin456",
"budi": "dev789"
}
# Login check
username = "fadhli"
password = "password123"
if username in users and users[username] == password:
    print("Login berhasil!")
else:
    print("Username atau password salah.")