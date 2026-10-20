# Osmanlıca · iPhone / iPad

**Osmanlıca okumayı dersler, kaynak açıklamaları ve uygulamalı çalışmalarla öğren.**

**Güncel: 1.2.0 (7)** · iOS 26+ · 20 Ekim 2026 yayını

[Android sürümü](https://github.com/BossP4nd4/Osmanlica-Ogren-Android) · [Tüm indirmeler](https://github.com/BossP4nd4/Osmanlica-Ogren-Apple/releases/tag/v1.2.0)

## Önce hangi dosyaları indireceğini seç

**İlk kurulum için Apple Silicon Mac, uygun Xcode, Apple hesabı ve iPhone gerekir.** Bu yayın App Store bağlantısı değildir. Normal kurulum yolu kaynak projeyi Xcode’da kendi hesabınla derlemektir.

| Sıra | Dosya | İndirme boyutu |
| --- | --- | --- |
| 1 | [⬇ Kaynak proje — Mac’e indir](https://github.com/BossP4nd4/Osmanlica-Ogren-Apple/releases/download/v1.2.0/Osmanlica-iOS-Kaynak-Kod.zip) | 33.3 MB |
| 2A | [⬇ Hafif ders içeriği](https://github.com/BossP4nd4/Osmanlica-Ogren-Apple/releases/download/v1.2.0/Osmanlica-iOS-Hafif-Icerik.zip) | 92.8 MB |
| 2B | [⬇ Tam kitaplık](https://github.com/BossP4nd4/Osmanlica-Ogren-Apple/releases/download/v1.2.0/Osmanlica-iOS-Tam-Kitaplik.zip) | 1730.9 MB |
| 3 | [⬇ Sözlük paketi — iki seçenek için de aynı](https://github.com/BossP4nd4/Osmanlica-Ogren-Apple/releases/download/v1.2.0/Osmanlica-iOS-Sozluk.zip) | 403.5 MB |

**2A veya 2B’den yalnız birini seç.** Sözlüğü kullanmak için 3’ü de indir. Uygulamanın içinde kitapların ikinci bir PDF kopyası yoktur; ilk açılışta ders paketini ayrıca kurarsın.

> **iOS’ta ZIP’i Dosyalar uygulamasında açıp içindeki klasörü seçersin.** Android’deki ZIP’i doğrudan seçme yöntemi burada geçerli değildir.
> GitHub’ın **Code → Download ZIP** veya otomatik **Source code** dosyaları yukarıdaki paketlerin yerine geçmez.

## 1. Uygulamayı Mac’ten iPhone’a kur

1. Kaynak ZIP’ini Mac’te aç. **Proje → Osmanlica.xcodeproj** dosyasını Xcode ile aç; `Package.swift` dosyasını seçme.
2. Xcode → Settings → Accounts bölümünden Apple hesabını ekle.
3. Projede **Osmanlica** hedefi → **Signing & Capabilities** → **Automatically manage signing** seçili olsun. **Team** olarak kendi hesabını seç.
4. İlk kurulumda kendine özgü Bundle Identifier belirle; örneğin `com.adin.osmanlica`. Hesabı ve kimliği sakla; güncellemelerde aynılarını kullan.
5. iPhone’u kabloyla bağla, güven istemini onayla. Gerekiyorsa iPhone’daki **Ayarlar → Gizlilik ve Güvenlik → Geliştirici Modu** adımlarını tamamla.
6. Xcode üst çubuğunda **Osmanlica** şeması ve kendi iPhone’un seçiliyken **Run / ▶** düğmesine bas. İstenirse iPhone’da geliştiriciye güven adımını tamamla.

Bu taşınabilir proje paylaşım uzantısı/App Group gerektirmeyen kurulum kopyasıdır; uygulamanın içinden dosya ekleyebilirsin. Hazır yerel kütüphaneler vardır; normal kurulumda Rust derlemek gerekmez.

**Ücretsiz Apple hesabında yenileme:** Personal Team imzasının profili 7 gün sonra sona erer; aynı hesap ve Bundle Identifier ile Xcode’dan yeniden derleyip yükle. Uygulamayı silme. [Apple’ın açıklaması](https://developer.apple.com/help/account/basics/about-your-developer-account).

## 2. Hafif veya tam ders paketini kur

1. Seçtiğin ders ZIP’ini Finder → iPhone → Dosyalar → Osmanlıca üzerinden telefona aktar.
2. Telefonda **Dosyalar → iPhone’umda → Osmanlıca** içinde ZIP’e dokunup aç.
3. Uygulamanın ilk açılışında **Ders kurulum klasörünü seç**’e dokun.
4. Açılan **Hafif-Icerik** veya **Tam-Kitaplik** klasörüne gir. **catalog.json ve Assets** birlikte görünürken **Aç**’a bas.
5. Ön kontroldeki içerik seçimini ve boş alanı kontrol et; **Kitapları ve çalışmaları kur** ile tamamla.

Tek PDF’yi, ZIP dosyasını veya bir üst klasörü seçme. Sonrasında bir ders ve kaynak sayfasını açarak kontrol et.

## 3. Sözlüğü ekle

1. Sözlük ZIP’ini de telefona aktar ve Dosyalar’da aç.
2. **Sözlük → Sözlük paketini kur → Kurulum klasörünü seç** yolunu aç.
3. **Sozluk-Paketi** içine gir: **Lexicons, Sources ve dictionary-install.json** birlikte görünürken klasörü seç.
4. Kurulumdan sonra `kitab` aramasını, sözlük maddesini ve tam kaynak sayfasını kontrol et.

**Depolama:** Sözlük dahil temel dosya toplamı hafifte yaklaşık **608 MB**, tam kitaplıkta yaklaşık **2,37 GB**. Bunlar telefonun Ayarlar ekranıyla birebir aynı ölçüm değildir. Aktarım ZIP’leri, açılmış kopyalar, kişisel kayıtlar ve önbellek ek yer ister. Kullanılmış kurulumda eski cevapların kaynak kanıtları da saklanabilir.

## Mevcut kurulumdan güncelleme ve paket değiştirme

1. Eski uygulamada **Bugün → Ayarlar → Dosyalar’a tam yedek aktar** ile yedek al; Mac’te ayrı bir kopya tut.
2. Yeni kaynak projeyi aynı Apple hesabı ve **aynı Bundle Identifier** ile mevcut uygulamanın üzerine yükle. Uygulamayı önceden silme.
3. Bu yayının yeni ders paketlerinden birini indir. **Ayarlar → ders/içerik güncellemeleri → Hafif içerik / Tam kitaplık** üzerinden açılmış klasörü seçip kurulumu tamamla.
4. Kayıtlarını, notlarını ve tekrarlarını kontrol et. Paket geçişinde bunlar korunur; hafifte olmayan sayfalardaki yer imleri tam kitaplık için saklanır.
5. Sözlük paketi bu güncellemede genişletilmedi; kurulu sözlük düzgün açılıyorsa tekrar kurman gerekmez.

İki uygulama simgesi veya boş ilerleme görürsen farklı hesap/kimlik kullanılmış olabilir; eski uygulamayı silmeden yedeğini koru. İçerik ve kayıtlar doğrulandıktan sonra yalnız aktarım ZIP’lerini/açılmış aktarım klasörlerini kaldır; uygulamanın verilerini silme.

## Bu güncellemede neler var?

- **38 ders ve 874 çalışma.** Derslere 171 kaynak açıklaması, 15 etkileşimli tablo ve 401 tablo hücresi; 149 kısa örnek ve bütünlüklü okumalar eşlik ediyor.
- **Hafif içerik / Tam kitaplık:** aynı dersler, açıklamalar ve çalışmalar; farklı kitap erişimi ve depolama kullanımı.
- Hafif içerik, düşük çözünürlüklü ekran görüntüsü veya ders özeti değildir. Dersler için gereken **573 özgün PDF sayfası**, özgün sayfa numaralarıyla korunur.
- Tam kitaplık, 55 ders PDF’sinin **14.318 sayfasına** erişim sağlar. Üç sözlük PDF’si her iki seçenekte de tamdır; sözlük kapsamı bu güncellemede artırılmadı.
- İlgili dosyalar doğrulanıp kurulduktan sonra içerik seçimi değişir. Hafifte erişilemeyen sayfalardaki yer imleri, tam kitaplığa dönüldüğünde kullanılmak üzere saklanır.

## Hafif mi, tam mı?

| İhtiyacın | Seçim |
| --- | --- |
| Dersleri ve alıştırmaları çalışmak; telefonda daha az yer kullanmak | **Hafif içerik** |
| Kaynak kitapların ders dışında kalan sayfalarını da okumak | **Tam kitaplık** |

İki içerik paketini birlikte indirmen gerekmez. Sonradan diğerine geçebilirsin. Kişisel kayıtlar, yedekler, aktarım dosyaları ve önbellek ayrıca yer kaplar.

## Kılavuz ve isteğe bağlı dosyalar

- [20 sayfalık görselli kurulum kılavuzu](https://github.com/BossP4nd4/Osmanlica-Ogren-Apple/releases/download/v1.2.0/Osmanlica-iOS-Kurulum-Kilavuzu.pdf). Kılavuzdaki `Yeniden-Derleme/Proje` yolu bu GitHub kaynak ZIP’inde doğrudan **Proje** klasörüdür. `Ders-Paketleri` ve `Sozluk-Paketi` ayrı indirmeler olarak sunulmuştur.
- [Hazır imzalı IPA (isteğe bağlı)](https://github.com/BossP4nd4/Osmanlica-Ogren-Apple/releases/download/v1.2.0/Osmanlica-iOS-1.2.0.ipa). Özgün geliştirici hesabına bağlıdır; herkesin indirip dokunarak kurabileceği bir paket değildir. Yeni ücretsiz hesapla kurulum için kaynak proje yolunu kullan.
- [Dosya doğrulama değerleri (SHA-256)](https://github.com/BossP4nd4/Osmanlica-Ogren-Apple/releases/download/v1.2.0/SHA256SUMS.txt).

Kaynak ZIP’inde uygulamaya gömülmeyen eski `App/Resources/Prepared` PDF kopyaları tekrarlanmaz; ders kitapları ayrı içerik paketlerindedir. Özel yerel imzalama ayarı ve kişisel cihaz yedekleri paylaşılmaz.

**Test durumu:** Yerel rapora göre yeni iOS paketi imzalı derlendi; kurulum/depolama/geçiş çekirdek testleri geçti. Bu yeni sürüm fiziksel iPhone’a kurulmadı; yeni ücretsiz hesapla telefon kurulumu denenmedi. Son yeni kurulum ekranının görsel denetimi tamamlanamadı. Bu GitHub yayını için uygulama yeniden derlenmedi; hazırlanmış güncel dosyalar paketlendi.

[Sorun bildir](https://github.com/BossP4nd4/Osmanlica-Ogren-Apple/issues): iOS/Xcode sürümünü, hafif/tam seçimini ve hata metnini belirt. Özel yedeğini veya hesap bilgilerini paylaşma.
