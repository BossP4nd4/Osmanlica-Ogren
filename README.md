<p align="center"><img src="kapak.svg" alt="Osmanlıca — Oku, anla, tekrar et" width="100%"></p>
<p align="center"><strong>Osmanlıca okumayı öğrenmek için dersler, kaynak kitaplar ve sözlük bir arada.</strong></p>
<p align="center">iPhone · iOS 26+ · Apple Silicon Mac ile kurulum · Sürüm 1.0.0 (5)</p>
<p align="center"><a href="https://github.com/BossP4nd4/Osmanlica-Ogren/releases/tag/v1.0.0-arsiv.20261015"><b>↓ Paketleri indir</b></a> &nbsp; · &nbsp; <a href="#kurulum">Kurulum</a> &nbsp; · &nbsp; <a href="KURULUM-KILAVUZU.txt">Ayrıntılı kılavuz</a> &nbsp; · &nbsp; <a href="https://github.com/BossP4nd4/Osmanlica-Ogren/issues">Sorun bildir</a></p>

---

## Osmanlıca nedir?

Osmanlıca, Osmanlı Türkçesi metinlerini okumaya çalışanlar için geliştirilmiş bir iPhone uygulamasıdır. Dersleri özgün kaynak sayfalarıyla birlikte incelemeyi, kitap okumayı, sözlükte araştırma yapmayı ve öğrenilenleri aralıklı tekrarla pekiştirmeyi bir araya getirir. Hazır içerikler ve kurulu sözlükler çevrimdışı kullanılabilir.

| Öğren | Kaynağa dön | Pekiştir |
| :--- | :--- | :--- |
| 38 ders ve 870 çalışma grubu | Uygulama içindeki 55 PDF kitap | FSRS tabanlı tekrar, notlar ve yer imleri |
| Okuma ve değerlendirme çalışmaları | Özgün sayfa görüntülerine geçiş | İlerleme ve tam yedek aktarımı |
| Ayrı kurulabilen sözlük paketi | 10.294 arama kaydı ve 3 sözlük PDF’si | Dosya, metin ve bağlantı içe aktarma |

Bu sayılar 15 Ekim 2026 tarihli arşiv kılavuzuna aittir. Sözlük indeksi Devellioğlu’nun Latin başlıklarına dayanır; bütün sözlüklerin eksiksiz metin aktarımı veya OCR sistemi değildir.

## İndir

**İlk kurulum için 01 ve 02 paketlerini indir. Tam arşivi saklamak için üç paketi de indir.**

