import streamlit as st
import joblib
import pandas as pd
import base64

# Eğitilmiş modeli yükleme
model = joblib.load('ev_fiyat_model.joblib')

# İlçe, oda sayısı, kat seçeneği, ev tipi ve diğer girdiler için seçenekleri oluşturma
ilceler = ['adalar', 'arnavutkoy', 'atasehir', 'avcilar', 'bagcilar', 'bahcelievler', 'bakirkoy',
           'basaksehir', 'bayrampasa', 'besiktas', 'beykoz', 'beylikduzu', 'beyoglu', 'buyukcekmece',
           'catalca', 'cekmekoy', 'esenler', 'esenyurt', 'eyupsultan', 'fatih', 'gaziosmanpasa',
           'gungoren', 'kadikoy', 'kagithane', 'kartal', 'kucukcekmece', 'maltepe', 'pendik', 'sancaktepe',
           'sariyer', 'sile', 'silivri', 'sisli', 'sultanbeyli', 'sultangazi', 'tuzla', 'umraniye',
           'uskudar', 'zeytinburnu']

oda_sayisi = ['1 Oda', '1+1', '1.5+1', '2+0', '2+1', '2+2', '2.5+1', '3+1', '3+2', '3.5+1', '4+1', '4+2',
              '4.5+1', '5 Oda', '5+1', '5+2', '5+3', '5+4', '6+1', '6+2', '6+3', '6+4', '7+1', '7+2',
              '7+3', '8+ Oda', 'Stüdyo']

kat_secenekleri = [
    '1. Kat', '2. Kat', '3. Kat', '4. Kat', '5. Kat', '6. Kat', '7. Kat', '8. Kat', '9. Kat', '10. Kat',
    '11. Kat', '12. Kat', '13. Kat', '14. Kat', '15. Kat', '16. Kat', '17. Kat', '18. Kat', '19. Kat',
    '20. Kat', '21. Kat', '22. Kat', '23. Kat', '24. Kat', '25. Kat', '26. Kat', '27. Kat', '28. Kat',
    '29. Kat', '30. Kat', '31. Kat', '32. Kat', '33. Kat', '34. Kat', '35. Kat', '36. Kat', '38. Kat',
    '40+. Kat', '10-20. Kat', '20-30. Kat', 'Bahçe Dublex', 'Bahçe Katı', 'Düz Giriş', 'Kot 1 (-1). Kat',
    'Kot 2 (-2). Kat', 'Kot 3 (-3). Kat', 'Müstakil', 'Tam Bodrum', 'Yarı Bodrum', 'Yüksek Bodrum',
    'Yüksek Giriş', 'Çatı Dubleks', 'Çatı Katı'
]

ev_tipleri = ['Bina', 'Daire', 'Dağ Evi', 'Devremülk', 'Kooperatif', 'Köy Evi', 'Köşk', 'Müstakil Ev',
              'Prefabrik', 'Residence', 'Villa', 'Yalı (Komple)', 'Yalı Dairesi', 'Yazlık', 'Çiftlik Evi']

# İlçeler için encode
ilceler_encode = {'adalar': 0, 'arnavutkoy': 1, 'atasehir': 2, 'avcilar': 3, 'bagcilar': 4,
                  'bahcelievler': 5, 'bakirkoy': 6, 'basaksehir': 7, 'bayrampasa': 8, 'besiktas': 9,
                  'beykoz': 10, 'beylikduzu': 11, 'beyoglu': 12, 'buyukcekmece': 13, 'catalca': 14,
                  'cekmekoy': 15, 'esenler': 16, 'esenyurt': 17, 'eyupsultan': 18, 'fatih': 19,
                  'gaziosmanpasa': 20, 'gungoren': 21, 'kadikoy': 22, 'kagithane': 23, 'kartal': 24,
                  'kucukcekmece': 25, 'maltepe': 26, 'pendik': 27, 'sancaktepe': 28, 'sariyer': 29,
                  'sile': 30, 'silivri': 31, 'sisli': 32, 'sultanbeyli': 33, 'sultangazi': 34, 'tuzla': 35,
                  'umraniye': 36, 'uskudar': 37, 'zeytinburnu': 38}

# Oda sayıları için encode
oda_sayisi_encode = {'1 Oda': 0, '1+1': 1, '1.5+1': 2, '2+0': 3, '2+1': 4, '2+2': 5, '2.5+1': 6, '3+1': 7,
                     '3+2': 8, '3.5+1': 9, '4+1': 10, '4+2': 11, '4.5+1': 12, '5 Oda': 13, '5+1': 14, '5+2': 15,
                     '5+3': 16, '5+4': 17, '6+1': 18, '6+2': 19, '6+3': 20, '6+4': 21, '7+1': 22, '7+2': 23,
                     '7+3': 24, '8+ Oda': 25, 'Stüdyo': 26}

