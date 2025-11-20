import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from datetime import datetime
import re
import webbrowser

# ------------------------------
# Genişletilmiş burç özellikleri ve element bilgisi
# ------------------------------
burclar = {
    "Koç": {
        "tarih": ((3,21),(4,19)),
        "element": "Ateş",
        "ozellik": (
            "Koç burcu enerjik, cesur ve lider ruhludur. "
            "Girişimci ve rekabetçidir; yeni başlangıçlardan ve meydan okumadan hoşlanır. "
            "Duygularını hızlı yaşar, net kararlar alır ve etrafına motivasyon yayar. "
            "Bazen sabırsız ve aceleci olabilir; dürtüleriyle hareket ettiği zamanlarda detayları kaçırabilir. "
            "İlişkilerde tutkuyu ve samimiyeti sever; açık sözlü olmayı tercih eder."
        ),
        "resim": "koc.png",
    },
    "Boğa": {
        "tarih": ((4,20),(5,20)),
        "element": "Toprak",
        "ozellik": (
            "Boğa burcu sakin, sabırlı ve kararlı bir karakter sergiler. "
            "Güvenlik ve konfora değer verir; sevdiklerine karşı sadık ve koruyucudur. "
            "Praktik zekâsı ve dayanıklılığı sayesinde uzun vadeli hedeflerde başarılı olur. "
            "Değişime karşı temkinli olabilir; bildiği rutini ve istikrarı korumaya çalışır."
        ),
        "resim": "boga.png",
    },
    "İkizler": {
        "tarih": ((5,21),(6,20)),
        "element": "Hava",
        "ozellik": (
            "İkizler burcu meraklı, esnek ve iletişim merkezlidir. "
            "Çabuk öğrenir, farklı fikirleri aynı anda kavrayabilir; sosyal ortamlarda parlar. "
            "Fikir alışverişi ve entelektüel uyarılma onu motive eder; bazen yüzeysel veya kararsız algılanabilir."
        ),
        "resim": "ikizler.png",
    },
    "Yengeç": {
        "tarih": ((6,21),(7,22)),
        "element": "Su",
        "ozellik": (
            "Yengeç burcu şefkatli, koruyucu ve derin duygulara sahiptir. "
            "Aile bağları ve ev yaşamı onun için çok önemlidir; empati gücü yüksektir. "
            "Duygusal güvenlik sağlandığında sadık ve fedakâr bir partner olur; yaralanmaya karşı temkinli davranabilir."
        ),
        "resim": "yengec.png",
    },
    "Aslan": {
        "tarih": ((7,23),(8,22)),
        "element": "Ateş",
        "ozellik": (
            "Aslan burcu cömert, gururlu ve sahneye çıkmayı seven bir karakterdir. "
            "Liderlik özellikleri ve yaratıcı ifade onun ön planda olmasını sağlar. "
            "Aşk ve ilişkilere büyük bir ciddiyetle yaklaşır; ilgi görmekten hoşlanır ve partnerine büyük jestler yapabilir."
        ),
        "resim": "aslan.png",
    },
    "Başak": {
        "tarih": ((8,23),(9,22)),
        "element": "Toprak",
        "ozellik": (
            "Başak burcu analitik, düzenli ve çalışkan yapısıyla bilinir. "
            "Detaylara önem verir, sorumluluk alır ve iyileştirmek için çaba gösterir. "
            "Eleştirel düşünebilir ama niyeti genelde yapıcıdır; ilişkilerde güvenilir ve destekleyicidir."
        ),
        "resim": "basak.png",
    },
    "Terazi": {
        "tarih": ((9,23),(10,22)),
        "element": "Hava",
        "ozellik": (
            "Terazi burcu adaletli, nazik ve uyum arayan bir karakterdir. "
            "Sosyal ilişkilerde denge ve estetik önemser; ortaklıklarda diplomasi yeteneği yüksektir. "
            "Karar verirken bazen iki tarafı da görme isteği kararsızlığa yol açabilir ama genelde orta yolu bulur."
        ),
        "resim": "terazi.png",
    },
    "Akrep": {
        "tarih": ((10,23),(11,21)),
        "element": "Su",
        "ozellik": (
            "Akrep burcu tutkulu, yoğun ve sezgisel bir doğaya sahiptir. "
            "Duygularını derinden yaşar; gizemli ve kararlı bir yapısı vardır. "
            "İlişkilerde sadakat bekler ve derin bağ kurmayı tercih eder; kıskançlık ve kontrol eğilimleri görülebilir."
        ),
        "resim": "akrep.png",
    },
    "Yay": {
        "tarih": ((11,22),(12,21)),
        "element": "Ateş",
        "ozellik": (
            "Yay burcu özgürlükçü, maceracı ve iyimserdir. "
            "Felsefi ve öğrenmeye açık bir yapısı vardır; yolculuk ve keşif onu besler. "
            "Bağlanırken de dürüstlük ve açıklık bekler; monotonluktan çabuk sıkılabilir."
        ),
        "resim": "yay.png",
    },
    "Oğlak": {
        "tarih": ((12,22),(1,19)),
        "element": "Toprak",
        "ozellik": (
            "Oğlak burcu disiplinli, sorumluluk sahibi ve hedef odaklıdır. "
            "Uzun vadeli planlar yapar ve sabırla ilerler; kariyer ve statü onun için önem taşıyabilir. "
            "Duygularını gösterme konusunda temkinli davranabilir ama güvenildiğinde son derece sadık olur."
        ),
        "resim": "oglak.png",
    },
    "Kova": {
        "tarih": ((1,20),(2,18)),
        "element": "Hava",
        "ozellik": (
            "Kova burcu yenilikçi, bağımsız ve orijinal düşüncelere sahiptir. "
            "Toplumsal meselelere duyarlı, arkadaş canlısı ve entelektüel düzeyde bağlantı kurmayı sever. "
            "Duygusal açıdan bazen mesafeli görünse de fikirsel uyum önemlidir."
        ),
        "resim": "kova.png",
    },
    "Balık": {
        "tarih": ((2,19),(3,20)),
        "element": "Su",
        "ozellik": (
            "Balık burcu empatik, hayalperest ve sezgiseldir. "
            "Sanatsal eğilimler, fedakârlık ve başkalarının duygularını hissetme gücü öne çıkar. "
            "Gerçeklikten kaçma eğilimi olabileceği için sınırlar koymakta zaman zaman zorlanabilir."
        ),
        "resim": "balik.png",
    },
}

