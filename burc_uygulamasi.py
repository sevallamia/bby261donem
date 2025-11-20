import tkinter as tk
from tkinter import ttk
# PIL kütüphanesi yüklü değilse: pip install pillow
from PIL import Image, ImageTk
from datetime import datetime
import re
import webbrowser
import os
# os kütüphanesini import ettik.

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
# Eleman tabanlı uyum hesaplama
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
        # Aynı ay içinde başlangıç ve bitiş
        if bas_ay == bit_ay and ay == bas_ay and bas_gun <= gun <= bit_gun:
            return burc
        # Yıl geçişli burçlar (örn: Oğlak 12. ayda başlar, 1. ayda biter)
        elif bas_ay > bit_ay: 
            if (ay == bas_ay and gun >= bas_gun) or (ay == bit_ay and gun <= bit_gun):
                return burc
        # Normal geçiş (bas_ay < bit_ay)
        elif bas_ay < bit_ay and ay == bas_ay and gun >= bas_gun:
            return burc
        elif bas_ay < bit_ay and ay == bit_ay and gun <= bit_gun:
            return burc

# ------------------------------
# Tkinter pencere
# ------------------------------
root = tk.Tk()
root.title("Burç Uygulaması — Geliştirilmiş Tarih Girişi")
root.geometry("680x580") # Pencere boyutunu biraz artırdık

# ------------------------------
# Ana menü
# ------------------------------

def ana_menu():
    for w in root.winfo_children():
        w.destroy()
    lbl = tk.Label(root, text="Burç Uygulamasına Hoşgeldiniz 🌟", font=("Arial",20,"bold"))
    lbl.pack(pady=16)

    btn = tk.Button(root, text="Burç Yorumu ve Uyum Hesaplama", font=("Arial",14), width=30, command=burc_yorumu)
    btn.pack(pady=10)

    btn2 = tk.Button(root, text="Tüm Burçları Kaydet", font=("Arial",12), command=html_kaydet)
    btn2.pack(pady=8)

    aciklama = tk.Label(root, text="Not: Tarih alanına sadece **gün ve ay** girin. Farklı ayraçlar kabul edilir.\nÖrnekler: 05.09, 5/9, 05-09, 5/9/2000 (yıl ihmal edilir)", wraplength=580, justify="center")
    aciklama.pack(pady=20)
    
    # Tüm burçlar listesi
    burclar_listesi = tk.Label(root, text="Burçların Tam Listesi:\n" + ", ".join(burclar.keys()), font=("Arial", 10))
    burclar_listesi.pack(pady=10)

# ------------------------------
# Burç Yorumu ekranı
# ------------------------------

