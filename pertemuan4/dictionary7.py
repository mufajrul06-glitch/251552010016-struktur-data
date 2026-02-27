user = {"name": "ahmad", "age": 25}

#menggunakan get agar aman dari keyError
email =user.get("email", "email belum tersedia")
print(email)

#menamahkan key jika belum ada dengan setdeafult
user.setdefault("email", "ahmad@example.com")

#update data
user.update({"age": 26, "role": "Developer"})

#menghapus key
age = user.pop("age")

#menampilkan semua key dan values
print(user.keys())
print(user.values())

#menyalin dictionary
user_copy = user.copy()
print(user_copy)