import BookTransactions
import MemberTransactions
import BookGivingTransactions
import json

def main_menu():
    try: #try except CALISINIZ 
        while True:
            print("-" * 50)
            print(" " * 10 + "HALK KUTUPHANEMIZE HOS GELDINIZ" + " " * 10)
            print("-" * 50)
            print("-" * 5 + "1-UYELIK ISLEMLERI" + " " * 10 + "1" + " " * 5)
            print("-" * 5 + "2-KITAP ISLEMLERI" + " " * 11 + "2" + " " * 5 )
            print("-" * 5 + "3-CIKIS" + " " * 21 + "0" + " " * 5 )
            print("-" * 50)
            secim = input("Lutfen yapmak istediginiz secimin kodunu girin: ")            
            if secim == '1':
                member_menu()
            elif secim == '2':
                book_menu()
            elif secim == '0':
                print("Cikis yapiliyor...")
                break
            else:
                print("Gecersiz secim, lutfen tekrar deneyin.")
    except Exception as e:
        print(f"Hata olustu: {e}")

def member_menu():
    while True:
        print("-" * 50)
        print(" " * 5 + "UYELER" + " " * 10 + "= 1 " + " " * 10 + "KITAP ODUNC VERME" + " " * 10 + "= 5 ")
        print(" " * 5 + "UYE EKLEME" + " " * 6 + "= 2 " + " " * 10 + "KITAP IADE" + " " * 17 + "= 6 ")
        print(" " * 5 + "UYE ARA" + " " * 9 + "= 3 " + " " * 10 + "KITAP TAKIBI" + " " * 15 + "= 7 ")
        print(" " * 5 + "UYE SIL" + " " * 9 + "= 4 " + " " * 10 + "CIKIS" + " " * 22 + "= 0 ")
        print("-" * 50)
        secim = input("Islem seciniz: ")
        
        if secim == '0':
            break
        elif secim == '1':
            MemberTransactions.list_members()
        elif secim == '2':
            MemberTransactions.add_member()
        elif secim == '3':
            MemberTransactions.search_member()
        elif secim == '4':
            MemberTransactions.delete_member()
        elif secim == '5':
            BookGivingTransactions.add_bookgiving()
        elif secim == '6':
            BookGivingTransactions.return_bookgiving()
        elif secim == '7':
            BookGivingTransactions.tracking_bookgiving()
        else:
            print(f"{secim} islemi secildi. (Bu kisimda islemler yapilabilir.)")

def book_menu():
    while True:
        print("-" * 50)
        print(" " * 5 + "KITAPLAR" + " " * 12 + "= 1 ")
        print(" " * 5 + "KITAP EKLEME" + " " * 8 + "= 2 ")
        print(" " * 5 + "KITAP ARA" + " " * 11 + "= 3 ")
        print(" " * 5 + "KITAP SIL" + " " * 11 + "= 4 ")
        print(" " * 5 + "CIKIS" + " " * 15 + "= 0 ")
        print("-" * 50)
        secim = input("Islem seciniz: ")
        
        if secim == '0':
            break
        elif secim == '1':
            BookTransactions.list_books()
        elif secim == '2':
            BookTransactions.add_book()
        elif secim == '3':
            BookTransactions.search_book()
        elif secim == '4':
            BookTransactions.delete_book()
        else:
            print(f"{secim} islemi secildi. (Bu kisimda islemler yapilabilir.)")

if __name__ == "__main__":
    main_menu()
