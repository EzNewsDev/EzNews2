"""Database seeder with 30 realistic Indonesian news articles (Long Content)"""

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
        categories_data = [
            ("Politik", "politik"),
            ("Ekonomi", "ekonomi"),
            ("Teknologi", "teknologi"),
            ("Olahraga", "olahraga"),
            ("Kesehatan", "kesehatan"),
            ("Hiburan", "hiburan"),
            ("Pendidikan", "pendidikan"),
        ]
        
        for name, slug in categories_data:
            db.session.add(Category(name=name, slug=slug))
        
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
        
        for name, slug in tags_data:
            db.session.add(Tag(name=name, slug=slug))
        
        db.session.commit()
        
        # Create articles
        print("Creating 30 articles...")
        
        articles_data = [
            # POLITIK (5)
            {
                "title": "Presiden Resmikan Pembangunan Infrastruktur Baru di Papua",
                "content": """Presiden Joko Widodo kembali melakukan kunjungan kerja ke Provinsi Papua untuk meresmikan sejumlah proyek infrastruktur strategis yang telah rampung dikerjakan. Dalam kunjungan kali ini, Presiden meresmikan jalan trans-Papua segmen terbaru sepanjang 50 kilometer serta dua jembatan gantung yang menghubungkan desa-desa terisolir. Pembangunan ini merupakan bagian dari komitmen pemerintah untuk mempercepat pemerataan pembangunan di wilayah timur Indonesia, khususnya di Papua dan Papua Barat.

Dalam sambutannya di hadapan ribuan masyarakat yang hadir, Presiden menekankan bahwa infrastruktur bukan hanya soal fisik bangunan, melainkan soal keadilan sosial. "Kita ingin saudara-saudara kita di Papua merasakan harga barang yang sama dengan di Jawa. Kita ingin akses pendidikan dan kesehatan menjadi mudah. Itulah mengapa kita bangun jalan, jembatan, dan pelabuhan di sini," tegas Presiden yang disambut tepuk tangan meriah. Presiden juga berdialog langsung dengan tokoh adat setempat untuk mendengar aspirasi mereka terkait pengembangan wilayah ke depan.

Menteri Pekerjaan Umum dan Perumahan Rakyat (PUPR) yang turut mendampingi Presiden menjelaskan bahwa tantangan pembangunan di Papua sangatlah berat karena kondisi geografis yang ekstrem. Namun, berkat kerja keras para insinyur dan dukungan keamanan dari TNI/Polri, proyek-proyek ini dapat diselesaikan tepat waktu. "Jembatan ini menggunakan teknologi tahan gempa dan dirancang untuk bertahan hingga 100 tahun," ujar Menteri PUPR saat memberikan laporan teknis.

Masyarakat setempat menyambut antusias peresmian ini. Salah satu warga, Markus, mengaku sangat bersyukur karena kini ia bisa membawa hasil kebunnya ke pasar kota dengan waktu tempuh yang jauh lebih singkat. "Dulu butuh waktu 2 hari jalan kaki, sekarang cuma 2 jam naik motor," katanya dengan mata berkaca-kaca. Pembangunan infrastruktur ini diharapkan dapat memicu pertumbuhan ekonomi lokal dan meningkatkan kesejahteraan masyarakat Papua secara signifikan dalam beberapa tahun mendatang.""",
                "category": "Politik",
                "tags": ["Nasional", "Breaking News"],
                "author": "Ahmad Fauzi",
                "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Joko_Widodo_2019_official_portrait.jpg/600px-Joko_Widodo_2019_official_portrait.jpg"
            },
            {
                "title": "KPU Tetapkan Jadwal Debat Capres-Cawapres 2024",
                "content": """Komisi Pemilihan Umum (KPU) Republik Indonesia akhirnya resmi merilis jadwal lengkap debat calon presiden (capres) dan calon wakil presiden (cawapres) untuk Pemilihan Umum (Pemilu) 2024. Pengumuman ini disampaikan langsung oleh Ketua KPU dalam konferensi pers yang digelar di kantor KPU Pusat, Jakarta, hari ini. Debat akan dilaksanakan sebanyak lima kali, terdiri dari tiga kali debat capres dan dua kali debat cawapres, dengan tema yang berbeda-beda di setiap sesinya.

Tema debat pertama akan berfokus pada isu hukum, hak asasi manusia (HAM), pemerintahan, pemberantasan korupsi, dan penguatan demokrasi. Debat kedua akan membahas ekonomi kerakyatan, ekonomi digital, keuangan, investasi, pajak, perdagangan, pengelolaan APBN/APBD, infrastruktur, dan perkotaan. Sementara itu, debat-debat selanjutnya akan mengangkat topik pertahanan, keamanan, hubungan internasional, geopolitik, pembangunan berkelanjutan, sumber daya alam, lingkungan hidup, energi, pangan, agraria, masyarakat adat, dan desa.

Ketua KPU menyatakan bahwa debat ini menjadi sarana yang sangat krusial bagi masyarakat untuk menilai kualitas, visi, dan misi para kandidat pemimpin bangsa. "Kami ingin pemilih mendapatkan informasi yang utuh dan mendalam tentang gagasan para paslon. Debat ini bukan sekadar tontonan, tapi tuntunan dalam menentukan pilihan," ujarnya. KPU juga telah menunjuk panelis dari kalangan akademisi, profesional, dan tokoh masyarakat yang memiliki integritas dan kompetensi di bidangnya masing-masing.

Stasiun televisi nasional akan menyiarkan secara langsung seluruh rangkaian debat tersebut pada jam 19.00 WIB. KPU menghimbau kepada seluruh tim sukses dan pendukung paslon untuk menjaga ketertiban dan kondusivitas selama debat berlangsung, baik di dalam maupun di luar arena debat. Diharapkan, debat ini dapat berjalan dengan santun, edukatif, dan substansial, sehingga dapat meningkatkan kualitas demokrasi di Indonesia.""",
                "category": "Politik",
                "tags": ["Nasional", "Trending"],
                "author": "Siti Aminah",
                "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Gedung_KPU_RI.jpg/800px-Gedung_KPU_RI.jpg"
            },
            {
                "title": "DPR Sahkan RUU Kesehatan Menjadi Undang-Undang",
                "content": """Dewan Perwakilan Rakyat (DPR) RI akhirnya mengesahkan Rancangan Undang-Undang (RUU) Kesehatan menjadi Undang-Undang dalam rapat paripurna yang digelar hari ini di Gedung Nusantara II, Kompleks Parlemen, Senayan, Jakarta. Pengesahan ini dilakukan setelah melalui proses pembahasan yang panjang dan alot antara pemerintah dan DPR, serta diwarnai dengan berbagai dinamika dan perdebatan publik. Palu sidang diketuk oleh Ketua DPR RI menandakan persetujuan mayoritas fraksi terhadap RUU tersebut.

Menteri Kesehatan yang hadir mewakili pemerintah menyambut baik pengesahan ini sebagai tonggak sejarah baru reformasi sistem kesehatan nasional. Dalam pidato pendapat akhir pemerintah, Menkes menegaskan bahwa UU Kesehatan yang baru ini akan fokus pada penguatan layanan kesehatan primer, pemerataan distribusi tenaga kesehatan, dan pemanfaatan teknologi kesehatan. "UU ini adalah wujud komitmen negara untuk menjamin hak setiap warga negara mendapatkan pelayanan kesehatan yang berkualitas dan terjangkau," katanya.

Salah satu poin penting dalam UU ini adalah penyederhanaan proses perizinan bagi tenaga kesehatan, termasuk dokter spesialis, guna mengatasi kekurangan dokter di daerah terpencil. Selain itu, UU ini juga mengatur tentang pendanaan kesehatan yang lebih efisien dan transparan. Namun, pengesahan ini tidak lepas dari kontroversi. Beberapa organisasi profesi kesehatan masih menyatakan keberatan terhadap beberapa pasal, terutama terkait peran organisasi profesi dalam penerbitan rekomendasi izin praktik.

Di luar gedung DPR, sejumlah massa dari berbagai organisasi tenaga kesehatan menggelar aksi damai menolak pengesahan RUU ini. Mereka menilai beberapa pasal dalam UU baru tersebut berpotensi merugikan tenaga kesehatan dan menurunkan standar pelayanan medis. Menanggapi hal ini, DPR dan pemerintah menyatakan siap membuka ruang dialog untuk menyusun aturan turunan yang dapat mengakomodasi aspirasi para tenaga kesehatan demi kebaikan bersama.""",
                "category": "Politik",
                "tags": ["Nasional", "Breaking News"],
                "author": "Budi Hartono",
                "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/Gedung_DPR_MPR_RI.jpg/800px-Gedung_DPR_MPR_RI.jpg"
            },
            {
                "title": "Pertemuan Bilateral Indonesia-Jepang Bahas Kerjasama Ekonomi",
                "content": """Presiden Republik Indonesia mengadakan pertemuan bilateral tingkat tinggi dengan Perdana Menteri Jepang di Tokyo, Jepang, di sela-sela KTT ASEAN-Jepang. Pertemuan yang berlangsung hangat ini membahas berbagai isu strategis, dengan fokus utama pada penguatan kerjasama ekonomi antara kedua negara. Jepang, sebagai salah satu mitra dagang dan investor terbesar bagi Indonesia, menegaskan kembali komitmennya untuk terus mendukung pembangunan ekonomi di Indonesia.

Dalam pertemuan tersebut, kedua pemimpin sepakat untuk meningkatkan nilai perdagangan bilateral dan mempercepat realisasi investasi Jepang di Indonesia, khususnya di sektor industri otomotif, elektronik, dan infrastruktur energi terbarukan. Presiden RI secara khusus mengundang investor Jepang untuk berpartisipasi dalam pembangunan Ibu Kota Nusantara (IKN) dengan konsep smart city dan green energy. "Kami menyambut baik minat investor Jepang di IKN. Kami butuh teknologi dan pengalaman Jepang dalam membangun kota modern yang ramah lingkungan," ujar Presiden.

Selain kerjasama ekonomi, isu keamanan dan stabilitas di kawasan Indo-Pasifik juga menjadi topik pembahasan yang serius. Kedua negara sepakat untuk memperkuat kerjasama maritim dan pertahanan guna menjaga perdamaian di kawasan di tengah dinamika geopolitik global yang kian kompleks. Jepang juga berkomitmen untuk memberikan bantuan teknis dan pelatihan bagi sumber daya manusia Indonesia di bidang teknologi tinggi.

Pertemuan diakhiri dengan penandatanganan sejumlah nota kesepahaman (MoU) antara pemerintah Indonesia dan Jepang, serta antara sektor swasta kedua negara. Kesepakatan ini mencakup proyek MRT Jakarta fase lanjutan, pengembangan pelabuhan Patimban, dan kerjasama transisi energi. Kunjungan ini diharapkan dapat semakin mempererat hubungan persahabatan yang telah terjalin selama 65 tahun antara Indonesia dan Jepang.""",
                "category": "Politik",
                "tags": ["Internasional", "Nasional"],
                "author": "Rina Wati",
                "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Flag_of_Japan.svg/800px-Flag_of_Japan.svg.png"
            },
            {
                "title": "Pilkada Serentak 2024: Persiapan Logistik Capai 80 Persen",
                "content": """Persiapan logistik untuk pelaksanaan Pemilihan Kepala Daerah (Pilkada) serentak tahun 2024 dilaporkan telah mencapai progres yang signifikan, yakni sebesar 80 persen secara nasional. Komisi Pemilihan Umum (KPU) di berbagai daerah terus bekerja keras mengebut proses pencetakan surat suara, formulir, dan pengadaan perlengkapan pemungutan suara lainnya seperti kotak suara, bilik suara, dan tinta. Hal ini dilakukan untuk memastikan seluruh logistik siap didistribusikan tepat waktu ke seluruh Tempat Pemungutan Suara (TPS).

Anggota KPU Divisi Logistik menjelaskan bahwa prioritas distribusi saat ini difokuskan pada daerah-daerah terluar, terdepan, dan tertinggal (3T) serta daerah kepulauan yang memiliki akses transportasi sulit. "Kami tidak ingin ada TPS yang kekurangan logistik pada hari H. Oleh karena itu, pengiriman ke daerah sulit sudah kami mulai lebih awal dengan menggunakan moda transportasi laut dan udara, bahkan bekerjasama dengan TNI/Polri," ungkapnya dalam rapat koordinasi nasional.

Kendala cuaca ekstrem yang melanda beberapa wilayah Indonesia belakangan ini menjadi tantangan tersendiri dalam proses distribusi. Di beberapa daerah di Sumatera dan Kalimantan, banjir sempat menghambat akses jalan menuju gudang logistik kecamatan. KPU daerah telah menyiapkan langkah antisipasi dengan membungkus logistik menggunakan plastik berlapis dan menempatkan gudang penyimpanan di lokasi yang bebas banjir dan aman dari gangguan keamanan.

Selain logistik fisik, KPU juga mematangkan persiapan sistem informasi rekapitulasi suara (Sirekap) yang akan digunakan untuk membantu transparansi penghitungan suara. Bimbingan teknis kepada petugas Kelompok Penyelenggara Pemungutan Suara (KPPS) juga mulai digencarkan agar mereka memahami prosedur pemungutan dan penghitungan suara dengan baik. Masyarakat dihimbau untuk aktif mengecek status daftar pemilih tetap (DPT) dan memastikan diri terdaftar agar dapat menggunakan hak pilihnya pada Pilkada mendatang.""",
                "category": "Politik",
                "tags": ["Daerah", "Nasional"],
                "author": "Dedi Mulyadi",
                "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/ce/Kotak_Suara_Pemilu.jpg/600px-Kotak_Suara_Pemilu.jpg"
            },

            # EKONOMI (5)
            {
                "title": "IHSG Menguat di Penutupan Perdagangan Akhir Pekan",
                "content": """Indeks Harga Saham Gabungan (IHSG) Bursa Efek Indonesia (BEI) ditutup menguat signifikan sebesar 0,5% ke level 7.200 pada perdagangan akhir pekan ini. Kenaikan ini didorong oleh aksi beli investor asing yang kembali masuk ke pasar saham domestik, serta sentimen positif dari bursa global yang menghijau. Sektor perbankan berkapitalisasi besar (big caps) dan sektor infrastruktur menjadi motor penggerak utama laju indeks hari ini.

Analis pasar modal dari sekuritas ternama menilai bahwa rilis data laporan keuangan emiten kuartal III yang mayoritas mencatatkan kinerja positif menjadi katalis kuat bagi kepercayaan investor. "Fundamental ekonomi Indonesia yang solid di tengah ketidakpastian global membuat aset-aset berisiko di Indonesia kembali menarik. Laba bersih emiten perbankan yang tumbuh double digit memberikan sinyal bahwa roda ekonomi berputar kencang," paparnya.

Selain faktor domestik, meredanya kekhawatiran terhadap kenaikan suku bunga The Fed di Amerika Serikat juga memberikan angin segar bagi pasar negara berkembang, termasuk Indonesia. Nilai tukar Rupiah juga terpantau stabil menguat terhadap Dolar AS, yang semakin menambah optimisme pelaku pasar. Transaksi harian tercatat cukup ramai dengan nilai turnover mencapai Rp 10 triliun.

Meskipun demikian, para analis tetap mengingatkan investor untuk tetap waspada terhadap volatilitas pasar pekan depan. Rilis data inflasi AS dan data neraca perdagangan Indonesia akan menjadi perhatian utama pasar. Investor disarankan untuk tetap selektif dalam memilih saham (stock picking) dengan fokus pada perusahaan yang memiliki fundamental kuat dan valuasi yang masih wajar. Prospek IHSG hingga akhir tahun diperkirakan masih berpotensi untuk mencetak rekor tertinggi baru (all time high).""",
                "category": "Ekonomi",
                "tags": ["Trending", "Nasional"],
                "author": "Kevin Sanjaya",
                "image": "https://images.unsplash.com/photo-1611974765270-ca1258634369?w=800"
            },
            {
                "title": "Bank Indonesia Tahan Suku Bunga Acuan",
                "content": """Rapat Dewan Gubernur (RDG) Bank Indonesia (BI) pada bulan ini memutuskan untuk kembali mempertahankan BI 7-Day Reverse Repo Rate (BI7DRR) di level 6,00%. Keputusan ini diambil sebagai langkah pre-emptive dan forward looking untuk memastikan inflasi tetap terkendali dalam sasaran 2,5±1% pada tahun ini dan tahun depan. Selain itu, kebijakan ini juga ditujukan untuk menjaga stabilitas nilai tukar Rupiah di tengah ketidakpastian pasar keuangan global yang masih tinggi.

Gubernur Bank Indonesia, dalam konferensi pers usai RDG, menjelaskan bahwa kondisi ekonomi domestik saat ini cukup resilien. Pertumbuhan ekonomi triwulan III tercatat solid, didukung oleh konsumsi rumah tangga yang kuat dan investasi yang meningkat. "Kami melihat bahwa stance kebijakan moneter saat ini masih konsisten dengan upaya menjaga stabilitas dan mendukung pertumbuhan ekonomi yang berkelanjutan," ujar Gubernur BI.

BI juga terus memperkuat bauran kebijakan moneter, makroprudensial, dan sistem pembayaran untuk menjaga stabilitas makroekonomi dan sistem keuangan. Kebijakan makroprudensial longgar terus dilanjutkan untuk mendorong kredit perbankan kepada dunia usaha. Di sisi lain, BI terus melakukan intervensi di pasar valas untuk memastikan ketersediaan likuiditas dan menjaga volatilitas nilai tukar agar sejalan dengan fundamentalnya.

Para ekonom menyambut baik keputusan BI ini. Mereka menilai bahwa menahan suku bunga adalah langkah yang tepat di tengah tren inflasi yang mulai melandai. Kenaikan suku bunga yang terlalu agresif dikhawatirkan justru dapat menekan pertumbuhan ekonomi riil. Dengan dipertahankannya suku bunga acuan, diharapkan perbankan tidak buru-buru menaikkan suku bunga kredit, sehingga momentum pemulihan ekonomi dapat terus terjaga.""",
                "category": "Ekonomi",
                "tags": ["Nasional", "Breaking News"],
                "author": "Sri Mulyani",
                "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2e/Bank_Indonesia_Jakarta.jpg/800px-Bank_Indonesia_Jakarta.jpg"
            },
            {
                "title": "Ekspor Non-Migas Indonesia Catat Surplus 40 Bulan Berturut-turut",
                "content": """Badan Pusat Statistik (BPS) kembali merilis data neraca perdagangan Indonesia yang menunjukkan kinerja impresif. Neraca perdagangan Indonesia pada bulan lalu tercatat kembali surplus, melanjutkan tren surplus yang telah terjadi selama 40 bulan berturut-turut sejak Mei 2020. Surplus ini terutama ditopang oleh kinerja ekspor non-migas yang masih kuat, meskipun harga komoditas global mengalami moderasi.

Komoditas unggulan Indonesia seperti batubara, minyak kelapa sawit (CPO), serta besi dan baja (produk turunan nikel) masih menjadi penyumbang terbesar devisa ekspor. Menteri Perdagangan mengapresiasi capaian ini dan menyebutnya sebagai bukti ketahanan ekonomi Indonesia. "Di tengah perlambatan ekonomi global dan menurunnya permintaan dari beberapa negara mitra dagang utama, produk kita masih kompetitif dan diminati pasar dunia," katanya.

Pemerintah terus berupaya melakukan diversifikasi pasar ekspor ke negara-negara non-tradisional seperti di kawasan Afrika, Timur Tengah, dan Amerika Latin. Misi dagang dan pameran internasional gencar dilakukan untuk membuka peluang pasar baru bagi produk-produk Indonesia, termasuk produk manufaktur dan UMKM. Hilirisasi industri yang digalakkan pemerintah juga dinilai mulai membuahkan hasil dengan meningkatnya nilai tambah produk ekspor.

Namun, BPS juga mengingatkan agar pemerintah tetap waspada terhadap potensi penurunan permintaan global akibat resesi di beberapa negara maju. Kinerja impor juga perlu diperhatikan, terutama impor bahan baku dan barang modal, yang menjadi indikator aktivitas industri dalam negeri. Pemerintah berkomitmen untuk terus menjaga iklim usaha yang kondusif dan memberikan insentif bagi eksportir agar kinerja positif ini dapat terus berlanjut.""",
                "category": "Ekonomi",
                "tags": ["Nasional", "Trending"],
                "author": "Bambang Brodjonegoro",
                "image": "https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?w=800"
            },
            {
                "title": "Harga Emas Antam Hari Ini Turun Tipis",
                "content": """Harga emas batangan bersertifikat Antam keluaran PT Aneka Tambang Tbk (ANTM) terpantau mengalami penurunan tipis pada perdagangan hari ini. Harga pecahan satu gram emas Antam berada di level Rp 1.120.000, turun Rp 2.000 dibandingkan harga perdagangan kemarin. Penurunan ini sejalan dengan pergerakan harga emas dunia di pasar spot yang terkoreksi akibat penguatan indeks Dolar AS dan kenaikan yield obligasi pemerintah AS.

Meskipun mengalami penurunan jangka pendek, minat masyarakat Indonesia untuk berinvestasi emas fisik masih tergolong tinggi. Emas dianggap sebagai aset lindung nilai (safe haven) yang paling aman di tengah ketidakpastian ekonomi dan inflasi. Banyak investor ritel, terutama kaum ibu dan milenial, yang justru memanfaatkan momen koreksi harga (buy on weakness) ini untuk menambah portofolio investasi emas mereka.

Analis komoditas memprediksi bahwa harga emas masih memiliki potensi untuk naik (bullish) hingga akhir tahun, didorong oleh ekspektasi bahwa bank sentral AS (The Fed) akan segera mengakhiri siklus kenaikan suku bunganya. Selain itu, permintaan emas fisik dari negara-negara konsumen utama seperti India dan China menjelang musim festival juga dapat menopang harga.

PT Antam Tbk sendiri terus berinovasi untuk memudahkan masyarakat membeli emas, salah satunya melalui layanan pembelian emas secara online dan brankas emas. Masyarakat dihimbau untuk membeli emas di tempat-tempat resmi dan terpercaya untuk menghindari penipuan emas palsu. Emas batangan Antam juga kini hadir dengan kemasan baru yang dilengkapi teknologi CertiEye untuk menjamin keaslian produk.""",
                "category": "Ekonomi",
                "tags": ["Nasional"],
                "author": "Dewi Persik",
                "image": "https://images.unsplash.com/photo-1610375461246-83df859d849d?w=800"
            },
            {
                "title": "Startup Unicorn Indonesia Siap IPO Tahun Depan",
                "content": """Kabar gembira datang dari ekosistem startup teknologi Indonesia. Salah satu startup berstatus unicorn yang bergerak di bidang logistik dan supply chain dikabarkan tengah mematangkan persiapan untuk melantai di Bursa Efek Indonesia (BEI) melalui mekanisme Initial Public Offering (IPO) pada awal tahun depan. Perusahaan tersebut dilaporkan telah menunjuk konsorsium underwriter (penjamin emisi efek) untuk membantu proses go public ini.

Langkah IPO ini dinilai sebagai strategi penting bagi perusahaan untuk menggalang dana segar guna membiayai ekspansi bisnis yang agresif, termasuk pengembangan teknologi AI dan perluasan jaringan gudang pintar di seluruh Indonesia. Selain itu, menjadi perusahaan terbuka juga diharapkan dapat meningkatkan tata kelola perusahaan (good corporate governance) dan transparansi, sehingga semakin meningkatkan kepercayaan mitra bisnis dan pelanggan.

Para pelaku pasar modal menyambut antusias rencana IPO ini. Masuknya perusahaan teknologi bervaluasi besar ke bursa saham diharapkan dapat menambah kedalaman pasar dan memberikan pilihan investasi yang lebih beragam bagi investor, khususnya investor ritel yang tertarik pada saham sektor teknologi (new economy). "Ini akan menjadi IPO jumbo yang ditunggu-tunggu. Kami berharap valuasinya wajar dan prospek bisnisnya menjanjikan profitabilitas," ujar seorang manajer investasi.

Otoritas Jasa Keuangan (OJK) dan BEI sendiri terus mendorong lebih banyak startup unicorn dan centaur untuk mencatatkan sahamnya di dalam negeri melalui papan ekonomi baru. Jika IPO ini sukses, diharapkan akan memicu gelombang IPO startup lainnya di tahun-tahun mendatang, menjadikan bursa saham Indonesia sebagai hub bagi perusahaan teknologi di kawasan Asia Tenggara.""",
                "category": "Ekonomi",
                "tags": ["Trending", "Nasional"],
                "author": "Nadiem Makarim",
                "image": "https://images.unsplash.com/photo-1559526324-4b87b5e36e44?w=800"
            },

            # TEKNOLOGI (5)
            {
                "title": "Apple Resmi Luncurkan iPhone 16 dengan Fitur AI Canggih",
                "content": """Raksasa teknologi Apple akhirnya resmi memperkenalkan jajaran smartphone terbarunya, iPhone 16 series, dalam acara Apple Event yang digelar di Cupertino, California. Peluncuran ini menjadi salah satu yang paling dinanti tahun ini, terutama karena Apple menyematkan fitur kecerdasan buatan (Artificial Intelligence/AI) yang sangat canggih dan terintegrasi mendalam pada sistem operasi iOS 18 terbaru mereka. Fitur yang diberi nama "Apple Intelligence" ini diklaim akan mengubah cara pengguna berinteraksi dengan iPhone mereka.

Salah satu kemampuan AI yang paling menonjol adalah peningkatan drastis pada asisten virtual Siri. Siri kini mampu memahami konteks percakapan yang lebih kompleks, merangkum notifikasi, menulis email, hingga mengedit foto secara otomatis sesuai perintah suara pengguna. Selain itu, iPhone 16 juga dilengkapi dengan chipset A18 Bionic terbaru yang dirancang khusus untuk memproses tugas-tugas machine learning dengan sangat cepat dan efisien, tanpa menguras baterai secara berlebihan.

Dari sisi hardware, iPhone 16 Pro dan Pro Max hadir dengan desain bodi menggunakan material titanium grade 5 yang lebih ringan namun lebih kuat dari baja tahan karat. Sektor kamera juga mendapat upgrade signifikan dengan sensor utama 48MP yang lebih besar dan kemampuan zoom optik periskop hingga 10x. Tombol "Action Button" yang sebelumnya hanya ada di seri Pro kini tersedia di seluruh model iPhone 16, memberikan akses cepat ke berbagai fungsi favorit.

Pre-order untuk iPhone 16 di pasar global akan dimulai minggu depan, sementara ketersediaan di Indonesia diperkirakan akan menyusul satu bulan kemudian. Para pengamat teknologi memprediksi iPhone 16 akan memicu "super cycle" upgrade di kalangan pengguna iPhone lama yang ingin merasakan pengalaman AI generatif di perangkat mobile. Harga yang ditawarkan pun relatif kompetitif dibandingkan flagship kompetitor, membuat persaingan di pasar smartphone premium semakin memanas.""",
                "category": "Teknologi",
                "tags": ["Internasional", "Trending", "Viral"],
                "author": "Gadget In",
                "image": "https://images.unsplash.com/photo-1510557880182-3d4d3cba35a5?w=800"
            },
            {
                "title": "Kominfo Blokir Ribuan Situs Judi Online",
                "content": """Kementerian Komunikasi dan Informatika (Kominfo) Republik Indonesia kembali menunjukkan ketegasannya dalam memberantas konten negatif di internet. Dalam operasi siber terbaru yang dilakukan minggu ini, Kominfo berhasil memblokir dan memutus akses terhadap ribuan situs serta aplikasi judi online yang meresahkan masyarakat. Langkah tegas ini diambil menyusul banyaknya laporan dari masyarakat tentang maraknya promosi judi online yang menyasar berbagai kalangan, termasuk remaja dan anak-anak.

Menteri Komunikasi dan Informatika (Menkominfo) dalam konferensi persnya menegaskan bahwa pemerintah tidak akan memberi ruang sedikitpun bagi praktik perjudian online di Indonesia. "Judi online adalah penyakit masyarakat yang merusak ekonomi keluarga dan mental generasi muda. Kami menggunakan teknologi AI dan crawling system terbaru untuk mendeteksi situs-situs ilegal ini secara otomatis 24 jam non-stop," tegas Menkominfo. Ia juga memperingatkan para influencer dan selebgram untuk tidak mempromosikan situs judi online jika tidak ingin berhadapan dengan hukum.

Selain pemblokiran situs, Kominfo juga bekerjasama dengan Otoritas Jasa Keuangan (OJK) dan Bank Indonesia untuk memblokir ribuan rekening bank dan akun dompet digital (e-wallet) yang terindikasi digunakan untuk transaksi judi online. Langkah "follow the money" ini diharapkan dapat mematikan nafas bisnis para bandar judi dengan memutus aliran dana mereka. Polisi juga terus melakukan penyelidikan untuk menangkap operator dan bandar di balik situs-situs tersebut.

Masyarakat diminta untuk terus aktif berpartisipasi dengan melaporkan jika menemukan situs atau aplikasi judi online melalui kanal aduan konten Kominfo. Pemerintah juga menggencarkan literasi digital ke sekolah-sekolah dan komunitas untuk memberikan edukasi tentang bahaya judi online dan pentingnya menjaga keamanan data pribadi di dunia maya. Perang melawan judi online ini membutuhkan kerjasama semua pihak agar ruang digital Indonesia menjadi lebih aman dan produktif.""",
                "category": "Teknologi",
                "tags": ["Nasional", "Breaking News"],
                "author": "Budi Arie",
                "image": "https://images.unsplash.com/photo-1563986768609-322da13575f3?w=800"
            },
            {
                "title": "Perkembangan Jaringan 5G di Indonesia Makin Meluas",
                "content": """Adopsi teknologi jaringan seluler generasi kelima atau 5G di Indonesia menunjukkan perkembangan yang semakin positif. Operator seluler utama di tanah air terus berlomba-lomba memperluas cakupan layanan 5G mereka ke berbagai kota besar di luar Pulau Jawa. Setelah sukses digelar di Jabodetabek, kini sinyal 5G komersial mulai dapat dinikmati oleh masyarakat di kota-kota seperti Surabaya, Bandung, Medan, Makassar, hingga Denpasar dan Balikpapan.

Teknologi 5G menawarkan keunggulan kecepatan internet yang jauh lebih tinggi, latensi (jeda) yang sangat rendah, dan kapasitas koneksi yang lebih besar dibandingkan 4G. Hal ini membuka peluang besar bagi pengembangan use cases masa depan seperti mobil otonom, bedah jarak jauh, pabrik pintar (smart factory), dan pengalaman metaverse yang immersive. Bagi pengguna umum, 5G memberikan pengalaman streaming video 4K tanpa buffering dan cloud gaming yang responsif.

Kementerian Kominfo terus mendukung percepatan pemerataan 5G dengan melakukan penataan ulang (refarming) spektrum frekuensi radio agar alokasi bandwidth untuk 5G semakin optimal. Pemerintah juga mendorong operator untuk membangun infrastruktur fiber optic (fiberisasi) ke seluruh BTS guna menopang trafik data 5G yang besar. Target pemerintah adalah seluruh ibu kota provinsi dan kawasan industri strategis sudah tercover jaringan 5G pada tahun 2025.

Di sisi perangkat, penetrasi smartphone yang mendukung 5G juga terus meningkat seiring dengan banyaknya produsen yang merilis ponsel 5G dengan harga terjangkau di kisaran 2-3 juta rupiah. Hal ini membuat ekosistem 5G di Indonesia semakin matang. Meski demikian, tantangan berupa kondisi geografis kepulauan dan biaya investasi infrastruktur yang mahal masih menjadi pekerjaan rumah yang harus diselesaikan bersama oleh pemerintah dan pelaku industri telekomunikasi.""",
                "category": "Teknologi",
                "tags": ["Nasional", "Teknologi"],
                "author": "Onno W. Purbo",
                "image": "https://images.unsplash.com/photo-1614064641938-3bbee52942c7?w=800"
            },
            {
                "title": "Google Perkenalkan Model AI Terbaru 'Gemini 2.0'",
                "content": """Google kembali membuat gebrakan besar di dunia kecerdasan buatan dengan resmi memperkenalkan model AI generatif terbarunya, Gemini 2.0. Model ini diklaim sebagai lompatan kuantum dari pendahulunya, dengan kemampuan penalaran, pemahaman konteks, dan kreativitas yang jauh lebih superior. CEO Google, Sundar Pichai, menyebut Gemini 2.0 sebagai model AI paling kapabel dan umum yang pernah dibuat oleh Google hingga saat ini.

Keunggulan utama Gemini 2.0 terletak pada kemampuan multimodalnya yang native. Artinya, model ini dilatih sejak awal untuk memahami dan memproses berbagai jenis input secara bersamaan, mulai dari teks, kode pemrograman, gambar, audio, hingga video. Pengguna bisa memberikan input berupa video real-time dan meminta Gemini 2.0 untuk menganalisis apa yang terjadi di dalamnya, atau memintanya membuat kode aplikasi lengkap hanya dari sketsa gambar di kertas.

Google berencana mengintegrasikan Gemini 2.0 ke dalam seluruh ekosistem produknya, mulai dari Google Search, Gmail, Docs, hingga Android. Hal ini akan menghadirkan pengalaman pengguna yang lebih cerdas dan personal. Misalnya, di Google Docs, Gemini 2.0 bisa membantu menulis draft artikel, merangkum dokumen panjang, atau membuat visualisasi data secara instan. Di Android, asisten Google akan menjadi jauh lebih pintar dalam membantu aktivitas sehari-hari.

Peluncuran Gemini 2.0 ini semakin memanaskan persaingan di ranah AI generatif, menantang dominasi model GPT dari OpenAI. Para ahli teknologi menilai persaingan ini sangat positif karena akan mendorong inovasi yang lebih cepat. Namun, Google juga menekankan komitmennya terhadap pengembangan AI yang bertanggung jawab (Responsible AI) dengan menyertakan fitur keamanan untuk mencegah penyalahgunaan model untuk menyebarkan disinformasi atau konten berbahaya.""",
                "category": "Teknologi",
                "tags": ["Internasional", "Trending"],
                "author": "Sundar Pichai",
                "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Google_2015_logo.svg/800px-Google_2015_logo.svg.png"
            },
            {
                "title": "Ancaman Cyber Attack Meningkat, Perusahaan Diminta Waspada",
                "content": """Badan Siber dan Sandi Negara (BSSN) merilis laporan tahunan yang menunjukkan adanya peningkatan drastis jumlah serangan siber (cyber attack) yang menargetkan institusi pemerintah dan perusahaan swasta di Indonesia dalam satu tahun terakhir. Serangan siber tidak hanya semakin sering terjadi, tetapi juga semakin canggih dan kompleks tekniknya. Ransomware, phishing, dan peretasan data (data breach) masih menjadi jenis ancaman yang paling mendominasi dan merugikan.

Kepala BSSN mengungkapkan bahwa sektor keuangan, kesehatan, dan energi menjadi target favorit para peretas karena memiliki data bernilai tinggi. "Para penjahat siber kini beroperasi seperti sindikat terorganisir. Mereka mencari celah keamanan sekecil apapun untuk masuk dan menyandera data perusahaan demi meminta tebusan," jelasnya. Kerugian finansial dan reputasi akibat serangan siber diperkirakan mencapai triliunan rupiah per tahun.

Menyikapi tren yang mengkhawatirkan ini, BSSN menghimbau seluruh organisasi untuk segera memperkuat sistem pertahanan keamanan digital mereka. Hal ini meliputi pembaruan software secara rutin, penggunaan firewall dan antivirus mutakhir, serta penerapan autentikasi dua faktor (2FA). Namun, yang tak kalah penting adalah meningkatkan kesadaran keamanan siber (cyber security awareness) bagi seluruh karyawan, karena faktor kelalaian manusia (human error) seringkali menjadi pintu masuk utama serangan.

BSSN juga mendorong perusahaan untuk rutin melakukan simulasi serangan siber dan audit keamanan, serta memiliki prosedur pemulihan bencana (disaster recovery plan) yang handal, termasuk backup data secara berkala dan terpisah (offline). Pemerintah saat ini juga tengah mempercepat pengesahan RUU Keamanan dan Ketahanan Siber untuk memberikan payung hukum yang lebih kuat dalam penanganan kejahatan siber di Indonesia.""",
                "category": "Teknologi",
                "tags": ["Nasional", "Investigasi"],
                "author": "Hinsa Siburian",
                "image": "https://images.unsplash.com/photo-1563206767-5b1d97299337?w=800"
            },

            # OLAHRAGA (5)
            {
                "title": "Timnas Indonesia Menang Telak Lawan Vietnam",
                "content": """Tim Nasional (Timnas) sepak bola Indonesia berhasil meraih kemenangan gemilang saat menjamu rival bebuyutannya, Vietnam, dalam laga lanjutan Kualifikasi Piala Dunia 2026 Zona Asia. Bertanding di hadapan puluhan ribu pendukung setia di Stadion Utama Gelora Bung Karno (SUGBK), Jakarta, skuad Garuda tampil trengginas dan melibas tim tamu dengan skor telak 3-0. Kemenangan ini sekaligus memutus rekor buruk Indonesia yang sulit menang saat bertemu Vietnam dalam beberapa tahun terakhir.

Gol-gol kemenangan Indonesia dicetak oleh para pemain debutan naturalisasi yang baru saja bergabung dengan tim. Jay Idzes membuka keunggulan lewat sundulan mematikan memanfaatkan sepak pojok di babak pertama. Di babak kedua, Ragnar Oratmangoen menggandakan keunggulan lewat aksi solo run yang memukau, sebelum Ramadhan Sananta menutup pesta gol di masa injury time. Permainan kolektif dan disiplin tinggi yang ditunjukkan anak asuh Shin Tae-yong menuai pujian dari berbagai pihak.

Pelatih Shin Tae-yong mengaku sangat puas dengan performa para pemainnya yang mampu menjalankan taktik dengan sempurna. "Para pemain bekerja sangat keras dan menunjukkan mentalitas pemenang. Dukungan suporter yang luar biasa juga memberikan energi tambahan bagi kami," ujar pelatih asal Korea Selatan tersebut. Kemenangan ini sangat krusial karena membuka peluang lebar bagi Indonesia untuk lolos ke putaran ketiga kualifikasi Piala Dunia.

Euforia kemenangan terasa hingga ke luar stadion. Ribuan suporter berpesta merayakan hasil positif ini, menyanyikan lagu-lagu kebangsaan dan yel-yel dukungan. Presiden RI yang turut menyaksikan pertandingan memberikan apresiasi tinggi dan berharap tren positif ini dapat terus dipertahankan di laga-laga selanjutnya. Timnas Indonesia kini menatap laga tandang ke markas Vietnam dengan kepercayaan diri tinggi.""",
                "category": "Olahraga",
                "tags": ["Nasional", "Viral", "Trending"],
                "author": "Bung Towel",
                "image": "https://images.unsplash.com/photo-1579952363873-27f3bade9f55?w=800"
            },
            {
                "title": "MotoGP Mandalika 2024 Siap Digelar",
                "content": """Sirkuit Internasional Pertamina Mandalika di Lombok Tengah, Nusa Tenggara Barat (NTB), kembali bersiap menjadi tuan rumah ajang balap motor paling bergengsi di dunia, MotoGP, pada akhir pekan ini. Seluruh persiapan, mulai dari infrastruktur lintasan, fasilitas pendukung, hingga logistik tim balap, dilaporkan telah rampung 100 persen. Panitia penyelenggara memastikan bahwa gelaran tahun ini akan lebih meriah dan tertata dibandingkan tahun-tahun sebelumnya.

Para pembalap top dunia seperti juara bertahan Francesco Bagnaia, Jorge Martin, dan Marc Marquez sudah tiba di Lombok sejak beberapa hari lalu. Mereka tampak menikmati keindahan alam dan keramahan masyarakat setempat sebelum mulai memacu motor mereka di lintasan. Beberapa pembalap bahkan membagikan momen keseruan mereka berlibur di pantai-pantai Lombok melalui akun media sosial, yang turut menjadi promosi gratis bagi pariwisata Indonesia.

Antusiasme penonton juga sangat tinggi. Tiket untuk kategori tribun utama dan VIP dilaporkan sudah terjual habis (sold out). Penonton tidak hanya datang dari Indonesia, tetapi juga dari mancanegara. Pihak penyelenggara telah menyiapkan berbagai acara hiburan sampingan (side events) seperti konser musik dan festival kuliner untuk memanjakan para pengunjung yang datang ke sirkuit.

Dampak ekonomi dari gelaran MotoGP Mandalika ini sangat dirasakan oleh masyarakat lokal. Tingkat hunian hotel dan homestay di sekitar sirkuit penuh, penyewaan kendaraan meningkat pesat, dan produk-produk UMKM laris manis diburu wisatawan. Pemerintah berharap MotoGP Mandalika dapat terus menjadi event olahraga unggulan yang mempromosikan "Sport Tourism" Indonesia di mata dunia.""",
                "category": "Olahraga",
                "tags": ["Nasional", "Internasional"],
                "author": "Matteo Guerinoni",
                "image": "https://images.unsplash.com/photo-1568782517-552568660d59?w=800"
            },
            {
                "title": "Lakers Juara NBA In-Season Tournament",
                "content": """Los Angeles Lakers mencatatkan sejarah baru dengan keluar sebagai juara edisi perdana NBA In-Season Tournament. Di partai final yang digelar di Las Vegas, Lakers berhasil menundukkan perlawanan sengit Indiana Pacers dengan skor 123-109. Bintang gaek LeBron James tampil sebagai inspirator kemenangan timnya dan dinobatkan sebagai Most Valuable Player (MVP) turnamen tersebut, menambah panjang daftar prestasi dalam karir legendarisnya.

Pertandingan final berlangsung ketat sejak kuarter pertama. Pacers yang dimotori oleh Tyrese Haliburton memberikan perlawanan sengit dengan permainan cepat mereka. Namun, pengalaman dan dominasi fisik Lakers, terutama Anthony Davis yang mencetak 41 poin dan 20 rebound, menjadi pembeda di lapangan. Pertahanan kokoh Lakers di kuarter keempat sukses mematikan serangan Pacers dan mengunci kemenangan.

Kemenangan ini disambut sukacita oleh para pemain dan fans Lakers. Setiap pemain Lakers berhak mendapatkan hadiah uang tunai sebesar USD 500.000. "Kami ingin menjadi yang pertama memenangkan ini. Ini adalah sejarah, dan kami bangga bisa membawanya pulang ke Los Angeles," ujar LeBron James usai mengangkat trofi NBA Cup yang baru.

Format turnamen baru In-Season Tournament yang diperkenalkan NBA musim ini dinilai sukses besar. Turnamen ini berhasil meningkatkan intensitas pertandingan dan antusiasme penonton di awal musim reguler yang biasanya berjalan datar. Rating televisi dan keterlibatan fans di media sosial meningkat tajam selama turnamen berlangsung. Kesuksesan ini kemungkinan besar akan membuat NBA menjadikan turnamen ini sebagai agenda rutin tahunan.""",
                "category": "Olahraga",
                "tags": ["Internasional"],
                "author": "Michael Jordan",
                "image": "https://images.unsplash.com/photo-1504450758481-7338eba7524a?w=800"
            },
            {
                "title": "Gregoria Mariska Tunjung Juara Japan Masters",
                "content": """Pebulutangkis tunggal putri andalan Indonesia, Gregoria Mariska Tunjung, berhasil menorehkan prestasi membanggakan dengan menjuarai turnamen Kumamoto Japan Masters 2023. Di babak final, Gregoria tampil luar biasa dan mengalahkan peraih medali emas Olimpiade Tokyo asal China, Chen Yu Fei, dua gim langsung dengan skor 21-12, 21-12. Kemenangan ini menjadi gelar juara level BWF World Tour Super 500 pertama bagi Gregoria sepanjang karirnya.

Penampilan Gregoria di final menuai banyak pujian. Ia bermain sangat taktis, sabar, dan minim melakukan kesalahan sendiri. Pukulan-pukulan variatif dan penempatan bola yang akurat membuat Chen Yu Fei, yang dikenal memiliki pertahanan kokoh, tak berkutik dan frustrasi. Kemenangan ini sekaligus memutus dominasi pemain-pemain top dunia atas tunggal putri Indonesia dalam beberapa tahun terakhir.

"Saya sangat bersyukur dan tidak menyangka bisa juara di sini. Kuncinya adalah bermain tenang dan menikmati setiap poin. Terima kasih untuk pelatih, PBSI, dan seluruh masyarakat Indonesia yang mendoakan," ucap Gregoria dengan wajah berseri-seri di podium juara. Gelar ini mendongkrak kepercayaan diri Gregoria dan posisinya di peringkat dunia BWF.

Prestasi ini menjadi modal yang sangat berharga bagi Gregoria dalam persiapan menuju Olimpiade Paris 2024. Konsistensi permainan yang ditunjukkan Gregoria sepanjang tahun ini memberikan harapan baru bagi bulutangkis Indonesia untuk kembali meraih medali di sektor tunggal putri pada ajang olahraga terakbar di dunia tersebut. PBSI berkomitmen untuk terus memberikan dukungan penuh agar performa Gregoria terus meningkat.""",
                "category": "Olahraga",
                "tags": ["Nasional", "Trending"],
                "author": "Taufik Hidayat",
                "image": "https://images.unsplash.com/photo-1626224583764-f87db24ac4ea?w=800"
            },
            {
                "title": "PSSI Tunjuk Pelatih Baru untuk Timnas Wanita",
                "content": """Persatuan Sepak Bola Seluruh Indonesia (PSSI) membuat langkah progresif dengan resmi menunjuk pelatih asal Jepang, Satoru Mochizuki, untuk menangani Tim Nasional (Timnas) Wanita Indonesia. Penandatanganan kontrak dilakukan langsung oleh Ketua Umum PSSI, Erick Thohir, di Jakarta. Penunjukan Satoru merupakan bukti keseriusan PSSI untuk membangkitkan prestasi sepak bola putri tanah air yang selama ini tertinggal.

Satoru Mochizuki bukanlah nama sembarangan di dunia sepak bola wanita. Ia memiliki rekam jejak mentereng, termasuk menjadi bagian dari staf pelatih yang membawa Timnas Wanita Jepang (Nadeshiko Japan) menjuarai Piala Dunia Wanita 2011 dan meraih medali perak Olimpiade London 2012. Pengalaman dan filosofi sepak bola Jepang yang disiplin dan teknis diharapkan dapat ditularkan kepada para pemain putri Indonesia.

"Kami memilih coach Satoru karena track record-nya yang luar biasa dalam membangun tim juara. Kami ingin beliau membangun fondasi sepak bola putri kita dari bawah, mulai dari pembinaan usia muda hingga tim senior," ujar Erick Thohir. Satoru dikontrak dengan durasi jangka panjang dan diberikan keleluasaan untuk menyusun program latihan serta scouting pemain ke seluruh penjuru Indonesia.

Tugas berat sudah menanti Satoru, di antaranya persiapan menghadapi Piala Asia Wanita U-17 yang akan digelar di Bali. Satoru mengaku antusias dengan tantangan ini dan melihat potensi besar pada pemain-pemain putri Indonesia. "Saya melihat semangat juang yang tinggi dari pemain Indonesia. Dengan latihan yang tepat dan sistem yang baik, saya yakin kita bisa bersaing di level Asia," kata Satoru. Kehadiran pelatih kelas dunia ini diharapkan menjadi titik balik kebangkitan Garuda Pertiwi.""",
                "category": "Olahraga",
                "tags": ["Nasional"],
                "author": "Ratu Tisha",
                "image": "https://images.unsplash.com/photo-1518605348400-437731db485a?w=800"
            },

            # KESEHATAN (4)
            {
                "title": "Kasus COVID-19 Varian Baru Meningkat, Masyarakat Diminta Waspada",
                "content": """Kementerian Kesehatan (Kemenkes) RI melaporkan adanya tren peningkatan kasus COVID-19 di beberapa kota besar di Indonesia dalam dua pekan terakhir. Peningkatan ini didominasi oleh sub-varian baru JN.1 yang diketahui memiliki kemampuan menular lebih cepat dibandingkan varian-varian sebelumnya. Meskipun mayoritas pasien hanya mengalami gejala ringan seperti batuk, pilek, dan demam, namun kewaspadaan tetap perlu ditingkatkan, terutama menjelang masa libur panjang.

Juru Bicara Kemenkes menghimbau masyarakat untuk kembali disiplin menerapkan protokol kesehatan dasar. "Kami menyarankan masyarakat untuk kembali memakai masker saat berada di tempat umum yang padat, transportasi publik, atau jika sedang merasa kurang sehat. Cuci tangan pakai sabun juga harus tetap menjadi kebiasaan," ujarnya. Selain itu, masyarakat yang belum melengkapi dosis vaksinasi, terutama booster, diminta untuk segera mendatangi fasilitas kesehatan terdekat.

Rumah sakit dan fasilitas pelayanan kesehatan di seluruh daerah telah disiagakan untuk mengantisipasi potensi lonjakan pasien. Ketersediaan oksigen, obat-obatan, dan ruang isolasi dipastikan aman. Namun, pemerintah menegaskan bahwa hingga saat ini belum ada rencana untuk memberlakukan kembali pembatasan sosial atau PPKM. Kebijakan yang diambil lebih bersifat himbauan dan edukasi kepada masyarakat untuk menjaga kesehatan diri dan lingkungan.

Para ahli epidemiologi memprediksi puncak kasus gelombang kali ini mungkin akan terjadi dalam beberapa minggu ke depan, namun dampaknya tidak akan separah saat varian Delta karena tingkat kekebalan masyarakat (herd immunity) sudah cukup tinggi. Meski demikian, perlindungan terhadap kelompok rentan seperti lansia dan orang dengan komorbid harus menjadi prioritas utama agar tidak terjadi peningkatan angka kematian.""",
                "category": "Kesehatan",
                "tags": ["Nasional", "Breaking News"],
                "author": "dr. Tirta",
                "image": "https://images.unsplash.com/photo-1584036561566-b93a945c3575?w=800"
            },
            {
                "title": "Manfaat Puasa Intermiten bagi Kesehatan Jantung",
                "content": """Tren diet puasa intermiten atau intermittent fasting semakin populer di kalangan masyarakat perkotaan sebagai cara untuk menurunkan berat badan dan menjaga kesehatan. Sebuah studi klinis terbaru yang dipublikasikan di jurnal medis internasional semakin memperkuat manfaat metode ini. Studi tersebut menemukan bahwa puasa intermiten tidak hanya efektif membakar lemak, tetapi juga memberikan dampak positif yang signifikan bagi kesehatan jantung dan pembuluh darah.

Penelitian menunjukkan bahwa orang yang rutin melakukan puasa intermiten dengan metode 16:8 (16 jam puasa, 8 jam jendela makan) mengalami penurunan tekanan darah sistolik dan diastolik yang konsisten. Selain itu, kadar kolesterol jahat (LDL) dan trigliserida dalam darah juga menurun, sementara sensitivitas insulin meningkat. Hal ini secara langsung menurunkan risiko terjadinya penyakit jantung koroner, stroke, dan diabetes tipe 2.

"Saat tubuh berpuasa, terjadi proses perbaikan sel dan penurunan peradangan sistemik. Jantung menjadi lebih efisien dalam memompa darah, dan metabolisme tubuh menjadi lebih fleksibel," jelas seorang dokter spesialis jantung. Namun, ia menekankan bahwa puasa intermiten harus dibarengi dengan asupan nutrisi yang seimbang saat jendela makan. Mengonsumsi makanan tinggi gula dan lemak jenuh saat berbuka puasa justru akan menghilangkan manfaat kesehatan tersebut.

Meskipun bermanfaat, puasa intermiten tidak disarankan untuk semua orang. Ibu hamil, menyusui, penderita maag akut, atau orang dengan gangguan makan sebaiknya berkonsultasi dengan dokter sebelum mencoba metode ini. Kunci keberhasilan diet ini adalah konsistensi dan mendengarkan sinyal tubuh. Dengan pola makan yang tepat dan gaya hidup aktif, puasa intermiten bisa menjadi strategi ampuh untuk mencapai umur panjang dan jantung yang sehat.""",
                "category": "Kesehatan",
                "tags": ["Opini", "Trending"],
                "author": "dr. Zaidul Akbar",
                "image": "https://images.unsplash.com/photo-1498837167922-ddd27525d352?w=800"
            },
            {
                "title": "Pemerintah Gratiskan Vaksin HPV untuk Anak Sekolah",
                "content": """Pemerintah Indonesia melalui Kementerian Kesehatan (Kemenkes) terus berkomitmen untuk meningkatkan derajat kesehatan masyarakat, khususnya kaum perempuan. Salah satu langkah konkret yang diambil adalah dengan memperluas cakupan imunisasi wajib nasional. Kini, vaksin Human Papillomavirus (HPV) yang berfungsi mencegah kanker serviks diberikan secara gratis kepada seluruh anak perempuan kelas 5 dan 6 Sekolah Dasar (SD) atau sederajat dalam program Bulan Imunisasi Anak Sekolah (BIAS).

Kanker serviks atau kanker leher rahim saat ini masih menjadi salah satu pembunuh utama wanita di Indonesia. Tingginya angka kasus dan kematian akibat penyakit ini sebagian besar disebabkan oleh deteksi yang terlambat. "Vaksinasi HPV adalah investasi kesehatan jangka panjang. Dengan memberikan perlindungan sejak dini sebelum anak aktif secara seksual, kita bisa mencegah ribuan kematian ibu di masa depan," ujar Menteri Kesehatan Budi Gunadi Sadikin.

Program vaksinasi gratis ini disambut baik oleh para orang tua dan pihak sekolah. Sebelumnya, vaksin HPV tergolong mahal jika diakses secara mandiri di klinik swasta, sehingga tidak terjangkau oleh banyak kalangan. Dengan masuknya vaksin HPV ke dalam program nasional, diharapkan kesenjangan akses kesehatan dapat dikurangi. Petugas puskesmas akan mendatangi sekolah-sekolah untuk melakukan penyuntikan secara terjadwal.

Kemenkes juga gencar melakukan sosialisasi dan edukasi kepada masyarakat untuk menepis hoaks atau informasi keliru terkait efek samping vaksin HPV. Vaksin ini dipastikan aman, halal, dan efektif. Orang tua dihimbau untuk tidak ragu memberikan izin anaknya divaksinasi demi masa depan mereka yang lebih sehat. Selain vaksinasi, upaya deteksi dini melalui tes IVA dan Pap Smear bagi wanita dewasa juga terus digalakkan.""",
                "category": "Kesehatan",
                "tags": ["Nasional"],
                "author": "Menkes Budi",
                "image": "https://images.unsplash.com/photo-1576765608535-5f04d1e3f289?w=800"
            },
            {
                "title": "Bahaya Polusi Udara Jakarta bagi Kesehatan Paru-paru",
                "content": """Kualitas udara di wilayah Jabodetabek, khususnya DKI Jakarta, yang memburuk dalam beberapa bulan terakhir menjadi sorotan publik dan perhatian serius dunia kesehatan. Tingkat polusi udara yang seringkali masuk dalam kategori "tidak sehat" dengan konsentrasi partikel halus PM2.5 yang tinggi, membawa ancaman nyata bagi kesehatan pernapasan warga. Rumah sakit mencatat adanya lonjakan kunjungan pasien dengan keluhan Infeksi Saluran Pernapasan Akut (ISPA), batuk kronis, hingga serangan asma.

Dokter spesialis paru dari Perhimpunan Dokter Paru Indonesia (PDPI) memperingatkan bahwa paparan jangka panjang terhadap polusi udara tidak hanya menyebabkan gangguan pernapasan akut, tetapi juga berisiko memicu penyakit serius seperti Penyakit Paru Obstruktif Kronis (PPOK), kanker paru, hingga gangguan perkembangan paru pada anak-anak. "Partikel PM2.5 sangat kecil sehingga bisa menembus masker biasa dan masuk hingga ke aliran darah, merusak organ tubuh lainnya," jelasnya.

Menghadapi situasi ini, warga disarankan untuk memantau kualitas udara melalui aplikasi sebelum beraktivitas di luar ruangan. Penggunaan masker medis atau respirator N95 sangat dianjurkan saat berada di luar, terutama bagi pengendara sepeda motor dan pejalan kaki. Di dalam ruangan, penggunaan air purifier dapat membantu membersihkan udara. Kelompok rentan seperti anak-anak, lansia, dan ibu hamil perlu mendapatkan perlindungan ekstra.

Pemerintah daerah dan pusat kini tengah berupaya keras menanggulangi masalah polusi ini melalui berbagai kebijakan, seperti uji emisi kendaraan, pembatasan operasional industri penghasil polusi, hingga penyemprotan jalan (water mist). Namun, solusi jangka panjang seperti perbaikan transportasi publik dan transisi ke energi bersih dinilai sebagai kunci utama untuk mengembalikan langit biru Jakarta dan menjamin hak warga atas udara bersih.""",
                "category": "Kesehatan",
                "tags": ["Daerah", "Investigasi"],
                "author": "dr. Erlina Burhan",
                "image": "https://images.unsplash.com/photo-1497436072909-60f360e1d4b0?w=800"
            },

            # HIBURAN (3)
            {
                "title": "Film 'Agak Laen' Tembus 7 Juta Penonton",
                "content": """Industri perfilman Indonesia kembali mencatatkan sejarah baru. Film komedi horor berjudul "Agak Laen" sukses besar memikat hati penonton tanah air. Dalam waktu kurang dari satu bulan penayangannya di bioskop, film yang diproduseri oleh Ernest Prakasa ini berhasil menembus angka fantastis, yakni lebih dari 7 juta penonton. Pencapaian ini menempatkan "Agak Laen" sebagai salah satu film Indonesia terlaris sepanjang masa, bersaing dengan film-film blockbuster lainnya seperti "KKN di Desa Penari".

Kesuksesan film ini tidak lepas dari chemistry yang kuat antara empat pemeran utamanya, yaitu Indra Jegel, Boris Bokir, Oki Rengga, dan Bene Dion. Keempatnya merupakan komika dan podcaster ternama yang memiliki basis penggemar loyal. Cerita yang diangkat pun sangat segar dan relate dengan kehidupan sehari-hari, memadukan unsur komedi yang mengocok perut dengan sentuhan horor yang pas, serta drama persahabatan yang menyentuh hati.

"Kami benar-benar tidak menyangka apresiasinya akan sebesar ini. Terima kasih kepada seluruh penonton Indonesia yang sudah mendukung film lokal. Ini bukti bahwa film komedi punya tempat spesial di hati masyarakat," ujar Ernest Prakasa. Sebagai bentuk nazar atas kesuksesan ini, para pemain dan produser berjanji akan melakukan tantangan unik, yaitu menjadi manusia silver di Bundaran HI, yang semakin membuat heboh media sosial.

Fenomena "Agak Laen" memberikan angin segar bagi industri kreatif pasca pandemi. Hal ini membuktikan bahwa kualitas cerita dan promosi yang kreatif mampu menarik minat masyarakat untuk kembali menonton di bioskop. Kesuksesan ini diharapkan dapat memotivasi sineas lain untuk terus berkarya menghasilkan film-film berkualitas yang dapat menjadi tuan rumah di negeri sendiri.""",
                "category": "Hiburan",
                "tags": ["Viral", "Trending"],
                "author": "Ernest Prakasa",
                "image": "https://images.unsplash.com/photo-1489599849927-2ee91cede3ba?w=800"
            },
            {
                "title": "Konser Taylor Swift di Singapura Sedot Wisatawan Indonesia",
                "content": """Konser penyanyi superstar dunia, Taylor Swift, yang bertajuk "The Eras Tour" di Singapura menjadi fenomena regional yang luar biasa. Digelar selama enam hari di National Stadium, konser ini menjadi satu-satunya pemberhentian Taylor Swift di kawasan Asia Tenggara. Tak pelak, hal ini memicu gelombang kedatangan fans (Swifties) dari negara-negara tetangga, dan Indonesia menjadi salah satu penyumbang penonton terbesar.

Ribuan Swifties dari berbagai kota di Indonesia rela merogoh kocek dalam-dalam untuk terbang ke Singapura demi menyaksikan idola mereka secara langsung. Tiket pesawat Jakarta-Singapura dan harga hotel di Singapura melonjak drastis selama periode konser. Meskipun demikian, antusiasme fans tidak surut. Mereka tampil totalitas dengan kostum-kostum unik yang terinspirasi dari era album Taylor Swift dan bertukar gelang persahabatan (friendship bracelets) di venue konser.

Fenomena "Swiftonomics" ini memberikan dampak ekonomi yang nyata bagi Singapura. Namun, di sisi lain, hal ini juga menjadi refleksi bagi industri pariwisata dan hiburan Indonesia. Menteri Pariwisata dan Ekonomi Kreatif RI menyatakan bahwa Indonesia harus belajar dari strategi Singapura dalam menarik event internasional kelas dunia. "Kita punya pasar yang besar, kita harus berbenah dari sisi perizinan, infrastruktur, dan keamanan agar promotor global mau membawa artis besar ke Jakarta," ujarnya.

Bagi para fans, konser ini bukan sekadar hiburan, melainkan sebuah pengalaman seumur hidup (once in a lifetime experience). Energi positif, tata panggung yang megah, dan daftar lagu hits yang dibawakan Taylor Swift selama 3,5 jam sukses memuaskan kerinduan fans. Cerita seru dan foto-foto konser membanjiri lini masa media sosial Indonesia selama sepekan penuh.""",
                "category": "Hiburan",
                "tags": ["Internasional", "Viral"],
                "author": "Raffi Ahmad",
                "image": "https://images.unsplash.com/photo-1501281668745-f7f57925c3b4?w=800"
            },
            {
                "title": "Pernikahan Mewah Artis Papan Atas Jadi Sorotan",
                "content": """Pernikahan pasangan selebriti papan atas Indonesia yang digelar di sebuah resort mewah di Bali pada akhir pekan lalu sukses menyita perhatian publik. Pesta pernikahan yang disebut-sebut sebagai "Wedding of The Year" ini berlangsung sangat meriah dan dihadiri oleh deretan artis ternama, pejabat negara, hingga pengusaha sukses. Bahkan, acara resepsi pernikahan ini disiarkan secara eksklusif dan langsung oleh salah satu stasiun televisi swasta nasional.

Kemewahan terlihat dari setiap detail acara. Dekorasi venue disulap bak negeri dongeng dengan ribuan bunga segar yang didatangkan langsung dari luar negeri. Sang pengantin wanita tampil anggun mengenakan gaun rancangan desainer internasional ternama, sementara pengantin pria tampak gagah dengan setelan jas yang dipesan khusus. Souvenir untuk para tamu undangan pun dikabarkan bernilai jutaan rupiah, menambah kesan eksklusif pesta tersebut.

Di media sosial, pernikahan ini menjadi trending topic selama berhari-hari. Netizen memberikan beragam komentar, mulai dari decak kagum atas kemewahan pesta, ucapan selamat dan doa, hingga kritik terkait disiarkannya acara pribadi di frekuensi publik. "Mewah banget, kayak pernikahan pangeran dan putri raja. Semoga langgeng terus ya," tulis salah satu netizen.

Pasangan pengantin baru ini dikabarkan akan segera bertolak ke Eropa untuk menikmati bulan madu romantis selama beberapa minggu. Mereka juga berencana untuk segera kembali bekerja di dunia hiburan setelah masa liburan usai. Pernikahan ini menjadi bukti bahwa kehidupan selebriti Indonesia selalu memiliki daya tarik tersendiri bagi masyarakat luas.""",
                "category": "Hiburan",
                "tags": ["Viral", "Trending"],
                "author": "Feni Rose",
                "image": "https://images.unsplash.com/photo-1519741497674-611481863552?w=800"
            },

            # PENDIDIKAN (3)
            {
                "title": "Pendaftaran SNBP 2024 Resmi Dibuka",
                "content": """Pendaftaran Seleksi Nasional Berdasarkan Prestasi (SNBP) untuk penerimaan mahasiswa baru Perguruan Tinggi Negeri (PTN) tahun 2024 resmi dibuka mulai hari ini. SNBP merupakan jalur seleksi yang menggunakan nilai rapor dan prestasi akademik maupun non-akademik siswa selama di sekolah menengah. Jalur ini menjadi salah satu yang paling diminati karena siswa tidak perlu mengikuti tes tulis, namun persaingannya sangat ketat.

Ketua Umum Tim Penanggung Jawab Seleksi Nasional Penerimaan Mahasiswa Baru (SNPMB) mengingatkan seluruh siswa yang dinyatakan eligible (memenuhi syarat) untuk segera melakukan pendaftaran dan finalisasi data sebelum batas waktu berakhir. "Kami himbau siswa untuk teliti dalam mengisi data dan memilih program studi. Diskusikan dengan orang tua dan guru BK agar pilihan prodi sesuai dengan minat, bakat, dan nilai rapor," pesannya.

Tahun ini, terdapat beberapa aturan baru dalam SNBP, di antaranya sanksi tegas bagi siswa yang sudah dinyatakan lolos SNBP namun tidak mengambilnya. Siswa tersebut akan diblacklist dan tidak diperbolehkan mendaftar di jalur SNBT (tes) maupun jalur mandiri di PTN manapun. Kebijakan ini diambil untuk meningkatkan komitmen siswa dan memberikan kesempatan yang adil bagi siswa lain yang benar-benar serius ingin kuliah.

Para siswa tampak antusias namun juga tegang menyambut pembukaan pendaftaran ini. Sekolah-sekolah juga sibuk memberikan pendampingan kepada siswanya dalam proses pendaftaran. Hasil seleksi SNBP dijadwalkan akan diumumkan pada bulan Maret mendatang. Bagi siswa yang belum beruntung di jalur ini, masih ada kesempatan melalui jalur SNBT dan Seleksi Mandiri.""",
                "category": "Pendidikan",
                "tags": ["Nasional", "Pendidikan"],
                "author": "Nizam",
                "image": "https://images.unsplash.com/photo-1523050854058-8df90110c9f1?w=800"
            },
            {
                "title": "Beasiswa LPDP Tahap 1 Dibuka, Kuota Ditambah",
                "content": """Pemerintah melalui Lembaga Pengelola Dana Pendidikan (LPDP) Kementerian Keuangan kembali membuka pendaftaran beasiswa pendidikan Indonesia Tahap 1 tahun ini. Kabar baiknya, kuota penerima beasiswa tahun ini ditambah secara signifikan dibandingkan tahun sebelumnya. Beasiswa LPDP menawarkan kesempatan bagi putra-putri terbaik bangsa untuk melanjutkan studi jenjang Magister (S2) dan Doktor (S3) di berbagai perguruan tinggi terbaik, baik di dalam maupun di luar negeri.

Direktur Utama LPDP menjelaskan bahwa penambahan kuota ini merupakan wujud komitmen pemerintah untuk meningkatkan kualitas sumber daya manusia (SDM) Indonesia menyongsong Indonesia Emas 2045. "Kita butuh lebih banyak ahli di bidang sains, teknologi, teknik, matematika (STEM), serta kesehatan dan pendidikan. Oleh karena itu, bidang-bidang tersebut menjadi prioritas utama kami," ujarnya. Proses seleksi akan dilakukan secara ketat, transparan, dan akuntabel, meliputi seleksi administrasi, bakat skolastik, dan wawancara.

Selain beasiswa reguler, LPDP juga menyediakan jalur afirmasi untuk masyarakat di daerah 3T, penyandang disabilitas, dan prasejahtera berprestasi. Hal ini untuk menjamin pemerataan akses pendidikan tinggi bagi seluruh lapisan masyarakat. Para alumni LPDP nantinya diwajibkan untuk kembali dan mengabdi di Indonesia, berkontribusi sesuai dengan bidang keilmuannya masing-masing.

Antusiasme pendaftar diprediksi akan membludak. Ribuan calon mahasiswa mulai mempersiapkan dokumen persyaratan seperti sertifikat bahasa asing (TOEFL/IELTS), surat rekomendasi, dan esai rencana studi. Berbagai komunitas pemburu beasiswa juga aktif mengadakan webinar dan sharing session untuk berbagi tips lolos seleksi LPDP. Bagi generasi muda Indonesia, LPDP adalah jembatan emas untuk meraih mimpi pendidikan setinggi-tingginya.""",
                "category": "Pendidikan",
                "tags": ["Nasional", "Trending"],
                "author": "Jerome Polin",
                "image": "https://images.unsplash.com/photo-1523240795612-9a054b0db644?w=800"
            },
            {
                "title": "Program Kampus Mengajar Angkatan 7 Lepas Ribuan Mahasiswa",
                "content": """Kementerian Pendidikan, Kebudayaan, Riset, dan Teknologi (Kemendikbudristek) secara resmi melepas ribuan mahasiswa dari berbagai perguruan tinggi di seluruh Indonesia untuk mengikuti program Kampus Mengajar Angkatan 7. Program ini merupakan bagian dari kebijakan Merdeka Belajar Kampus Merdeka (MBKM) yang memberikan kesempatan kepada mahasiswa untuk belajar di luar kelas dengan menjadi mitra guru di sekolah dasar (SD) dan sekolah menengah pertama (SMP), khususnya di daerah 3T (terdepan, terluar, tertinggal).

Menteri Nadiem Makarim dalam sambutan pelepasannya menyampaikan apresiasi tinggi kepada para mahasiswa yang berani mengambil tantangan ini. "Kalian bukan hanya mengajar, tapi juga belajar tentang realitas pendidikan di lapangan. Tugas kalian adalah membantu meningkatkan literasi dan numerasi siswa, serta mengenalkan adaptasi teknologi di sekolah," pesan Menteri Nadiem. Mahasiswa akan bertugas selama satu semester penuh dan mendapatkan konversi hingga 20 SKS.

Kehadiran mahasiswa Kampus Mengajar diharapkan dapat membawa energi baru dan inovasi pembelajaran yang menyenangkan bagi siswa-siswa di daerah. Mereka akan berkolaborasi dengan guru untuk merancang media pembelajaran kreatif, menghidupkan perpustakaan sekolah, dan memotivasi siswa untuk terus bersekolah. Banyak kisah inspiratif yang lahir dari angkatan-angkatan sebelumnya, di mana kehadiran mahasiswa mampu mengubah wajah sekolah dan semangat belajar siswa.

Bagi mahasiswa, program ini menjadi wadah untuk mengasah soft skills seperti kepemimpinan, pemecahan masalah, dan kepekaan sosial. Pengalaman berinteraksi langsung dengan masyarakat dan menghadapi tantangan nyata di lapangan akan menjadi bekal berharga bagi mereka setelah lulus nanti. Program Kampus Mengajar terus dievaluasi dan disempurnakan untuk memberikan dampak yang lebih luas bagi kemajuan pendidikan Indonesia.""",
                "category": "Pendidikan",
                "tags": ["Nasional", "Daerah"],
                "author": "Maudy Ayunda",
                "image": "https://images.unsplash.com/photo-1509062522246-3755977927d7?w=800"
            }
        ]
        
        for idx, article_data in enumerate(articles_data, 1):
            print(f"Creating article {idx}/{len(articles_data)}: {article_data['title'][:50]}...")
            
            # Find category
            category = Category.query.filter_by(name=article_data['category']).first()
            if not category:
                category = Category.query.first()
            
            # Calculate published date (random 0-10 days ago)
            published_date = datetime.utcnow() - timedelta(days=random.randint(0, 10))
            
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
            for tag_name in article_data['tags']:
                tag = Tag.query.filter_by(name=tag_name).first()
                if tag:
                    article.tags.append(tag)
            
            db.session.add(article)
        
        db.session.commit()
        
        # Create sample bookmarks
        print("Creating sample bookmarks...")
        bookmark1 = Bookmark(user_id=user.id, article_id=1)
        bookmark2 = Bookmark(user_id=user.id, article_id=5)
        bookmark3 = Bookmark(user_id=user.id, article_id=10)
        
        db.session.add_all([bookmark1, bookmark2, bookmark3])
        db.session.commit()
        
        print("\n✅ Database seeded successfully with 30 static articles (Long Content)!")
        print("\n📊 Summary:")
        print(f"   - Users: {User.query.count()}")
        print(f"   - Categories: {Category.query.count()}")
        print(f"   - Tags: {Tag.query.count()}")
        print(f"   - Articles: {Article.query.count()}")
        print(f"   - Bookmarks: {Bookmark.query.count()}")

if __name__ == '__main__':
    seed_database()