# ------------------------------
# Eleman tabanlı basit uyum hesaplama
# ------------------------------
elementler = {
    "Ateş": ["Koç","Aslan","Yay"],
    "Toprak": ["Boğa","Başak","Oğlak"],
    "Hava": ["İkizler","Terazi","Kova"],
    "Su": ["Yengeç","Akrep","Balık"],
}

# elementi bul
sign_to_element = {s:info["element"] for s,info in burclar.items()}

def uyum_puani(sign1, sign2):
    # Aynı işaret -> yüksek uyum
    if sign1 == sign2:
        return 95
    e1 = sign_to_element.get(sign1)
    e2 = sign_to_element.get(sign2)
    if e1 == e2:
        return 85
    # Ateş-Hava iyi, Toprak-Su iyi, Ateş-Su zor, Toprak-Hava zor
    pair = {e1, e2}
    if pair == {"Ateş","Hava"}:
        return 80
    if pair == {"Toprak","Su"}:
        return 80
    if pair == {"Ateş","Su"}:
        return 40
    if pair == {"Toprak","Hava"}:
        return 45
    return 60

# ------------------------------
# Doğum gününden burç bulma (sadece gün+ay kullanılır)
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
root = tk.Tk()
root.title("Burç Uygulaması — Yıl ve Cinsiyet Kaldırıldı")
root.geometry("640x560")

# ------------------------------
# Ana menü
# ------------------------------

def ana_menu():
    for w in root.winfo_children():
        w.destroy()
    lbl = tk.Label(root, text="Burç Uygulamasına Hoşgeldiniz", font=("Arial",18,"bold"))
    lbl.pack(pady=16)

    btn = tk.Button(root, text="Burç Yorumu", font=("Arial",14), width=20, command=burc_yorumu)
    btn.pack(pady=10)

    btn2 = tk.Button(root, text="Burçları HTML Olarak Kaydet", font=("Arial",12), command=html_kaydet)
    btn2.pack(pady=8)

    aciklama = tk.Label(root, text="Not: Tarih alanına sadece gün ve ay girin. Örnek: 05.09 veya 5/9 veya 05-09", wraplength=580, justify="left")
    aciklama.pack(pady=12)

# ------------------------------
# Burç Yorumu ekranı
# ------------------------------