def burc_yorumu():
    for w in root.winfo_children():
        w.destroy()

    baslik = tk.Label(root, text="Doğum Tarihi Analizi", font=("Arial",18,"bold"))
    baslik.pack(pady=10)

    tarih_label = tk.Label(root, text="Doğum tarihinizi girin (gg.aa veya gg/aa/yyyy):")
    tarih_label.pack()
    tarih_entry = tk.Entry(root, width=30)
    tarih_entry.pack(pady=5)

    # Resim ve sonuçları tutacak çerçeve
    info_frame = tk.Frame(root)
    info_frame.pack(pady=10)

    resim_label = tk.Label(info_frame, width=140, height=140, text="Burç Resmi")
    resim_label.pack(side="left", padx=20)
    
    sonuc_label = tk.Label(info_frame, text="Sonuçlar burada gösterilecektir.", 
                           font=("Arial",12), justify="left", wraplength=450, 
                           pady=5, relief="groove", anchor="nw", width=50, height=8)
    sonuc_label.pack(side="left")

    uyum_label = tk.Label(root, text="", font=("Arial",11), justify="left", wraplength=600)
    uyum_label.pack(pady=8)

    def goster():
        s = tarih_entry.get().strip()
        
        # 1. Girdiyi temizle: Sadece rakamları ve ayraçları (., /, -) tut
        temizlenmis_s = re.sub(r"[^0-9\.\/\-]", "", s)
        
        # 2. Tüm ayraçları tek tip bir ayıraça (nokta .) çevir
        s2 = re.sub(r"[\/\-]", ".", temizlenmis_s)
        
        # 3. Boş girdileri filtreleyerek parçalara ayır
        parts = [p for p in s2.split(".") if p]
        
        gun, ay = None,None
        
        # Çıktı etiketlerini sıfırla
        sonuc_label.config(text="Sonuçlar burada gösterilecektir.")
        resim_label.config(image='', text="Burç Resmi")
        uyum_label.config(text="")
        
        try:
            if len(parts) < 2:
                raise ValueError("Lütfen gün ve ay (en az 2 parça) girin.")
            
            # Gün ve Ay'ı al. Yıl varsa 3. parça olarak ihmal edilecek.
            gun = int(parts[0])
            ay = int(parts[1])
            
            # Değerlerin geçerliliğini kontrol et
            if not (1 <= ay <= 12 and 1 <= gun <= 31):
                raise ValueError("Gün veya ay değeri geçerli aralıkta değil.")
            
            # 30 veya 31 gün kontrolü (Basit bir kontrol)
            if (ay in [4, 6, 9, 11] and gun > 30) or (ay == 2 and gun > 29):
                raise ValueError("Bu ay için gün sayısı geçersiz.")
                
            burc = burc_bul(gun, ay)
            if not burc:
                sonuc_label.config(text=f"Girilen tarih ({gun:02d}.{ay:02d}) hiçbir burç aralığına denk gelmiyor. Lütfen gün ve ayı kontrol edin.", 
                                   font=("Arial",12,"bold"), fg="red")
                return
            
            # --- Burç bulundu, sonuçları göster ---
            info = burclar[burc]
            sonuc_label.config(text=f"Burcunuz: **{burc}**\nElementiniz: **{info['element']}**\n\n**Özellikler**:\n{info['ozellik']}",
                               font=("Arial",12), fg="black")

            # Resim göster
            try:
                if not os.path.exists(info['resim']):
                    raise FileNotFoundError(f"{info['resim']} dosyası bulunamadı.")
                img = Image.open(info['resim'])
                img = img.resize((140, 140))
                photo = ImageTk.PhotoImage(img)
                resim_label.config(image=photo, text="")
                resim_label.image = photo
            except Exception as e:
                resim_label.config(text=f"Resim Hatası:\n{info['resim']}\n{e}", font=("Arial",8))

            # Uyum gösterimi
            uyum_text = "--- 🤝 Uyum Puanları (Örnekler) 🤝 ---\n"
            uyum_ornekleri = []
            
            elementim = info['element']
            
            # Kendi elementi (Bir tane)
            ornek_burc = next((s for s in elementler[elementim] if s != burc), None)
            if ornek_burc:
                uyum_ornekleri.append((ornek_burc, uyum_puani(burc, ornek_burc)))

            # İyi uyum elementi (Bir tane)
            iyi_uyum_elementi = {"Ateş":"Hava", "Hava":"Ateş", "Toprak":"Su", "Su":"Toprak"}.get(elementim)
            if iyi_uyum_elementi:
                ornek_burc = next((s for s in elementler[iyi_uyum_elementi] if s != burc), None)
                if ornek_burc:
                    uyum_ornekleri.append((ornek_burc, uyum_puani(burc, ornek_burc)))

            # Zorlu uyum elementi (Bir tane)
            zorlu_uyum_elementi = {"Ateş":"Su", "Hava":"Toprak", "Toprak":"Hava", "Su":"Ateş"}.get(elementim)
            if zorlu_uyum_elementi:
                ornek_burc = next((s for s in elementler[zorlu_uyum_elementi] if s != burc), None)
                if ornek_burc:
                    uyum_ornekleri.append((ornek_burc, uyum_puani(burc, ornek_burc)))
                    
            
            # Uyum metnini oluştur (Tekrar edenleri set ile temizleyip listeye çevir)
            for diger, puan in list(set(uyum_ornekleri)):
                uyum_text += f" - {diger} ({sign_to_element[diger]}): **{puan}**/100\n"
            
            uyum_label.config(text=uyum_text)
            
        except ValueError as e:
            # Kullanıcıya özel format hataları
            sonuc_label.config(text=f"Girdi Hatası: {e}\nLütfen sadece gün ve ay girin (örnek: 05.09 veya 5/9)",
                               font=("Arial",12,"bold"), fg="red")
        except Exception as e:
            # Diğer beklenmeyen hatalar
            sonuc_label.config(text=f"Genel Hata Oluştu: {e}",
                               font=("Arial",12,"bold"), fg="red")

    goster_btn = tk.Button(root, text="Burcumu Göster", font=("Arial",12,"bold"), command=goster)
    goster_btn.pack(pady=10)

    geri_btn = tk.Button(root, text="Ana Menüye Dön", command=ana_menu)
    geri_btn.pack(pady=6)

