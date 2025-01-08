import random

# Soru ve cevaplar
questions_and_answers = {
    "Türkiye'nin başkenti neresidir?": "ankara",
    "Python hangi tür bir dilidir?": "programlama",
    "En büyük gezegen hangisidir?": "jüpiter",
    "Python'un yaratıcısı kimdir?": "guido van rossum",
    "Dünyanın en uzun nehri hangisidir?": "nil",
    "Hangi elementin sembolü 'O'dur?": "oksijen",
    "Dünyadaki en büyük okyanus hangisidir?": "pasifik",
    "En küçük gezegen hangisidir?": "merkur",
    "İstanbul hangi denize kıyısı olan bir şehirdir?": "marmara",
    "En büyük hayvan hangisidir?": "mavi balina",
    "Güneş sistemi kaç gezegenden oluşur?": "sekiz",
    "Hangi gezegen 'Kızıl Gezegen' olarak bilinir?": "mars",
    "Dünyada en fazla konuşulan dil hangisidir?": "çince",
    "Hangi ülke Piramitleri ile ünlüdür?": "mısır",
    "En eski medeniyetlerden biri hangisidir?": "mezoamerika",
    "Başbakanlık hangi ülkenin başkentinde bulunmaktadır?": "ingiltere",
    "Eiffel Kulesi hangi şehirde bulunur?": "paris",
    "Venüs gezegeni hangi gezegene yakın bir gezegendir?": "dünya",
    "Dünyanın en uzun nehri hangisidir?": "nil",
}

# Yönetici şifresi
ADMIN_PASSWORD = "1903"

def ask_questions():
    score = 0  # Başlangıçta puan 0
    total_questions = len(questions_and_answers)  # Toplam soru sayısı

    print("\nSoru-Cevap Uygulamasına Hoşgeldiniz!")
    print("Cevaplarınızı küçük harflerle yazmaya özen gösterin.\n")

    # Soruları rastgele sıraya sokuyoruz
    questions = list(questions_and_answers.items())  # Soru ve cevapları bir listeye çevir
    random.shuffle(questions)  # Soruları karıştırıyoruz

    # Soruları sırayla soralım
    for question, correct_answer in questions:
        print(question)
        user_answer = input("Cevabınızı girin: ").strip().lower()  # Kullanıcı cevabını al

        # Cevabı kontrol et
        if user_answer == correct_answer:
            print("Doğru!")
            score += 1
        else:
            print(f"Yanlış! Doğru cevap: {correct_answer.capitalize()}")
        
        print("-" * 30)

    # Sonuçları göster
    print(f"\nToplam Puanınız: {score}/{total_questions}")
    
    if score == total_questions:
        print("Tebrikler! Bütün soruları doğru bildiniz!")
    elif score >= total_questions / 2:
        print("İyi iş! Daha fazla çalışarak mükemmeliyet hedefleyebilirsiniz!")
    else:
        print("Daha fazla pratik yapmalısınız!")

def show_answers():
    # Yönetici paneli ve cevapları göster
    print("Yönetici Paneli - Cevaplar:\n")
    for question, correct_answer in questions_and_answers.items():
        print(f"Soru: {question} \nCevap: {correct_answer.capitalize()}\n")
    print("-" * 50)

    while True:
        action = input("Başka ne arıyorsunuz? (Sırlar Odası yazarsanız sırlar odası, exit: çıkış) : ").strip().lower()

        if action == "exit":
            print("Çıkış yapılıyor...")
            break  # Çıkış yap, programı sonlandır
        elif action == "sırlar odası":
            ask_for_secret()  # Sırlar Odası'na yönlendir
        else:
            print("Geçersiz komut, 'exit' yazarsanız çıkış yapabilirsiniz.")

def ask_for_secret():
    print("Sırlar Odasına hoş geldiniz!")
    secret_request = input("Sırlar odasından kimin sırrını istersin? (Kodları göster yazarsan kodları gösterir): ").strip().lower()

    if secret_request == "kodları göster":
        print("\nİşte Kodlarınız:\n")
        show_python_code()  # Python kodlarını göster
    else:
        print(f"{secret_request.capitalize()} hakkında bir sırrım yok.\n")
    
    while True:
        action = input("Başka ne arıyorsunuz? (Sırlar Odası veya exit yazabilirsiniz) : ").strip().lower()
        
        if action == "exit":
            print("Çıkış yapılıyor...")
            break
        elif action == "sırlar odası":
            ask_for_secret()  # Yine sırlar odasına girme seçeneği
        else:
            print("Geçersiz komut. 'exit' yazarsanız çıkış yapabilirsiniz.")

def show_python_code():
    # Python kodlarını göster
    python_code = '''import random

# Soru ve cevaplar
questions_and_answers = {
    "Türkiye'nin başkenti neresidir?": "ankara",
    "Python hangi tür bir dilidir?": "programlama",
    "En büyük gezegen hangisidir?": "jüpiter",
    "Python'un yaratıcısı kimdir?": "guido van rossum",
    "Dünyanın en uzun nehri hangisidir?": "nil",
    "Hangi elementin sembolü 'O'dur?": "oksijen",
    "Dünyadaki en büyük okyanus hangisidir?": "pasifik",
    "En küçük gezegen hangisidir?": "merkur",
    "İstanbul hangi denize kıyısı olan bir şehirdir?": "marmara",
    "En büyük hayvan hangisidir?": "mavi balina",
    "Güneş sistemi kaç gezegenden oluşur?": "sekiz",
    "Hangi gezegen 'Kızıl Gezegen' olarak bilinir?": "mars",
    "Dünyada en fazla konuşulan dil hangisidir?": "çince",
    "Hangi ülke Piramitleri ile ünlüdür?": "mısır",
    "En eski medeniyetlerden biri hangisidir?": "mezoamerika",
    "Başbakanlık hangi ülkenin başkentinde bulunmaktadır?": "ingiltere",
    "Eiffel Kulesi hangi şehirde bulunur?": "paris",
    "Venüs gezegeni hangi gezegene yakın bir gezegendir?": "dünya",
    "Dünyanın en uzun nehri hangisidir?": "nil",
}

# Yönetici şifresi
ADMIN_PASSWORD = "1903"
'''

    print(python_code)

def admin_login():
    # Şifreyi en başta soralım
    print("Yönetici girişi için şifrenizi girin:")
    password = input("Şifre: ").strip()
    
    if password == ADMIN_PASSWORD:
        print("\nYönetici Girişi Başarılı!\n")
        show_answers()  # Cevapları yönetici için göster
    else:
        print("\nYanlış şifre! Yönetici girişi sağlanamadı. Sorulara devam ediliyor...\n")
        ask_questions()  # Şifre yanlışsa, normal soru-cevap oyununa başla

# Ana fonksiyonu çalıştır
def main():
    admin_login()  # İlk başta şifreyi sor ve işlemi başlat

if __name__ == "__main__":
    main()
