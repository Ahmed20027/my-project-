def uye_ol():
    # Sisteme üyelik işlemleri yapılır
    pass

def giris_yap():
    # Sisteme giriş işlemleri yapılır
    pass

def sifre_unuttum():
    # Şifre sıfırlama işlemleri yapılır
    pass

while True:
    print("Lütfen aşağıdaki işlemlerden birini seçiniz:")
    print("1 - Sisteme Üye Ol")
    print("2 - Sisteme Giriş Yap")
    print("3 - Şifremi Unuttum")
    secim = input("Seçiminiz: ")
    if secim == "1":
        uye_ol()
    elif secim == "2":
        giris_yap()
    elif secim == "3":
        sifre_unuttum()
    else:
        print("Hatalı seçim! Lütfen tekrar deneyin.")