[Releases sayfasını aç](https://github.com/BossP4nd4/Osmanlica-Ogren/releases/tag/v1.0.0-arsiv.20261015) ve **Assets** bölümündeki aşağıdaki dosyaları kullan:

| Paket | Yaklaşık indirme | İçerik |
| :--- | ---: | :--- |
| [01 · Kaynak kodu ve kılavuzlar](https://github.com/BossP4nd4/Osmanlica-Ogren/releases/download/v1.0.0-arsiv.20261015/01-kaynak-kod-ve-kilavuzlar.zip) | 1,90 GB | Xcode projesi, uygulama içerikleri, yerel kütüphaneler, bağımlılık kaynakları ve kurulum belgeleri |
| [02 · Sözlük paketi](https://github.com/BossP4nd4/Osmanlica-Ogren/releases/download/v1.0.0-arsiv.20261015/02-sozluk-paketi.zip) | 413 MB | Sözlük indeksi ve üç kaynak PDF |
| [03 · Hazır IPA arşivi](https://github.com/BossP4nd4/Osmanlica-Ogren/releases/download/v1.0.0-arsiv.20261015/03-hazir-ipa.zip) | 1,73 GB | Önceden imzalanmış uygulama çıktısı; yeni Apple hesabıyla kurulum için kaynak proje kullanılır |

> **GitHub’ın “Code → Download ZIP” veya otomatik “Source code” indirmesi tam uygulama paketini içermez.** Büyük dosyalar yukarıdaki üç Release ekindedir. Bu depo, kurulum arşivi ve belgelerin dağıtım sayfasıdır; Xcode kaynak projesi 01 numaralı paketin içindedir.

### Paketleri aç

**Finder ile:** Her ZIP’e çift tıkla. İlk paketteki `01-Sifirdan-Kurulum` klasörünü esas al. İkinci paketten çıkan `Sozluk-Paketi` klasörünü bu klasörün içine taşı. Üçüncü paketi de indirdiysen içindeki `Hazir-IPA` klasörünü aynı yere taşı. Var olan ana klasörü başka bir ana klasörle değiştirme; yalnız ilgili alt klasörleri ekle.

**Tam arşiv için otomatik yol:** Üç ZIP’i ve [PAKETLERI_AC.py](PAKETLERI_AC.py) dosyasını aynı klasöre indir. Python 3 kurulu Mac’te bu klasörden aşağıdaki komutu çalıştır. Araç önce üç paketin SHA-256 değerlerini doğrular, ardından yeni bir `Osmanlica-Kurulum` klasörüne açar. Mevcut klasörün üzerine yazmaz.

```bash
python3 PAKETLERI_AC.py
```

Oluşacak temel yapı:

```text
Osmanlica-Kurulum/
├── 00-BURADAN-BASLA.txt
├── PAKET-OZETI.json
└── 01-Sifirdan-Kurulum/
    ├── Osmanlica-Kisisel-Kurulum-Kilavuzu.pdf
    ├── KURULUM-KILAVUZU.txt
    ├── Yeniden-Derleme/Proje/Osmanlica.xcodeproj
    ├── Sozluk-Paketi/
    └── Hazir-IPA/
```

## Kurulum

### Gerekenler

- Apple Silicon işlemcili Mac. Hazır yerel kütüphaneler Intel Mac için hazırlanmadı.
- iOS 26 veya üzerini çalıştıran iPhone ve bu iOS sürümünü destekleyen Xcode.
- Apple hesabı, veri aktarabilen kablo ve ilk kurulum için internet.
- Mac’te Xcode ve derleme için yaklaşık 35–50 GB çalışma alanı; telefonda içerikler için yeterli boş alan.

Arşiv, kendi sürüm kaydına göre Xcode 27.0 ve macOS 26.6.2 ile hazırlanmıştır. Xcode ve Apple SDK’ları pakete dahil değildir. Normal kurulumda Rust’ı ayrıca yüklemek gerekmez; hazır XCFramework bulunur.

### iPhone’a kaynak kodundan kur

1. Mac App Store’dan Xcode’u kur ve ilk açılış bileşenlerini tamamla.
2. Açtığın arşivin bir çalışma kopyasını oluştur. `01-Sifirdan-Kurulum/Yeniden-Derleme/Proje/Osmanlica.xcodeproj` dosyasını Xcode ile aç.
3. **Xcode → Settings → Apple Accounts** bölümünden kendi Apple hesabını ekle.
4. **TARGETS → Osmanlica → Signing & Capabilities** bölümünde **Automatically manage signing** seçeneğini aç ve kendi **Personal Team** hesabını seç. İlk kurulumda benzersiz bir Bundle Identifier belirle; örneğin `com.adin.osmanlica`.
5. iPhone’u kabloyla bağla, güven ve eşleştirme adımlarını tamamla. iOS isterse **Ayarlar → Gizlilik ve Güvenlik → Geliştirici Modu** adımlarını uygula.
6. Xcode’da **Osmanlica** şemasını ve hedef olarak kendi iPhone’unu seç; **⌘R** ile derle ve çalıştır.
7. Telefonda bir ders ve kaynak kitabı açarak kurulumu kontrol et.

> Ücretsiz Personal Team profilleri **7 gün** sonra sona erer. Aynı Apple hesabı ve Bundle Identifier ile yeniden derleme/kurulum gerekir. Uygulamayı silmeden önce ilerlemeni yedekle. [Apple’ın güncel Personal Team açıklaması](https://developer.apple.com/help/account/basics/about-your-developer-account).

**Test durumu:** Arşivin hazırlık kayıtlarında ücretsiz Personal Team ile gerçek iPhone kurulumu test edilmemiş olarak işaretlidir. Dosyaların sağlamlığı, bu kurulumun her cihazda başarıyla tamamlandığı anlamına gelmez.

### Sözlüğü ekle

1. Açılmış `Sozluk-Paketi` klasörünü Mac’te sıkıştır ve iPhone’a Finder’ın **Dosyalar → Osmanlıca** bölümüyle aktar.
2. iPhone’un Dosyalar uygulamasında ZIP’i aç.
3. Osmanlıca’da **Sözlük → Sözlük paketini kur → Kurulum klasörünü seç** yolunu izle.
4. `dictionary-install.json`, `Lexicons` ve `Sources` öğelerinin birlikte bulunduğu klasörü seç; ön kontrolü okuyup kurulumu başlat.
5. `kitab` aramasıyla `kitâb` sonucunu ve özgün kaynak sayfasını kontrol et.

Release’ten indirilen 02 numaralı ZIP, arşiv klasör yapısını da içerir. Telefona doğrudan bu ZIP’i taşırsan iç içe klasörlerden geçerek yukarıdaki üç öğenin birlikte bulunduğu seviyeyi seç.

### Mac’te dene

Xcode’da uygun iOS Simulator bileşenini kur, aynı projede iPhone Simulator hedefini seç ve **⌘R** ile çalıştır. Simülatör ilerlemesi telefonla kendiliğinden eşitlenmez; taşıma için uygulamanın tam yedek özelliğini kullan.

## Kılavuzlar ve doğrulama

- [Ayrıntılı kurulum kılavuzu](KURULUM-KILAVUZU.txt) — hesap, imzalama, sözlük, simülatör ve sorun giderme.
- [Görselli PDF kılavuzu](Osmanlica-Kisisel-Kurulum-Kilavuzu.pdf) — çizimler şematiktir, uygulama ekran görüntüsü değildir.
- [Paket SHA-256 değerleri](SHA256SUMS.txt) — indirilen üç ZIP için.
- [Dosya envanteri](DOSYA-ENVANTERI.json) — 2.585 dosyanın yolu, boyutu, SHA-256 değeri ve bulunduğu paket.

Paketleme sırasında bütün dosyalar ZIP içinden tekrar okunarak yerel kaynaklarla SHA-256 düzeyinde eşleştirildi. Tam arşivi açtıktan sonra orijinal denetleyici de çalıştırılabilir:

```bash
cd 01-Sifirdan-Kurulum
python3 BUTUNLUGU_KONTROL_ET.py
```

Proje ayarlarını değiştirmeden önce doğrulama yap. Xcode’da imzalama ve uygulama kimliği değiştirildiğinde ilgili dosyaların hash değerlerinin değişmesi normaldir.

## Bilinen sınırlar

- Ücretsiz kurulum kopyasında paylaşım uzantısı ve App Groups kapalıdır; uygulama içindeki dosya/metin/bağlantı içe aktarma seçenekleri kullanılır.
- Hazır IPA eski hesabın imzasını taşır; yeni hesap için doğrudan kurulum garantisi vermez.
- Sözlükte tüm kaynaklar tam metin olarak aranamaz; özgün PDF sayfaları başvuru kaynağıdır.
- Yeni Xcode ve iOS sürümleri ileride kod veya ayar uyarlaması gerektirebilir.
- Uygulama arşivi, kullanıcının son çalışma ilerlemesinin yedeği değildir.

<details>
<summary><strong>Arşiv kapsamı hakkında</strong></summary>

Bu yayın, 15 Ekim 2026 arşivinden `00-BURADAN-BASLA.txt`, `PAKET-OZETI.json` ve `01-Sifirdan-Kurulum` klasörünün eksiksiz kopyasını içerir. Özgün dosyalar değiştirilmeden paketlenmiştir. Başlangıç notunda anılan 02–06 klasörleri bu yayının kapsamı değildir. `PAKET-OZETI.json` daha geniş yerel arşivin özgün özetidir; bu GitHub yayınının dosya sayısı için `DOSYA-ENVANTERI.json` esas alınmalıdır.

</details>

## Sorun bildirme

[Issues](https://github.com/BossP4nd4/Osmanlica-Ogren/issues) üzerinden macOS, Xcode ve iOS sürümlerini, denediğin adımı ve hata mesajını paylaş. Parola, doğrulama kodu veya kişisel yedek ekleme.

---

<sub>Osmanlıca · 15 Ekim 2026 arşiv yayını · Uygulama sürümü 1.0.0 (5)</sub>
