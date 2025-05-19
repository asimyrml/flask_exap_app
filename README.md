# Flask Sınav Uygulaması

## Proje Özeti

Bu proje, Python'ın ileri seviye kütüphaneleriyle geliştirilen, **gençlere yönelik, dinamik ve kullanıcı dostu bir sınav platformudur**.  
Flask ve SQLAlchemy kullanılarak, çoktan seçmeli ve farklı Python konularını kapsayan bir sınav sunulur. Kullanıcılar sınavı tekrar tekrar çözebilir, hem kendi hem de genel en yüksek skorları canlı olarak görebilir.  
Proje PythonAnywhere üzerinde yayınlanmaya hazırdır ve bütün fonksiyonları gereksinimlere uygun şekilde çalışır.

---

## İçerik ve Özellikler

- **Kapsanan Sınav Konuları:**
  - Python ile sohbet botu otomasyonu (Discord.py)
  - Python ile web geliştirme (Flask)
  - Python ile yapay zeka geliştirme
  - Bilgisayar görüşü (TensorFlow, ImageAI)
  - Doğal Dil İşleme (BeautifulSoup, NLTK)

- **Temel Özellikler:**
  - Kullanıcı adı ile sınava giriş
  - En az 5 soruluk, rastgele sıralanan dinamik sınav
  - Sorular ve seçenekler **ilişkisel veritabanında** saklanır
  - Flask-SQLAlchemy ile veritabanı yönetimi
  - Sınav sonucu: hem en son alınan puan hem de en yüksek skor gösterimi
  - Skorlar % (yüzde) olarak hesaplanır ve görüntülenir
  - Genel ve kişisel en yüksek skorlar, sitenin sağ üst köşesinde canlı olarak görüntülenir
  - Sınav sonuç ekranı: şık bir pop-up ile kullanıcıya gösterilir, tekrar çözme veya ana sayfaya dönme seçenekleri sunulur
  - Tüm sayfalarda alt kısımda (footer) yazar bilgisi yer alır
  - Responsive ve sade arayüz

---

## Proje Mimarisi
```
project/
│
├── app.py
├── requirements.txt
├── models.py 
│
├── templates/
│ ├── index.html
│ ├── exam.html
│ └── result.html
│
├── static/
│ └── styles.css
│
└── README.md
```
---


## Kurulum & Çalıştırma

1. **Depoyu klonlayın**
    ```bash
    git clone https://github.com/yourusername/flask-sinav-proje.git
    cd flask-sinav-proje
    ```

2. **(Opsiyonel) Sanal ortam oluşturun**
    ```bash
    python -m venv venv
    source venv/bin/activate  # Windows: venv\Scripts\activate
    ```

3. **Bağımlılıkları yükleyin**
    ```bash
    pip install -r requirements.txt
    ```

4. **Veritabanını başlatın ve soruları yükleyin**
    ```bash
    python app.py
    ```

5. **Uygulamayı başlatın**
    ```bash
    python app.py
    ```
    Ardından tarayıcıdan [http://127.0.0.1:5000](http://127.0.0.1:5000) adresine giderek uygulamayı kullanabilirsiniz.

---