# ------------------------------
# HTML dosyası oluşturma
# ------------------------------

def html_kaydet():
    try:
        html = "<!doctype html>\n<html lang=\"tr\">\n<head>\n<meta charset=\"utf-8\">\n<title>Burçlar ve Özellikleri</title>\n<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n<style>body{font-family:Arial,Helvetica,sans-serif;padding:20px;line-height:1.6} .card{border-radius:8px;padding:12px;margin:15px 0;box-shadow:0 2px 8px rgba(0,0,0,0.1); border-left: 5px solid #007bff;} h2{color:#007bff;} table{border-collapse:collapse;width:100%;margin-top:20px;} th,td{border:1px solid #ddd;padding:10px;text-align:center;} th{background-color:#f2f2f2;}</style>\n</head>\n<body>\n<h1>Burçlar — Özellikler ve Uyum Tablosu</h1>\n<p>Bu sayfa uygulama tarafından otomatik oluşturulmuştur.</p>\n"
        # Burç kartları
        for s,info in burclar.items():
            desc = info['ozellik']
            element = info.get('element','')
            html += f"<div class=\"card\"><h2>{s} Burcu ({element})</h2><p><b>Dönemi:</b> {info['tarih'][0][0]}.{info['tarih'][0][1]} - {info['tarih'][1][0]}.{info['tarih'][1][1]}</p><p>{desc}</p></div>\n"
        # Uyum tablosu
        html += "<h2>Burç Uyum Tablosu (0-100 Puan)</h2>\n<table><tr><th></th>"
        signs = list(burclar.keys())
        for s in signs:
            html += f"<th>{s}</th>"
        html += "</tr>\n"
        for s1 in signs:
            html += f"<tr><th>{s1}</th>"
            for s2 in signs:
                html += f"<td>{uyum_puani(s1,s2)}</td>"
            html += "</tr>\n"
        html += "</table>\n<p style='margin-top:20px;'>Not: Uyum puanları basitleştirilmiş element uyumlarına göre hesaplanmıştır.</p>\n</body>\n</html>"

        dosya_adi = 'burclar_analiz.html'
        with open(dosya_adi,'w',encoding='utf-8') as f:
            f.write(html)
        
        # Dosyayı tarayıcıda aç
        webbrowser.open(os.path.abspath(dosya_adi))
        tk.messagebox.showinfo('Başarılı','HTML dosyası başarıyla oluşturuldu ve tarayıcıda açıldı: ' + dosya_adi)
    except Exception as e:
        tk.messagebox.showerror('Hata','HTML oluşturulurken veya açılırken hata: ' + str(e))

# ------------------------------
# Başlat
# ------------------------------
if __name__ == "__main__":
    ana_menu()
    root.mainloop()