# Kat seçenekleri için encode
kat_secenekleri_encode = {'1. Kat': 0, '10-20. Kat': 1, '10. Kat': 2, '11. Kat': 3, '12. Kat': 4, '13. Kat': 5,
                          '14. Kat': 6, '15. Kat': 7, '16. Kat': 8, '17. Kat': 9, '18. Kat': 10, '19. Kat': 11,
                          '2. Kat': 12, '20-30. Kat': 13, '20. Kat': 14, '21. Kat': 15, '22. Kat': 16, '23. Kat': 17,
                          '24. Kat': 18, '25. Kat': 19, '26. Kat': 20, '27. Kat': 21, '28. Kat': 22, '29. Kat': 23,
                          '3. Kat': 24, '30-40. Kat': 25, '30. Kat': 26, '31. Kat': 27, '32. Kat': 28, '33. Kat': 29,
                          '34. Kat': 30, '35. Kat': 31, '36. Kat': 32, '38. Kat': 33, '4. Kat': 34, '40+. Kat': 35,
                          '5. Kat': 36, '6. Kat': 37, '7. Kat': 38, '8. Kat': 39, '9. Kat': 40, 'Bahçe Dublex': 41,
                          'Bahçe Katı': 42, 'Düz Giriş': 43, 'Kot 1 (-1). Kat': 44, 'Kot 2 (-2). Kat': 45, 'Kot 3 (-3). Kat': 46,
                          'Müstakil': 47, 'Tam Bodrum': 48, 'Villa Tipi': 49, 'Yarı Bodrum': 50, 'Yüksek Bodrum': 51,
                          'Yüksek Giriş': 52, 'Çatı Dubleks': 53, 'Çatı Katı': 54}

ev_tipleri_encode = {'Bina': 0, 'Daire': 1, 'Dağ Evi': 2, 'Devremülk': 3, 'Kooperatif': 4,
                       'Köy Evi': 5, 'Köşk': 6, 'Müstakil Ev': 7, 'Prefabrik': 8, 'Residence': 9,
                       'Villa': 10, 'Yalı (Komple)': 11, 'Yalı Dairesi': 12, 'Yazlık': 13,
                       'Çiftlik Evi': 14}

# Kullanıcı arayüzünü oluşturma
st.title('Ev Fiyat Tahmini')
st.sidebar.title('Giriş Bilgileri')

# Kullanıcı giriş alanları
ilce = st.sidebar.selectbox('İlçe Seçin', ilceler)
oda = st.sidebar.selectbox('Oda Sayısı Seçin', oda_sayisi)
kat = st.sidebar.selectbox('Ev Kaçıncı katta?', kat_secenekleri)
ev_tipi = st.sidebar.selectbox('Ev Tipi Seçin', ev_tipleri)
brut_metrekare = st.sidebar.number_input('Brüt Metrekare Girin', min_value=1)
net_metrekare = st.sidebar.number_input('Net Metrekare Girin', min_value=1)
bina_yasi = st.sidebar.number_input('Bina Yaşı Girin', min_value=0)
bina_kat_sayisi = st.sidebar.number_input('Bina Kat Sayısı Girin', min_value=1)

# Tahmin yapma fonksiyonu
def ev_fiyat_tahmini(ilce, oda, kat, ev_tipi, brut_metrekare, bina_yasi, bina_kat_sayisi, net_metrekare):
    # Kullanıcı girdilerini veri çerçevesine dönüştürme
    girdiler = pd.DataFrame({
        'ilce': [ilceler_encode[ilce]],
        'brut_metrekare': [brut_metrekare],
        'bina_yasi': [bina_yasi],
        'bina_kat_sayisi': [bina_kat_sayisi],
        'oda': [oda_sayisi_encode[oda]],
        'kat': [kat_secenekleri_encode[kat]],
        'net_metrekare': [net_metrekare],
        'ev_tipi': [ev_tipleri_encode[ev_tipi]]
    })

    # Modeli kullanarak tahmin yapma
    tahmin = model.predict(girdiler.values)

    return tahmin[0]*3

# Arka plan resmini ekleme
def set_background(image_file):
    with open(image_file, "rb") as image:
        encoded_string = base64.b64encode(image.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/jpeg;base64,{encoded_string});
            background-size: cover;
            padding: 10px;  /* İçeriği çerçeveden ayırma */
            border-radius: 10px;  /* Köşeleri yuvarlama */
            border: 2px solid green;  /* Dikdörtgen çerçeve oluşturma */
        }}
        .stMarkdown {{
            color: white;  /* Yazı rengi */
            font-size: 20px;
            font-weight: bold;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

set_background("background.jpg")  # Arka plan resmini burada belirtin

# Tahmin sonucunu canlı yeşil renkte ve çerçeve içinde gösterme
if st.sidebar.button('Hesapla'):
    tahmin_sonucu = ev_fiyat_tahmini(ilce, oda, kat, ev_tipi, brut_metrekare, bina_yasi, bina_kat_sayisi, net_metrekare)
    formatted_tahmin = '{:,.0f}'.format(tahmin_sonucu)

    # Çerçeve genişliğini otomatik olarak ayarlamak için display: inline-block özelliğini kullanalım
    st.markdown('<div style="background-color:#00FF00; display: inline-block; padding:10px; border-radius:10px;">'
                'Tahmini Ev Fiyatı: <span style="color:white;">' + str(formatted_tahmin) + ' TL</span>'
                '</div>', unsafe_allow_html=True)
