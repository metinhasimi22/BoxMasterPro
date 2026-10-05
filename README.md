# BoxMasterPro

BoxMasterPro, boks antrenmanları için tasarlanmış modern bir yardımcı uygulamadır. Uygulama rastgele vuruş kombinasyonları üretir, raunt sürelerini yönetir, dinlenme aşamasını takip eder ve Windows için paketlenmeye uygun bir çalıştırılabilir dosya üretir.

## Özellikler
- Karanlık mod modern arayüz
- Uygulama simgesi ve açılış ekranı desteği
- Rastgele vuruş kombinasyonu üretme
- 3 dakikalık raunt ve dinlenme takibi
- Başlat / durdur / sıfırla kontrolü
- Sesli uyarı sistemi (Windows, macOS, Linux için uyarlanmış)
- Otomatik sürüm numarası kontrolü
- PyInstaller ile `.exe` üretimi
- Inno Setup için kurulum betiği

## Kurulum

```bash
python -m pip install -r requirements.txt
```

## Uygulamayı Çalıştırma

```bash
python main.py
```

## Uygulama ikonlarını ve splash ekranını üretme

```bash
python generate_assets.py
```

## Windows EXE oluşturma

```bash
python build_exe.py
```

Bu işlem `dist/BoxMasterPro.exe` dosyasını üretir.

## Kurulum dosyası oluşturma

Inno Setup kurulu olmalıdır:

```bash
"C:\Program Files (x86)\Inno Setup 6\ISCC.exe" installer\BoxMasterPro.iss
```

Bu işlem `installer\Output\BoxMasterPro-Setup.exe` dosyasını oluşturur.

## Sürüm yönetimi

- Sürüm bilgisi: `VERSION` dosyasında tutulur.
- Uygulama kodu: `version.py` içinde tanımlıdır.
- PyInstaller sürüm metni: `version_info.txt` kullanılır.

## Notlar
- `generate_assets.py`, ikon ve açılış ekranını otomatik üretir.
- `BoxMasterPro.iss` kurulumu için Inno Setup kullanır.
- Uygulama, Windows için tüm üretim gereksinimlerini karşılamak üzere tasarlanmıştır.

