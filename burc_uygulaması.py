import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from datetime import datetime

# ------------------------------
# Burç bilgileri ve tarihleri
# ------------------------------
burclar = {
    "Koç": {
        "tarih": ((3,21),(4,19)),
        "ozellik": "Koç burcu enerjik, cesur ve lider ruhludur. Kararlı, hırslı ve macerayı seven bir burçtur. Sabırsız olabilir ama tutkuyu sever ve özgürlüğüne düşkündür.",
        "resim": "koc.png",
    },
    "Boğa": {
        "tarih": ((4,20),(5,20)),
        "ozellik": "Boğa burcu sabırlı, güvenilir ve sadıktır. Konforu sever ve sevdiklerine bağlıdır. İlişkilerde istikrar ve huzur arar, bazen inatçı olabilir.",
        "resim": "boga.png",
    },
    "İkizler": {
        "tarih": ((5,21),(6,20)),
        "ozellik": "İkizler burcu zeki, meraklı ve sosyal bir burçtur. Hızlı düşünen, iletişimi güçlü, değişken ruhludur. Macerayı sever, bazen kararsız olabilir.",
        "resim": "ikizler.png",
    },
    "Yengeç": {
        "tarih": ((6,21),(7,22)),
        "ozellik": "Yengeç burcu duygusal, şefkatli ve koruyucudur. Evine düşkün ve hassas bir burçtur. İlişkilerde anlayışlı ve sadıktır, empati yeteneği yüksektir.",
        "resim": "yengec.png",
    },
    "Aslan": {
        "tarih": ((7,23),(8,22)),
        "ozellik": "Aslan burcu lider ruhlu, gururlu ve cesurdur. Gösterişi ve ilgiyi sever, cömerttir. İlişkilerde tutkunu sever, sevgi dolu ve sadıktır.",
        "resim": "aslan.png",
    },
    "Başak": {
        "tarih": ((8,23),(9,22)),
        "ozellik": "Başak burcu titiz, dikkatli ve çalışkan bir burçtur. Analitik ve detaycıdır. İlişkilerde güvenilir ve sorumluluk sahibidir, bazen eleştirel olabilir.",
        "resim": "basak.png",
    },
    "Terazi": {
        "tarih": ((9,23),(10,22)),
        "ozellik": "Terazi burcu adaletli, sosyal ve uyumlu bir burçtur. Estetik ve güzellikten hoşlanır. İlişkilerde romantik, dengeli ve uyumlu davranır.",
        "resim": "terazi.png",
    },
    "Akrep": {
        "tarih": ((10,23),(11,21)),
        "ozellik": "Akrep burcu tutkulu, sezgisel ve derin düşüncelidir. Kararlı ve yoğun duygulara sahiptir. İlişkilerde derin bağ kurmayı sever, kıskanç olabilir.",
        "resim": "akrep.png",
    },
    "Yay": {
        "tarih": ((11,22),(12,21)),
        "ozellik": "Yay burcu özgür ruhlu, iyimser ve açık fikirli bir burçtur. Macerayı ve yenilikleri sever. İlişkilerde eğlenceli, özgürlükçü ve dürüsttür.",
        "resim": "yay.png",
    },
    "Oğlak": {
        "tarih": ((12,22),(1,19)),
        "ozellik": "Oğlak burcu disiplinli, sorumluluk sahibi ve çalışkandır. Planlı ve sabırlıdır. İlişkilerde güvenilir, sadık ve kararlıdır.",
        "resim": "oglak.png",
    },
    "Kova": {
        "tarih": ((1,20),(2,18)),
        "ozellik": "Kova burcu yenilikçi, özgür ve yaratıcıdır. Arkadaş canlısı ve bağımsızdır. İlişkilerde dostane, özgürlükçü ve anlayışlıdır.",
        "resim": "kova.png",
    },
    "Balık": {
        "tarih": ((2,19),(3,20)),
        "ozellik": "Balık burcu duygusal, hassas ve sezgiseldir. Hayal gücü geniş, fedakâr ve romantiktir. İlişkilerde şefkatli ve sadıktır.",
        "resim": "balik.png",
    },
}

# ------------------------------
# Doğum tarihinden burç bulma
# ------------------------------
def burc_bul(gun, ay):
    for burc, info in burclar.items():
        (bas_gun, bas_ay),(bit_gun, bit_ay) = info["tarih"]
        if (ay == bas_ay and gun >= bas_gun) or (ay == bit_ay and gun <= bit_gun):
            return burc
    return None

# ------------------------------
# Tkinter pencere
# ------------------------------
pencere = tk.Tk()
pencere.title("Burç Uygulaması 💫")
pencere.geometry("600x500")

# ------------------------------
# Ana menü
# ------------------------------
def ana_menu():
    for widget in pencere.winfo_children():
        widget.destroy()
    
    baslik = tk.Label(pencere, text="Burç Uygulamasına Hoşgeldiniz", font=("Arial",16,"bold"))
    baslik.pack(pady=20)
    
    yorum_btn = tk.Button(pencere, text="Burç Yorumu", font=("Arial",14), width=20, command=burc_yorumu)
    yorum_btn.pack(pady=10)

# ------------------------------
# Burç Yorumu sayfası
# ------------------------------
def burc_yorumu():
    for widget in pencere.winfo_children():
        widget.destroy()
    
    baslik = tk.Label(pencere, text="Burç Yorumu", font=("Arial",16,"bold"))
    baslik.pack(pady=10)
    
    tarih_label = tk.Label(pencere, text="Doğum tarihinizi girin (gg.aa.yyyy):")
    tarih_label.pack()
    tarih_entry = tk.Entry(pencere)
    tarih_entry.pack(pady=5)
    
    cinsiyet_label = tk.Label(pencere, text="Cinsiyetinizi seçin:")
    cinsiyet_label.pack()
    cinsiyet_combo = ttk.Combobox(pencere, values=["Kadın","Erkek"])
    cinsiyet_combo.pack(pady=5)
    
    sonuc_label = tk.Label(pencere, text="", font=("Arial",12), justify="left", wraplength=500)
    sonuc_label.pack(pady=10)
    
    resim_label = tk.Label(pencere)
    resim_label.pack()
    
    def goster():
        try:
            dogum = datetime.strptime(tarih_entry.get(), "%d.%m.%Y")
            burc = burc_bul(dogum.day, dogum.month)
            if not burc:
                sonuc_label.config(text="Geçersiz tarih girdiniz.")
                return
            info = burclar[burc]
            
            sonuc_label.config(text=f"Burcunuz: {burc}\n\nÖzellikler:\n{info['ozellik']}")
            
            img = Image.open(info["resim"])
            img = img.resize((100,100))
            photo = ImageTk.PhotoImage(img)
            resim_label.config(image=photo)
            resim_label.image = photo
        except:
            sonuc_label.config(text="Lütfen doğru formatta tarih girin (gg.aa.yyyy)")
    
    goster_btn = tk.Button(pencere, text="Burcumu Göster", command=goster)
    goster_btn.pack(pady=10)
    
    geri_btn = tk.Button(pencere, text="Ana Menüye Dön", command=ana_menu)
    geri_btn.pack(pady=5)

# ------------------------------
# Uygulama başlat
# ------------------------------
ana_menu()
pencere.mainloop()
