import json
import os

# JSON dosya yolu
FILE_PATH = "kitap.json"

def load_books():
    """Kitap listesini JSON dosyasından yükler."""
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r", encoding="utf-8") as file:
            return json.load(file)
    return []

def save_books(books):
    """Kitap listesini JSON dosyasına kaydeder."""
    with open(FILE_PATH, "w", encoding="utf-8") as file:
        json.dump(books, file, ensure_ascii=False, indent=4)

def list_books():
    """Kitapları listeler."""
    books = load_books()
    if not books:
        print("Henüz kayıtlı bir kitap yok.")
    else:
        for index, book in enumerate(books, start=1):
            print(f"{index}. {book['Kitap_Adi']} - {book['Yazar']} ({book['Yayinevi']}) - {book['Fiyat']} TL")

def add_book():
    """Kullanıcıdan alınan bilgilerle yeni bir kitap ekler."""
    kitap_adi = input("Kitap adı: ")
    yazar = input("Yazar: ")
    yayinevi = input("Yayınevi: ")
    dil = input("Dil: ")
    fiyat = float(input("Fiyat: "))
    barkod = int(input("Barkod: "))

    new_book = {
        "Kitap_Adi": kitap_adi,
        "Yazar": yazar,
        "Yayinevi": yayinevi,
        "Dil": dil,
        "Fiyat": fiyat,
        "Barkod": barkod
    }

    books = load_books()
    books.append(new_book)
    save_books(books)
    print("Kitap başarıyla eklendi!")

def search_book():
    """Barkod numarasıyla kitap arar."""
    barkod = int(input("Aramak istediğiniz kitabın barkod numarasını girin: "))
    books = load_books()
    
    for book in books:
        if book["Barkod"] == barkod:
            print(f"Kitap bulundu: {book['Kitap_Adi']} - {book['Yazar']} ({book['Yayinevi']}) - {book['Fiyat']} TL")
            return

    print("Kitap bulunamadı.")

def delete_book():
    """Barkod numarasıyla bir kitabı siler."""
    barkod = int(input("Silmek istediğiniz kitabın barkod numarasını girin: "))
    books = load_books()

    for book in books:
        if book["Barkod"] == barkod:
            books.remove(book)
            save_books(books)
            print("Kitap başarıyla silindi!")
            return

    print("Kitap bulunamadı.")

