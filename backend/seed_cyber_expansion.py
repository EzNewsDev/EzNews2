from app import create_app, db
from app.models.category import Category
from app.models.article import Article
from app.models.tag import Tag
from app.models.user import User
from datetime import datetime, timedelta
import random

app = create_app()

def seed_cyber_expansion():
    with app.app_context():
        print("Seeding Expanded Cyber Security Content...")

        # 1. Get Admin User
        admin = User.query.filter_by(email='admin@eznews.com').first()
        if not admin:
            print("Admin user not found.")
            return

        # 2. Get Categories
        cyber_cat = Category.query.filter_by(slug='cyber-security').first()
        if not cyber_cat:
            cyber_cat = Category(name='Cyber Security', slug='cyber-security')
            db.session.add(cyber_cat)
            db.session.commit()

        # 3. Create Tags
        tags_list = [
            'Phishing', 'Social Engineering', 'Zero Day', 'BSSN', 'OJK', 
            'Crypto', 'LockBit', 'Brain Cipher', 'Data Privacy'
        ]
        
        tags_map = {}
        for tag_name in tags_list:
            slug = tag_name.lower().replace(' ', '-')
            tag = Tag.query.filter_by(slug=slug).first()
            if not tag:
                tag = Tag(name=tag_name, slug=slug)
                db.session.add(tag)
            tags_map[tag_name] = tag
        
        db.session.commit()

        # 4. Create Articles
        articles_data = [
            {
                'title': 'Kronologi Serangan Ransomware Brain Cipher yang Lumpuhkan PDN Surabaya',
                'content': 'Serangan ransomware terhadap Pusat Data Nasional (PDN) di Surabaya pada Juni 2024 menjadi salah satu insiden siber terburuk dalam sejarah Indonesia. Varian ransomware Brain Cipher, turunan dari LockBit 3.0, mengenkripsi ribuan server virtual, melumpuhkan layanan imigrasi di bandara internasional, dan mengganggu ratusan instansi pemerintah. Artikel ini mengulas kronologi lengkap dari deteksi awal hingga pemulihan layanan.',
                'tags': ['Ransomware', 'PDN', 'Brain Cipher', 'LockBit'],
                'image_prompt': 'digital timeline of ransomware attack red warning screens server room chaos'
            },
            {
                'title': 'Peningkatan 70% Kasus Phishing di Indonesia: Kenali Ciri-cirinya',
                'content': 'Badan Siber dan Sandi Negara (BSSN) mencatat lonjakan kasus phishing sebesar 70% di tahun 2024. Modus operandi pelaku semakin canggih, mulai dari menyamar sebagai kurir paket, undangan pernikahan digital, hingga petugas bank. Masyarakat diimbau untuk tidak sembarangan mengklik tautan dari nomor tidak dikenal dan selalu memverifikasi sumber pesan.',
                'tags': ['Phishing', 'Social Engineering', 'BSSN'],
                'image_prompt': 'smartphone screen with fake message phishing link warning icon'
            },
            {
                'title': 'OJK Terbitkan Panduan Keamanan Siber Baru untuk Aset Kripto',
                'content': 'Merespons insiden peretasan bursa kripto Indodax, Otoritas Jasa Keuangan (OJK) merilis pedoman keamanan siber ketat bagi penyelenggara perdagangan aset kripto. Pedoman ini mewajibkan audit keamanan berkala, penerapan autentikasi multi-faktor (MFA), dan penyimpanan aset nasabah di cold wallet untuk meminimalisir risiko pencurian.',
                'tags': ['Crypto', 'OJK', 'Data Privacy'],
                'image_prompt': 'bitcoin coins protected by digital shield cyber security lock'
            },
            {
                'title': 'Ancaman "GoldFactory": Malware Android yang Kuras Rekening Bank',
                'content': 'Kelompok kejahatan siber GoldFactory terdeteksi aktif menyebarkan malware perbankan di Indonesia. Malware ini disusupkan melalui aplikasi palsu yang terlihat sah. Setelah terinstal, malware dapat mengambil alih kontrol perangkat, membaca SMS OTP, dan melakukan transaksi tanpa sepengetahuan korban. Ahli keamanan menyarankan pengguna hanya mengunduh aplikasi dari toko resmi.',
                'tags': ['Malware', 'Phishing', 'Social Engineering'],
                'image_prompt': 'android phone infected with goldfactory malware stealing money digital concept'
            },
            {
                'title': 'Kebocoran Data BKN: 4,7 Juta Data ASN Diduga Dijual di Dark Web',
                'content': 'Insiden kebocoran data kembali terjadi di instansi pemerintah. Kali ini, Badan Kepegawaian Negara (BKN) mengonfirmasi adanya dugaan peretasan yang mengekspos data pribadi 4,7 juta Aparatur Sipil Negara (ASN). Data yang bocor meliputi NIK, nama lengkap, tanggal lahir, hingga nomor telepon, yang berpotensi disalahgunakan untuk penipuan identitas.',
                'tags': ['Data Breach', 'Data Privacy', 'BSSN'],
                'image_prompt': 'hacker selling id cards data on dark web laptop screen anonymous mask'
            },
            {
                'title': 'Tren Serangan Siber 2025: AI Digunakan untuk Membuat Email Phishing',
                'content': 'Para ahli keamanan siber memprediksi bahwa tahun 2025 akan diwarnai dengan serangan phishing yang didukung oleh Artificial Intelligence (AI). Pelaku kejahatan menggunakan AI untuk membuat email penipuan yang sangat meyakinkan, bebas dari kesalahan tata bahasa, dan dipersonalisasi untuk target tertentu, sehingga semakin sulit dideteksi oleh filter keamanan tradisional.',
                'tags': ['Phishing', 'Social Engineering', 'Zero Day'],
                'image_prompt': 'robot typing on laptop creating fake emails artificial intelligence hacker'
            },
            {
                'title': 'Pemerintah Siapkan RUU Keamanan dan Ketahanan Siber',
                'content': 'Pemerintah Indonesia mempercepat pembahasan Rancangan Undang-Undang (RUU) Keamanan dan Ketahanan Siber. Regulasi ini diharapkan dapat menjadi payung hukum yang kuat dalam penanganan insiden siber, mewajibkan pelaporan insiden bagi sektor vital, dan memperkuat wewenang BSSN sebagai koordinator keamanan siber nasional.',
                'tags': ['BSSN', 'Data Privacy'],
                'image_prompt': 'gavel and law book with digital circuit board background cyber law concept'
            },
            {
                'title': 'Tips Mengamankan Akun Media Sosial dari Serangan Brute Force',
                'content': 'Serangan brute force terhadap akun media sosial pejabat dan figur publik semakin marak. Pengguna disarankan untuk menggunakan password yang panjang dan kompleks, mengaktifkan Two-Factor Authentication (2FA), dan rutin mengganti password. Artikel ini memberikan panduan langkah demi langkah untuk meningkatkan keamanan akun digital Anda.',
                'tags': ['Social Engineering', 'Data Privacy'],
                'image_prompt': 'padlock on smartphone screen social media icons protection shield'
            }
        ]

        print(f"Adding {len(articles_data)} cyber security articles...")

        for article_data in articles_data:
            # Check if article exists
            existing_article = Article.query.filter_by(title=article_data['title']).first()
            if existing_article:
                print(f"Skipping existing article: {article_data['title']}")
                continue

            # Get tags
            article_tags = []
            for tag_name in article_data['tags']:
                if tag_name in tags_map:
                    article_tags.append(tags_map[tag_name])

            # Generate Image URL
            image_url = f"https://image.pollinations.ai/prompt/{article_data['image_prompt'].replace(' ', '%20')}?width=800&height=600&nologo=true"

            # Create Article
            article = Article(
                title=article_data['title'],
                content=article_data['content'],
                image_url=image_url,
                published_date=datetime.now() - timedelta(days=random.randint(0, 14)),
                author_name=admin.full_name,
                category_id=cyber_cat.id
            )
            
            # Add tags
            article.tags = article_tags
            
            db.session.add(article)
            print(f"Added article: {article.title}")

        db.session.commit()
        print("Seeding completed successfully!")

if __name__ == '__main__':
    seed_cyber_expansion()
