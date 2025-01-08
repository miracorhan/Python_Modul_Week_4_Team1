import json

FILE_NAME = "user.json"

def load_members():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}


def save_members(members):
    with open(FILE_NAME, "w") as file:
        json.dump(members, file, indent=4)

# Üye ekleme
def add_member():
    members = load_members()
    member_id = input("Üye ID'sini girin: ")
    if member_id in members:
        print("Bu ID ile zaten bir üye var.")
        return
    name = input("Üye adini girin: ")
    phone = input("Üye telefonunu girin: ")
    address = input("Üye adresini girin: ")

    members[member_id] = {
        "adi": name,
        "telefon": phone,
        "adres": address
    }
    save_members(members)  # Dosyaya kaydet
    print(f"{name} kişisi basariyla eklendi. Toplam üye sayisi: {len(members)}")

def list_members():
    members = load_members()
    if not members:
        print("Henüz kayıtlı üye yok.")
    else:
        print(f"\nToplam Üye Sayisi: {len(members)}")
        print("\nÜye Listesi:")
        for member_id, member in members.items():
            print(f"ID: {member_id}, Adi: {member['adi']}, Telefon: {member['telefon']}, Adres: {member['adres']}")

def search_member():
    members = load_members()
    search_term = input("Aramak istediğiniz üye ID'sini girin: ")
    found = False

    for member_id, member in members.items():
        if search_term == member_id:
            print("\nBulunan Üye:")
            print(f"ID: {member_id}, Adi: {member['adi']}, Telefon: {member['telefon']}, Adres: {member['adres']}")
            found = True
            break

    if not found:
        print("Aranan üye bulunamadı.")


def delete_member():
    members = load_members()
    member_id = input("Silmek istediğiniz üye ID'sini girin: ")
    if member_id in members:
        deleted_member = members.pop(member_id)
        save_members(members)
        print(f"{deleted_member['adi']} kişisi başariyla silindi. Toplam üye sayisi: {len(members)}")
    else:
        print("Bu ID ile kayitli bir üye bulunamadi.")
