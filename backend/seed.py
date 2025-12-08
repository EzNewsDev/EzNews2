"""Database seeder with realistic Indonesian news content"""

from app import create_app, db
from app.models import User, Article, Category, Tag, Bookmark
from datetime import datetime, timedelta
import random

app = create_app()


def seed_database():
    """Seed the database with initial data"""
    with app.app_context():
        # Drop all tables and recreate
        print("Dropping all tables...")
        db.drop_all()
        
        print("Creating all tables...")
        db.create_all()
        
        # Create admin user
        print("Creating admin user...")
        admin = User(
            full_name="Admin EzNews",
            email="admin@eznews.com",
            role="admin"
        )
        admin.set_password("Admin123!")
        db.session.add(admin)
        
        # Create regular user
        print("Creating regular user...")
        user = User(
            full_name="Budi Santoso",
            email="user@eznews.com",
            role="user"
        )
        user.set_password("User123!")
        db.session.add(user)
        
        db.session.commit()
        
        # Create categories
        print("Creating categories...")
        categories = [
            Category(name="Politik", slug="politik"),
            Category(name="Ekonomi", slug="ekonomi"),
            Category(name="Teknologi", slug="teknologi"),
            Category(name="Olahraga", slug="olahraga"),
            Category(name="Kesehatan", slug="kesehatan"),
            Category(name="Hiburan", slug="hiburan"),
            Category(name="Pendidikan", slug="pendidikan"),
        ]
        
        for cat in categories:
            db.session.add(cat)
        
        db.session.commit()
        
        # Create tags
        print("Creating tags...")
        tags_data = [
            ("Breaking News", "breaking-news"),
            ("Viral", "viral"),
            ("Trending", "trending"),
            ("Investigasi", "investigasi"),
            ("Opini", "opini"),
            ("Internasional", "internasional"),
            ("Nasional", "nasional"),
            ("Daerah", "daerah"),
        ]
        
        tags = []
        for name, slug in tags_data:
            tag = Tag(name=name, slug=slug)
            db.session.add(tag)
            tags.append(tag)
        
        db.session.commit()
        
        # Create articles with realistic Indonesian news content
        print("Creating articles...")
        
        articles_data = [
            {
                "title": "Presiden Jokowi Resmikan Pembangunan Ibu Kota Nusantara di Kalimantan Timur",
                "content": """Jakarta - Presiden Joko Widodo (Jokowi) secara resmi meresmikan pembangunan Ibu Kota Nusantara (IKN) di Kalimantan Timur pada hari Senin kemarin. Peresmian ini menandai dimulainya era baru bagi Indonesia dengan pemindahan pusat pemerintahan dari Jakarta.

Dalam sambutannya, Presiden Jokowi menekankan bahwa pembangunan IKN bukan hanya sekadar memindahkan gedung-gedung pemerintahan, tetapi juga menciptakan kota yang berkelanjutan, ramah lingkungan, dan berbasis teknologi modern.

"IKN akan menjadi simbol transformasi Indonesia menuju negara maju. Kita akan membangun kota yang hijau, pintar, dan inklusif," ujar Presiden Jokowi di hadapan ribuan tamu undangan.

Pembangunan tahap pertama difokuskan pada infrastruktur dasar seperti jalan, jembatan, sistem air bersih, dan jaringan listrik. Pemerintah menargetkan kantor-kantor utama dapat beroperasi di IKN pada tahun 2024.

Sementara itu, Menteri PUPR Basuki Hadimuljono menjelaskan bahwa pembangunan IKN melibatkan investasi swasta yang cukup besar. "Kami membuka peluang kerjasama dengan investor dalam dan luar negeri untuk membangun kawasan komersial, perumahan, dan fasilitas umum," katanya.""",
                "category": "Politik",
                "tags": ["Breaking News", "Nasional"],
                "author": "Ahmad Fauzi",
                "published_days_ago": 1,
                "image": "https://images.unsplash.com/photo-1523345863760-5b7f3472d14f?w=800"
            },
            {
                "title": "Bank Indonesia Pertahankan Suku Bunga Acuan di Level 5.75 Persen",
                "content": """Jakarta - Bank Indonesia (BI) memutuskan untuk mempertahankan suku bunga acuan (BI Rate) di level 5,75 persen pada Rapat Dewan Gubernur (RDG) bulan ini. Keputusan ini diambil setelah mempertimbangkan kondisi inflasi dalam negeri dan stabilitas nilai tukar rupiah.

Gubernur BI Perry Warjiyo mengatakan, kebijakan ini konsisten dengan upaya menjaga inflasi tetap terkendali sekaligus mendukung pertumbuhan ekonomi. "Kami melihat inflasi masih dalam tren penurunan dan ekonomi menunjukkan pertumbuhan yang solid," ujarnya.

Inflasi tahun kalender (ytd) tercatat 2,56 persen, masih dalam rentang sasaran inflasi 2023 sebesar 3±1 persen. Sementara itu, pertumbuhan ekonomi Indonesia di kuartal III mencapai 4,94 persen year-on-year.

BI juga terus memperkuat stabilitas nilai tukar Rupiah melalui operasi moneter di pasar valas dan Pasar Domestik Non-Deliverable Forward (DNDF). Per hari ini, nilai tukar Rupiah berada di level Rp 15.400 per dolar AS.

Para ekonom menilai keputusan BI cukup tepat mengingat masih ada ketidakpastian ekonomi global akibat kebijakan moneter Amerika Serikat dan konflik geopolitik di beberapa kawasan.""",
                "category": "Ekonomi",
                "tags": ["Trending", "Nasional"],
                "author": "Siti Nurhaliza",
                "published_days_ago": 2,
                "image": "https://images.unsplash.com/photo-1634128221889-82ed6efebfc3?w=800"
            },
            {
                "title": "Peluncuran Satelit Merah Putih 2 Sukses, Indonesia Makin Mandiri di Bidang Telekomunikasi",
                "content": """Jakarta - Indonesia berhasil meluncurkan satelit Merah Putih 2 dari Cape Canaveral, Florida, Amerika Serikat menggunakan roket Falcon 9 milik SpaceX. Peluncuran yang dilakukan pada Selasa dini hari WIB ini berjalan dengan sukses dan satelit telah memasuki orbit geostasioner.

Menteri Komunikasi dan Informatika Budi Arie Setiadi menyambut gembira keberhasilan ini. "Peluncuran Merah Putih 2 merupakan tonggak penting bagi kemandirian Indonesia di sektor telekomunikasi. Satelit ini akan meningkatkan kapasitas layanan internet dan telekomunikasi di seluruh Indonesia, terutama daerah 3T (Terdepan, Terluar, Tertinggal)," katanya.

Satelit Merah Putih 2 memiliki 32 transponder C-band dan 8 transponder Extended C-band dengan masa operasional minimal 15 tahun. Kapasitas ini jauh lebih besar dibanding satelit sebelumnya.

Direktur Utama PT Telkom Ririek Kumar menambahkan bahwa satelit ini akan mendukung program transformasi digital nasional. "Dengan Merah Putih 2, kami dapat menyediakan layanan broadband satellite untuk wilayah yang belum terjangkau jaringan fiber optik," jelasnya.

Para ahli telekomunikasi menilai investasi di bidang satelit sangat strategis mengingat Indonesia adalah negara kepulauan dengan lebih dari 17.000 pulau.""",
                "category": "Teknologi",
                "tags": ["Breaking News", "Nasional"],
                "author": "Dimas Prasetyo",
                "published_days_ago": 1,
                "image": "https://images.unsplash.com/photo-1446776653964-20c1d3a81b06?w=800"
            },
            {
                "title": "Timnas Indonesia Lolos ke Putaran Final Piala Asia 2024 Setelah Kalahkan Vietnam 3-0",
                "content": """Jakarta - Timnas Indonesia berhasil meraih kemenangan gemilang 3-0 atas Vietnam dalam laga kualifikasi terakhir Piala Asia 2024 yang berlangsung di Stadion Gelora Bung Karno. Kemenangan ini memastikan Garuda mendapat tiket ke putaran final yang akan diselenggarakan di Qatar.

Gol-gol kemenangan Indonesia dicetak oleh Egy Maulana Vikri (15'), Witan Sulaeman (34'), dan Marselino Ferdinan (78'). Penampilan gemilang skuad Shin Tae-yong ini disambut meriah oleh 78.000 penonton yang memadati stadion.

Pelatih Shin Tae-yong mengungkapkan kebanggaannya. "Para pemain telah bekerja sangat keras selama persiapan. Ini adalah hasil kerja tim yang solid. Kami akan terus berbenah untuk tampil maksimal di putaran final," ujarnya dalam konferensi pers.

Kiper Ernando Ari menjadi salah satu pemain terbaik dengan beberapa penyelamatan gemilang. "Ini kemenangan untuk seluruh rakyat Indonesia. Kami ingin membuat sejarah di Piala Asia nanti," kata Ernando.

Lolosnya Indonesia ke putaran final Piala Asia 2024 merupakan pencapaian bersejarah setelah terakhir kali tampil pada tahun 2007. Suporter optimis tim bisa melampaui prestasi masa lalu.

Menpora Dito Ariotedjo mengapresiasi pencapaian ini dan berjanji akan memberikan dukungan penuh untuk persiapan tim menuju putaran final.""",
                "category": "Olahraga",
                "tags": ["Trending", "Viral", "Nasional"],
                "author": "Andi Wijaya",
                "published_days_ago": 0,
                "image": "https://images.unsplash.com/photo-1574629810360-7efbbe195018?w=800"
            },
            {
                "title": "Kemenkes Luncurkan Program Vaksinasi COVID-19 Booster Kedua untuk Lansia",
                "content": """Jakarta - Kementerian Kesehatan (Kemenkes) meluncurkan program vaksinasi booster kedua khusus untuk kelompok lansia berusia 60 tahun ke atas. Program ini merupakan upaya pemerintah memperkuat imunitas kelompok rentan di tengah kemunculan varian baru virus COVID-19.

Menteri Kesehatan Budi Gunadi Sadikin mengatakan, vaksinasi booster kedua penting untuk mempertahankan antibodi yang optimal. "Data menunjukkan antibodi dari vaksinasi sebelumnya mulai menurun setelah 6 bulan. Booster kedua akan mengembalikan perlindungan optimal, terutama bagi lansia," jelasnya.

Program ini menggunakan vaksin mRNA seperti Pfizer atau Moderna yang telah terbukti efektif meningkatkan respons imun. Pelaksanaan vaksinasi dilakukan di seluruh puskesmas, rumah sakit, dan sentra vaksinasi di Indonesia.

Juru Bicara Kemenkes dr. Mohammad Syahril menambahkan bahwa pendaftaran dapat dilakukan melalui aplikasi PeduliLindungi. "Kami menargetkan 10 juta lansia dapat divaksinasi dalam 3 bulan ke depan," katanya.

Ketua Perhimpunan Geriatri Indonesia (Pergeri) dr. Siti Setiati mendukung program ini. "Lansia memiliki sistem imun yang lebih lemah sehingga memerlukan perlindungan ekstra. Vaksinasi booster sangat direkomendasikan," ujarnya.

Hingga saat ini, cakupan vaksinasi booster pertama di Indonesia telah mencapai 62 persen dari total populasi.""",
                "category": "Kesehatan",
                "tags": ["Nasional", "Trending"],
                "author": "dr. Amalia Putri",
                "published_days_ago": 3,
                "image": "https://images.unsplash.com/photo-1584515933487-779824d29309?w=800"
            },
            {
                "title": "Film Indonesia 'Siksa Neraka' Pecahkan Rekor 6 Juta Penonton dalam 2 Minggu",
                "content": """Jakarta - Film horor Indonesia 'Siksa Neraka' berhasil menorehkan prestasi gemilang dengan menembus angka 6 juta penonton hanya dalam waktu 2 minggu sejak tayang. Pencapaian ini memecahkan rekor sebagai film Indonesia dengan penonton tercepat sepanjang masa.

Produser Manoj Punjabi mengungkapkan rasa syukurnya. "Kami tidak menyangka antusiasme penonton sebesar ini. Siksa Neraka adalah bukti bahwa film Indonesia berkualitas bisa bersaing dan bahkan mengalahkan film-film Hollywood," ujarnya.

Sutradara Anggy Umbara mengatakan kesuksesan film ini berkat cerita yang kuat dan eksekusi yang matang. "Kami menggarap film ini selama 2 tahun, dari riset cerita hingga post production. Hasil yang kami dapatkan sekarang adalah buah dari kerja keras seluruh tim," katanya.

Film yang dibintangi oleh Safira Ratu Sofya, Ariyo Wahab, dan Slamet Rahardjo ini mengangkat tema tentang konsekuensi perbuatan di dunia terhadap kehidupan setelah mati. Visual efek yang memukau dan alur cerita yang mencekam menjadi daya tarik utama.

Pengamat film Dr. Hikmat Darmawan menilai kesuksesan Siksa Neraka menunjukkan kebangkitan industri film Indonesia. "Ini momentum yang tepat bagi para sineas untuk terus berkarya dan mengangkat standar perfilman Indonesia ke level internasional," ujarnya.

Di platform streaming internasional, Siksa Neraka juga trending di beberapa negara Asia Tenggara.""",
                "category": "Hiburan",
                "tags": ["Viral", "Trending"],
                "author": "Rahma Safitri",
                "published_days_ago": 4,
                "image": "https://images.unsplash.com/photo-1489599849927-2ee91cede3ba?w=800"
            },
            {
                "title": "Kemendikbud Luncurkan Kurikulum Merdeka untuk Tingkat SD hingga SMA",
                "content": """Jakarta - Kementerian Pendidikan, Kebudayaan, Riset, dan Teknologi (Kemendikbudristek) resmi meluncurkan Kurikulum Merdeka untuk jenjang SD hingga SMA pada tahun ajaran baru 2024. Kurikulum ini memberikan kebebasan lebih besar kepada guru dan siswa dalam proses pembelajaran.

Menteri Nadiem Makarim menjelaskan bahwa Kurikulum Merdeka dirancang untuk meningkatkan kualitas pembelajaran yang lebih relevan dengan kebutuhan zaman. "Kurikulum ini fokus pada pengembangan kompetensi, bukan sekadar hafalan. Siswa didorong untuk berpikir kritis, kreatif, dan kolaboratif," ujarnya.

Salah satu fitur utama Kurikulum Merdeka adalah adanya Projek Penguatan Profil Pelajar Pancasila (P5) yang mengajak siswa belajar melalui proyek nyata. Misalnya, siswa membuat proyek tentang lingkungan, kewirausahaan, atau kearifan lokal.

Kepala Badan Standar Kurikulum dan Asesmen Pendidikan (BSKAP) Anindito Aditomo menambahkan bahwa guru diberikan pelatihan intensif untuk mengimplementasikan kurikulum baru. "Kami telah melatih lebih dari 500.000 guru di seluruh Indonesia," katanya.

Sejumlah sekolah yang telah mengimplementasikan Kurikulum Merdeka melaporkan peningkatan motivasi belajar siswa. Kepala SD Negeri 1 Jakarta, Ibu Sari Dewi, mengatakan: "Siswa lebih antusias belajar karena materi lebih menarik dan aplikatif."

Namun, beberapa ahli pendidikan mengingatkan pentingnya monitoring implementasi agar tidak terjadi kesenjangan kualitas antar daerah.""",
                "category": "Pendidikan",
                "tags": ["Nasional", "Breaking News"],
                "author": "Prof. Dr. Indah Kusuma",
                "published_days_ago": 5,
                "image": "https://images.unsplash.com/photo-1503676260728-1c00da094a0b?w=800"
            },
            {
                "title": "Harga BBM Naik, Pemerintah Salurkan Subsidi Langsung ke Masyarakat Kurang Mampu",
                "content": """Jakarta - Pemerintah resmi menaikkan harga bahan bakar minyak (BBM) bersubsidi Pertalite dan Solar masing-masing Rp 500 per liter. Kenaikan ini berlaku mulai hari Senin depan di seluruh Indonesia sebagai respons terhadap kenaikan harga minyak dunia.

Menteri ESDM Arifin Tasrif menjelaskan bahwa kenaikan ini tidak dapat dihindari mengingat harga minyak mentah dunia yang terus merangkak naik. "Harga Brent crude oil saat ini di level USD 95 per barel. Jika pemerintah tetap mempertahankan harga BBM, beban subsidi akan membengkak dan mengancam APBN," ujarnya.

Untuk meringankan beban masyarakat, pemerintah menyiapkan paket kompensasi berupa Bantuan Langsung Tunai (BLT) sebesar Rp 200.000 per bulan selama 4 bulan bagi keluarga kurang mampu. Total dana kompensasi mencapai Rp 24,8 triliun.

Menko Perekonomian Airlangga Hartarto menekankan bahwa distribusi BLT akan dilakukan dengan sistem digital untuk memastikan tepat sasaran. "Data penerima menggunakan basis data terpadu kesejahteraan sosial (DTKS) yang telah diverifikasi dan validasi," katanya.

Dengan kenaikan ini, harga Pertalite menjadi Rp 11.000 per liter dan Solar menjadi Rp 10.500 per liter. Sementara Pertamax dan BBM non-subsidi lainnya mengikuti mekanisme pasar.

Pengamat ekonomi Faisal Basri menilai kebijakan ini sebagai langkah yang sulit namun diperlukan. "Subsidi BBM yang tidak tepat sasaran justru lebih menguntungkan kelompok mampu. Subsidi langsung lebih efektif membantu rakyat kecil," ungkapnya.""",
                "category": "Ekonomi",
                "tags": ["Breaking News", "Nasional"],
                "author": "Rudi Hermawan",
                "published_days_ago": 1,
                "image": "https://images.unsplash.com/photo-1519452575417-564c1401ecc0?w=800"
            },
            {
                "title": "Startup Teknologi Indonesia Go-Jek Ekspansi ke 5 Negara Asia Tenggara",
                "content": """Jakarta - Platform teknologi multiservis Go-Jek mengumumkan rencana ekspansi ambisius ke lima negara Asia Tenggara yaitu Malaysia, Thailand, Filipina, Vietnam, dan Myanmar. Langkah ini merupakan bagian dari strategi Go-Jek menjadi super app terdepan di kawasan regional.

CEO Go-Jek Kevin Aluwi mengatakan ekspansi ini didukung oleh pendanaan seri F senilai USD 2 miliar yang baru saja ditutup. "Kami melihat peluang besar di Asia Tenggara. Kebutuhan akan transportasi, logistik, dan pembayaran digital terus meningkat pasca pandemi," ujarnya dalam konferensi pers.

Strategi ekspansi Go-Jek mencakup kemitraan dengan perusahaan lokal di setiap negara. Di Malaysia, Go-Jek akan berkolaborasi dengan perusahaan telekomunikasi terkemuka, sementara di Thailand akan bermitra dengan ritel besar.

Co-Founder Nadiem Makarim yang kini menjabat sebagai Menteri Pendidikan menyambut baik langkah ini. "Go-Jek adalah kebanggaan Indonesia. Ekspansi mereka membuktikan bahwa startup Indonesia mampu bersaing di kancah global," katanya.

Analis teknologi Rudiantara memprediksi persaingan akan semakin ketat dengan Grab yang sudah lebih dulu hadir di kawasan. "Go-Jek harus menawarkan nilai tambah yang jelas untuk merebut pasar. Pengalaman mereka di Indonesia memberikan pembelajaran berharga," ujarnya.

Saat ini Go-Jek telah memiliki lebih dari 2 juta mitra driver dan merchant di Indonesia dengan total transaksi mencapai Rp 150 triliun per tahun.""",
                "category": "Teknologi",
                "tags": ["Trending", "Internasional"],
                "author": "Budi Santoso",
                "published_days_ago": 2,
                "image": "https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?w=800"
            },
            {
                "title": "Atlet Indonesia Raih 3 Emas di SEA Games 2023 Cabang Bulu Tangkis",
                "content": """Phnom Penh - Kontingen bulu tangkis Indonesia menorehkan prestasi gemilang di SEA Games 2023 dengan meraih tiga medali emas dari lima nomor yang dipertandingkan. Emas diperoleh dari nomor tunggal putra, ganda putra, dan beregu putra.

Anthony Sinisuka Ginting sukses merebut emas tunggal putra setelah mengalahkan wakil Thailand Kunlavut Vitidsarn dengan skor 21-18, 21-19. "Ini untuk Indonesia. Saya bersyukur bisa tampil maksimal dan mengharumkan nama bangsa," ujar Anthony usai pertandingan.

Di nomor ganda putra, Kevin Sanjaya/Marcus Gideon yang dijuluki "The Minions" kembali menunjukkan dominasi dengan mengalahkan pasangan Malaysia 21-15, 21-17. Kemenangan telak ini semakin memantapkan posisi mereka sebagai pasangan terbaik dunia.

Sementara tim beregu putra yang terdiri dari Jonatan Christie, Fajar Alfian/Rian Ardianto, dan Hendra Setiawan/Mohammad Ahsan berhasil merebut emas setelah mengalahkan Malaysia 3-1 di final.

Ketua Umum PBSI Agung Firman Sampurna mengapresiasi pencapaian ini. "Prestasi di SEA Games adalah modal untuk menghadapi turnamen yang lebih besar seperti Olimpiade Paris 2024. Kami akan terus memberikan dukungan penuh kepada atlet," katanya.

Menpora Dito Ariotedjo yang hadir langsung di venue memberikan bonus khusus bagi para peraih medali emas. Total Indonesia meraih 8 medali emas dari cabang bulu tangkis.

Target Indonesia adalah finish di tiga besar klasemen umum SEA Games dengan minimal 100 medali emas.""",
                "category": "Olahraga",
                "tags": ["Internasional", "Viral"],
                "author": "Hendra Kusuma",
                "published_days_ago": 6,
                "image": "https://images.unsplash.com/photo-1626224583764-f87db24ac4ea?w=800"
            },
            {
                "title": "WHO Tetapkan Status Darurat Global untuk Wabah Cacar Monyet",
                "content": """Jenewa - Organisasi Kesehatan Dunia (WHO) menetapkan wabah cacar monyet (monkeypox) sebagai darurat kesehatan global atau Public Health Emergency of International Concern (PHEIC). Keputusan ini diambil setelah kasus meningkat drastis di lebih dari 75 negara.

Direktur Jenderal WHO Tedros Adhanom Ghebreyesus mengatakan penetapan status darurat ini bertujuan mempercepat koordinasi internasional dalam penanganan wabah. "Kami perlu respons global yang terkoordinasi untuk menghentikan penyebaran virus ini," ujarnya.

Hingga saat ini, tercatat lebih dari 16.000 kasus cacar monyet di seluruh dunia dengan 5 kasus kematian. Mayoritas kasus terjadi di Eropa dan Amerika, namun mulai menyebar ke Asia dan Afrika.

Kemenkes RI telah memperketat pengawasan di pintu masuk negara dan menyiapkan protokol penanganan. "Kami melakukan screening ketat di bandara dan pelabuhan. Fasilitas kesehatan juga sudah disiapkan untuk isolasi dan perawatan," kata Juru Bicara Kemenkes.

Gejala cacar monyet meliputi demam, sakit kepala, nyeri otot, dan ruam kulit yang berkembang menjadi benjolan berisi cairan. Penularan terjadi melalui kontak fisik erat dengan penderita.

Para ahli kesehatan mengimbau masyarakat untuk tidak panik namun tetap waspada. "Cacar monyet tidak semudah COVID-19 dalam penularan. Dengan protokol kesehatan yang baik, penyebaran bisa dicegah," ujar epidemiolog Prof. Dr. Pandu Riono.

WHO mendorong negara-negara untuk meningkatkan surveilans dan akses terhadap vaksin cacar monyet.""",
                "category": "Kesehatan",
                "tags": ["Breaking News", "Internasional"],
                "author": "dr. Siska Amelia",
                "published_days_ago": 3,
                "image": "https://images.unsplash.com/photo-1631815588090-d4bfec5b1ccb?w=800"
            },
            {
                "title": "Konser Coldplay di Jakarta Sold Out dalam 30 Menit, Promotor Tambah 2 Hari Show",
                "content": """Jakarta - Tiket konser Coldplay di Stadion Utama Gelora Bung Karno (GBK) ludes terjual hanya dalam waktu 30 menit sejak dibuka. Antusiasme luar biasa dari penggemar membuat promotor PK Entertainment mengumumkan penambahan dua hari show.

Direktur PK Entertainment Arief Wicaksono mengatakan pihaknya tidak menyangka respons sangat masif. "Ini konser internasional dengan penjualan tiket tercepat dalam sejarah Jakarta. Kami langsung koordinasi dengan management Coldplay dan Alhamdulillah disetujui penambahan show," ujarnya.

Konser yang awalnya dijadwalkan 15 November 2024 kini bertambah menjadi 13, 14, dan 15 November. Total kapasitas penonton mencapai 240.000 orang dengan harga tiket mulai dari Rp 1,5 juta hingga Rp 11 juta.

Coldplay akan membawakan lagu-lagu hits seperti "Yellow", "The Scientist", "Viva La Vida", "Fix You", dan lagu-lagu dari album terbaru "Music of the Spheres". Konser ini juga bagian dari tur dunia mereka yang mengusung konsep ramah lingkungan.

Chris Martin selaku vokalis Coldplay mengungkapkan kegembiraannya melalui video message. "Indonesia! We can't wait to play for you. It's going to be an incredible show with lots of surprises!" ujarnya.

Penggemar Indonesia sangat antusias terutama karena ini adalah kunjungan kedua Coldplay setelah terakhir kali manggung pada tahun 2009. "Saya sudah menunggu 15 tahun! Apapun akan saya lakukan untuk bisa nonton," kata Rani, salah seorang penggemar.

Pemerintah DKI Jakarta sudah menyiapkan pengamanan ekstra dan sistem transportasi khusus untuk mengantisipasi lonjakan penonton.""",
                "category": "Hiburan",
                "tags": ["Viral", "Trending", "Nasional"],
                "author": "Dewi Lestari",
                "published_days_ago": 7,
                "image": "https://images.unsplash.com/photo-1540039155733-5bb30b53aa14?w=800"
            },
            {
                "title": "Kemendikbud Resmikan Beasiswa LPDP untuk 1000 Mahasiswa S2-S3 Luar Negeri",
                "content": """Jakarta - Kementerian Pendidikan, Kebudayaan, Riset, dan Teknologi melalui Lembaga Pengelola Dana Pendidikan (LPDP) resmi membuka program beasiswa untuk 1000 mahasiswa Indonesia yang ingin melanjutkan studi S2 dan S3 di universitas terkemuka luar negeri.

Menteri Nadiem Makarim mengatakan program ini bertujuan mencetak generasi unggul yang dapat berkontribusi bagi kemajuan Indonesia. "Kami mengalokasikan dana Rp 5 triliun untuk program beasiswa tahun ini. Fokusnya pada bidang STEM, kesehatan, dan ekonomi digital," ujarnya.

Kepala LPDP Riset Akbar menjelaskan bahwa penerima beasiswa akan mendapat pembiayaan penuh meliputi biaya kuliah, biaya hidup, tiket pesawat, asuransi kesehatan, dan tunjangan buku. "Kami juga memberikan dana riset untuk mahasiswa S3," katanya.

Pendaftaran dibuka mulai hari ini hingga 30 Mei 2024 melalui website resmi LPDP. Persyaratan meliputi IPK minimal 3.0 untuk S2 dan 3.25 untuk S3, skor TOEFL iBT minimal 80 atau IELTS 6.5, serta letter of acceptance (LoA) dari universitas tujuan.

Universitas target mencakup perguruan tinggi top dunia seperti Harvard, MIT, Stanford, Oxford, Cambridge, dan National University of Singapore (NUS). "Kami sudah membuat MoU dengan 150 universitas terkemuka," tambah Riset.

Alumni beasiswa LPDP wajib kembali ke Indonesia dan mengabdi minimal 2 tahun untuk S2 dan 3 tahun untuk S3. "Mereka akan ditempatkan di instansi pemerintah, BUMN, atau institusi pendidikan sesuai keahlian," jelasnya.

Sejak diluncurkan tahun 2013, LPDP telah memberangkatkan lebih dari 30.000 mahasiswa ke berbagai negara dengan tingkat kelulusan 95 persen.""",
                "category": "Pendidikan",
                "tags": ["Breaking News", "Nasional"],
                "author": "Prof. Dr. Hadi Susanto",
                "published_days_ago": 2,
                "image": "https://images.unsplash.com/photo-1523050854058-8df90110c9f1?w=800"
            },
            {
                "title": "BPS: Tingkat Pengangguran Indonesia Turun Menjadi 5.3 Persen di Kuartal III 2023",
                "content": """Jakarta - Badan Pusat Statistik (BPS) melaporkan Tingkat Pengangguran Terbuka (TPT) Indonesia turun menjadi 5,32 persen pada Agustus 2023, atau turun 0,45 persen poin dibandingkan Agustus 2022 yang sebesar 5,77 persen.

Kepala BPS Margo Yuwono mengatakan penurunan tingkat pengangguran ini sejalan dengan pemulihan ekonomi nasional pasca pandemi. "Jumlah angkatan kerja meningkat 2,78 juta orang, dan yang bekerja bertambah 3,74 juta orang," ujarnya dalam konferensi pers.

Secara absolut, jumlah pengangguran berkurang dari 8,40 juta orang menjadi 7,86 juta orang. Penurunan terjadi di hampir semua kelompok umur, terutama kelompok usia muda 15-24 tahun.

Sektor yang paling banyak menyerap tenaga kerja adalah sektor jasa, perdagangan, dan industri manufaktur. "Investasi yang masuk ke Indonesia membuka banyak lapangan pekerjaan baru," tambah Margo.

Namun demikian, kualitas pekerjaan masih menjadi perhatian. Jumlah pekerja informal masih tinggi mencapai 58,92 persen dari total pekerja. "Pemerintah fokus pada upskilling dan reskilling tenaga kerja agar bisa bersaing di era digital," kata Wakil Menteri Ketenagakerjaan Afriansyah Noor.

Menko Perekonomian Airlangga Hartarto menargetkan TPT bisa ditekan hingga di bawah 5 persen pada akhir 2024. "Kami terus mendorong pertumbuhan ekonomi inklusif yang membuka akses pekerjaan layak bagi semua kalangan," ujarnya.

Pemerintah juga meluncurkan program Kartu Prakerja dan pelatihan vokasi untuk meningkatkan kompetensi pencari kerja.""",
                "category": "Ekonomi",
                "tags": ["Nasional", "Trending"],
                "author": "Eko Prasetyo",
                "published_days_ago": 8,
                "image": "https://images.unsplash.com/photo-1507679799987-c73779587ccf?w=800"
            },
            {
                "title": "Google Luncurkan Cloud Region Baru di Indonesia dengan Investasi USD 1 Miliar",
                "content": """Jakarta - Google Cloud mengumumkan pembukaan region cloud baru di Jakarta dengan investasi mencapai USD 1 miliar. Ini merupakan cloud region ketiga Google di Asia Tenggara setelah Singapura dan Malaysia.

Country Director Google Indonesia Randy Jusuf mengatakan kehadiran cloud region di Indonesia merespons permintaan tinggi dari perusahaan lokal yang ingin transformasi digital. "Data center lokal memastikan latensi rendah, keamanan data, dan kepatuhan terhadap regulasi Indonesia," ujarnya.

Fasilitas cloud region Google di Jakarta terdiri dari tiga availability zones yang berlokasi terpisah untuk memastikan redundansi dan ketersediaan tinggi. Infrastruktur ini mampu mendukung berbagai layanan mulai dari compute, storage, hingga AI/ML.

Menteri Komunikasi dan Informatika Budi Arie memuji investasi ini sebagai kepercayaan terhadap ekonomi digital Indonesia. "Kehadiran hyperscaler seperti Google akan mempercepat adopsi cloud di berbagai sektor termasuk pemerintahan, perbankan, dan retail," katanya.

Beberapa perusahaan besar Indonesia seperti Gojek, Tokopedia, dan Bank Mandiri berkomitmen menggunakan Google Cloud region Jakarta. "Kami akan memigrasikan beberapa workload kritik to local cloud untuk comply dengan regulasi," kata CTO Gojek Niranjan Paranjape.

Google juga mengumumkan program pelatihan cloud untuk 100.000 developer Indonesia dan kemitraan dengan universitas untuk kurikulum cloud computing. "Kami ingin berkontribusi membangun talenta digital Indonesia," tambah Randy.

Investasi Google menyusul AWS dan Microsoft Azure yang lebih dulu membangun cloud region di Indonesia.""",
                "category": "Teknologi",
                "tags": ["Breaking News", "Nasional", "Internasional"],
                "author": "Arief Budiman",
                "published_days_ago": 4,
                "image": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=800"
            },
        ]
        
        for idx, article_data in enumerate(articles_data, 1):
            print(f"Creating article {idx}/{len(articles_data)}: {article_data['title'][:50]}...")
            
            # Find category
            category = Category.query.filter_by(name=article_data['category']).first()
            
            # Calculate published date
            published_date = datetime.utcnow() - timedelta(days=article_data['published_days_ago'])
            
            # Create article
            article = Article(
                title=article_data['title'],
                content=article_data['content'],
                category_id=category.id,
                author_name=article_data['author'],
                source_url="https://www.eznews.com",
                image_url=article_data['image'],
                published_date=published_date
            )
            
            # Add tags
            article_tags = []
            for tag_name in article_data['tags']:
                tag = Tag.query.filter_by(name=tag_name).first()
                if tag:
                    article_tags.append(tag)
            article.tags = article_tags
            
            db.session.add(article)
        
        db.session.commit()
        
        # Create sample bookmarks
        print("Creating sample bookmarks...")
        bookmark1 = Bookmark(user_id=user.id, article_id=1)
        bookmark2 = Bookmark(user_id=user.id, article_id=3)
        bookmark3 = Bookmark(user_id=user.id, article_id=5)
        
        db.session.add_all([bookmark1, bookmark2, bookmark3])
        db.session.commit()
        
        print("\n✅ Database seeded successfully!")
        print("\n📊 Summary:")
        print(f"   - Users: {User.query.count()}")
        print(f"   - Categories: {Category.query.count()}")
        print(f"   - Tags: {Tag.query.count()}")
        print(f"   - Articles: {Article.query.count()}")
        print(f"   - Bookmarks: {Bookmark.query.count()}")
        print("\n🔐 Login credentials:")
        print("   Admin: admin@eznews.com / Admin123!")
        print("   User:  user@eznews.com / User123!")


if __name__ == '__main__':
    seed_database()
