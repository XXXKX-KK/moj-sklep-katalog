# Porta — katalog

Zawartość tego folderu to **całe publiczne repo `XXXKX-KK/moj-sklep-katalog`**.
Sklep czyta stąd jeden plik:

`https://raw.githubusercontent.com/XXXKX-KK/moj-sklep-katalog/main/apps.json`

| Plik          | Po co                                                                       |
| ------------- | --------------------------------------------------------------------------- |
| `apps.json`   | lista aplikacji w sklepie                                                   |
| `ikony/*.png` | ikony aplikacji (kwadrat, najlepiej 512×512, sklep sam zaokrągla rogi)      |
| Releases      | `moj-sklep.apk` — wydania samego sklepu (wrzuca je workflow „Wydaj wersję”) |

## Format wpisu

```json
{
  "packageName": "com.gradus.app",
  "name": "GRADUS",
  "shortDesc": "Jedno zdanie na listę",
  "description": "Pełny opis pod „Więcej”",
  "versionCode": 1004,
  "versionName": "2026.10.08-4",
  "apkUrl": "https://github.com/XXXKX-KK/gradus-pobierz/releases/download/v1004/gradus.apk",
  "iconUrl": "https://raw.githubusercontent.com/XXXKX-KK/moj-sklep-katalog/main/ikony/gradus.png",
  "accentColor": "#22C55E",
  "screenshots": ["https://…/1.png", "https://…/2.png"],
  "videoUrl": "https://github.com/…/releases/download/…/demo.mp4",
  "videoThumbUrl": "https://…/miniatura.png",
  "changelog": "Co się zmieniło",
  "sizeMb": 3.9
}
```

- `screenshots`, `videoUrl`, `videoThumbUrl` są opcjonalne. Bez nich karuzela się
  dopasowuje albo znika.
- `apkUrl` musi być `https://` i na GitHubie — inny adres sklep odrzuci.
- Pole `_todo` sklep ignoruje — to notatka dla Ciebie.
- Zły wpis (literówka, brak pola) wypada sam; reszta katalogu działa dalej.
  Plik, w którym nie ma ani jednego dobrego wpisu, sklep ignoruje i zostaje przy
  ostatniej dobrej wersji.

## Co jeszcze jest TODO

- TENAX i GRADUS: `screenshots`, `videoUrl`, `videoThumbUrl` (opcjonalne).
- Porta: wpis uzupełni się sam przy pierwszym uruchomieniu „Wydaj wersję”.