def burc_yorumu():
    for w in root.winfo_children():
        w.destroy()

    baslik = tk.Label(root, text="Burç Yorumu (Yıl ve Cinsiyet gerekmiyor)", font=("Arial",16,"bold"))
    baslik.pack(pady=10)

    tarih_label = tk.Label(root, text="Doğum tarihinizi girin (gg.aa veya gg.aa.yyyy veya gg/aa):")
    tarih_label.pack()
    tarih_entry = tk.Entry(root)
    tarih_entry.pack(pady=5)

    sonuc_label = tk.Label(root, text="", font=("Arial",12), justify="left", wraplength=600)
    sonuc_label.pack(pady=10)

    resim_label = tk.Label(root)
    resim_label.pack()

    uyum_label = tk.Label(root, text="", font=("Arial",11), justify="left", wraplength=600)
    uyum_label.pack(pady=8)

    def goster():
        s = tarih_entry.get().strip()
        # Non-digitleri noktaya çevir ve split et
        s2 = re.sub(r"[^0-9]", ".", s)
        parts = [p for p in s2.split(".") if p]
        try:
            if len(parts) < 2:
                raise ValueError
            gun = int(parts[0])
            ay = int(parts[1])
            if not (1 <= ay <= 12 and 1 <= gun <= 31):
                raise ValueError
            burc = burc_bul(gun, ay)
            if not burc:
                sonuc_label.config(text="Geçersiz tarih aralığı. Lütfen gün ve ayı kontrol edin.")
                return
            info = burclar[burc]
            sonuc_label.config(text=f"Burcunuz: {burc}\n\nÖzellikler:\n{info['ozellik']}")

            # Resim göster
            try:
                img = Image.open(info['resim'])
                img = img.resize((140,140))
                photo = ImageTk.PhotoImage(img)
                resim_label.config(image=photo)
                resim_label.image = photo
            except Exception as e:
                resim_label.config(text=f"Resim yüklenemedi: {e}")

            # Örnek uyum gösterimi: diğer burçlarla puan
            uyum_text = "Burç uyumları (kısa örnek):\n"
            for diger in burclar.keys():
                if diger == burc:
                    continue
                puan = uyum_puani(burc, diger)
                uyum_text += f"- {burc} ile {diger}: {puan}/100\n"
            uyum_label.config(text=uyum_text)
        except Exception:
            sonuc_label.config(text="Lütfen doğru formatta gün ve ay girin (örnek: 05.09 veya 5/9)")

    goster_btn = tk.Button(root, text="Burcumu Göster", command=goster)
    goster_btn.pack(pady=10)

    geri_btn = tk.Button(root, text="Ana Menüye Dön", command=ana_menu)
    geri_btn.pack(pady=6)

# ------------------------------
# HTML dosyası oluşturma
# ------------------------------

def html_kaydet():
    try:
        html = "<!doctype html>\n<html lang=\"tr\">\n<head>\n<meta charset=\"utf-8\">\n<title>Burçlar ve Özellikleri</title>\n<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n<style>body{font-family:Arial,Helvetica,sans-serif;padding:20px;line-height:1.6} .card{border-radius:8px;padding:12px;margin:10px 0;box-shadow:0 1px 4px rgba(0,0,0,0.08)} table{border-collapse:collapse;width:100%} th,td{border:1px solid #ddd;padding:8px;text-align:left}</style>\n</head>\n<body>\n<h1>Burçlar — Özellikler ve Uyum</h1>\n<p>Bu sayfa uygulama tarafından otomatik oluşturulmuştur. Tarihten yılı kaldırdık; cinsiyet alanı çıkarıldı.</p>\n"
        # Burç kartları
        for s,info in burclar.items():
            desc = info['ozellik']
            element = info.get('element','')
            html += f"<div class=\"card\"><h2>{s} — {element}</h2><p>{desc}</p></div>\n"
        # Uyum tablosu
        html += "<h2>Burç Uyum Tablosu (puan)</h2>\n<table><tr><th></th>"
        signs = list(burclar.keys())
        for s in signs:
            html += f"<th>{s}</th>"
        html += "</tr>\n"
        for s1 in signs:
            html += f"<tr><th>{s1}</th>"
            for s2 in signs:
                html += f"<td>{uyum_puani(s1,s2)}</td>"
            html += "</tr>\n"
        html += "</table>\n</body>\n</html>"

        with open('burclar.html','w',encoding='utf-8') as f:
            f.write(html)
        # Dosyayı tarayıcıda aç
        webbrowser.open('burclar.html')
    except Exception as e:
        tk.messagebox.showerror('Hata','HTML oluşturulurken hata: ' + str(e))

# ------------------------------
# Başlat
# ------------------------------
ana_menu()
root.mainloop()
