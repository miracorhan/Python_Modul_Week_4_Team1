from datetime import datetime, timedelta 
import json

kontrol_file ="tracking.json"
MEMBERS_FILE = "user.json"
BOOKS_FILE = "kitap.json"

# Kitapları yükleme
def load_books():
    try:
        with open(BOOKS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Kitap dosyası bulunamadı.")
        return []
    except json.JSONDecodeError:
        print("Kitaplar yüklenirken hata oluştu.")
        return []

# Üyeleri yükleme
def load_members():
    try:
        with open(MEMBERS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Üye dosyası bulunamadı.")
        return {}
    except json.JSONDecodeError:
        print("Üyeler yüklenirken hata oluştu.")
        return {}

# Kitap ödünç verme
def add_bookgiving():
    members = load_members()
    books = load_books()

    if not books:
        print("Mevcut kitap yok.")
        return

    # Üye bilgilerini alma
    member_id = input("Kitap ödünç vermek için üye ID'sini girin: ")
    if member_id not in members:
        print("Üye bulunamadı.")
        return

    # Kitapları listeleyerek seçim yapma kolaylasir.
    print("Mevcut Kitaplar:")
    for book in books:
        print(f"Barkod: {book['Barkod']}, Başlık: {book['Kitap_Adi']}")

    book_barkod = input("Ödünç vermek için kitap barkodunu girin: ")

    # Seçilen kitabın barkodunu doğrula
    selected_book = None
    for book in books:
        if str(book['Barkod']) == book_barkod:
            selected_book = book
            break

    if not selected_book:
        print("Kitap bulunamadı.")
        return

    # Kitap ödünç alma işlemi
    current_date = datetime.now()
    return_date = current_date + timedelta(weeks=2)  # 2 hafta sonra teslim tarihi
    new_entry = {
        "member_id": member_id,
        "member_name": members[member_id]["adi"],
        "book_barkod": book_barkod,
        "book_name": selected_book["Kitap_Adi"],
        "lend_date": current_date.strftime('%Y-%m-%d'),
        "return_date": return_date.strftime('%Y-%m-%d')
    }

    # Mevcut tracking.json dosyasını yükle
    try:
        with open(kontrol_file, "r") as file:
            tracking_data = json.load(file)
            # Eğer dosya bir sözlükse, listeye dönüştür
            if isinstance(tracking_data, dict):
                tracking_data = [tracking_data]
    except FileNotFoundError:
        tracking_data = []  # Eğer dosya yoksa boş bir liste başlat
    except json.JSONDecodeError:
        print("Tracking dosyası okunamadı. Yeni dosya oluşturulacak.")
        tracking_data = []

    # Yeni girdiyi ekle
    tracking_data.append(new_entry)

    # Dosyayı güncelle
    with open(kontrol_file, "w") as file:
        json.dump(tracking_data, file, indent=4)


    print(f"Kitap {members[member_id]['adi']} adlı üyeye ödünç verildi.")
    print(f"Kitap, şu tarihe kadar geri verilmelidir: {return_date.strftime('%Y-%m-%d')}")


'''

def return_bookgiving():

'''


# Ödünç verilen kitapları listeleme
def tracking_bookgiving():
    try:
        # Tracking.json dosyasını oku
        with open(kontrol_file, "r") as file:
            tracking_data = json.load(file)

        # Eğer dosya boşsa bilgi ver
        if not tracking_data:
            print("Henüz ödünç verilmiş bir kitap bulunmuyor.")
            return

        # Üye bilgilerini members dosyasından al
        members = load_members()

        # Ödünç verilen kitapları listele
        print("Ödünç Verilen Kitaplar:")
        for entry in tracking_data:
            member_name = members.get(entry['member_id'], {}).get("adi", "Bilinmiyor")  # Üye adını members dosyasından al
            print(
                f"Üye Adı: {member_name}, "
                f"Kitap Adı: {entry['book_name']}, "
                f"Barkod: {entry['book_barkod']}, "
                f"Verilme Tarihi: {entry['lend_date']}, "
                f"Teslim Tarihi: {entry['return_date']}"
            )

    except FileNotFoundError:
        print("Tracking dosyası bulunamadı.")
    except json.JSONDecodeError:
        print("Tracking dosyası okunamadı.")

