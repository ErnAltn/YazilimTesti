from faker import Faker #sahte veri üretme kütüphanesi
fake = Faker()
print(f"Name: {fake.name()}") #sahte isim üretme
print(f"Address: {fake.address()}") #sahte adres üretme