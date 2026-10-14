"""Podbija wersje w apps.json na podstawie version.json z repo "-pobierz" każdej aplikacji.

Sklep czyta tylko apps.json. Aplikacje wydają się same (każda w swoim repo),
więc ten skrypt co kilkanaście minut sprawdza ich najnowsze version.json
i przepisuje do katalogu: versionCode, versionName, apkUrl, changelog, sizeMb.
Wpis samej Porty pomija: ten podbija jej własny workflow wydania.
"""
import json
import sys
import urllib.request

STORE_PACKAGE = "com.kuba.sklep"


def fetch(url, method="GET"):
    req = urllib.request.Request(url, method=method, headers={"User-Agent": "porta-sync"})
    return urllib.request.urlopen(req, timeout=30)


def pobierz_repo(apk_url):
    # https://github.com/OWNER/REPO/releases/download/TAG/plik.apk -> OWNER/REPO
    parts = apk_url.split("/")
    return f"{parts[3]}/{parts[4]}" if len(parts) > 4 and parts[2] == "github.com" else None


def main():
    with open("apps.json", encoding="utf-8") as f:
        apps = json.load(f)
    changed = False
    for app in apps:
        if app.get("packageName") == STORE_PACKAGE:
            continue
        repo = pobierz_repo(app.get("apkUrl", ""))
        if not repo:
            continue
        try:
            info = json.load(fetch(f"https://github.com/{repo}/releases/latest/download/version.json"))
        except Exception as e:  # brak wydania / sieć — zostawiamy wpis bez zmian
            print(f"{app['name']}: pomijam ({e})")
            continue
        code = info.get("versionCode")
        if not isinstance(code, int) or code <= app.get("versionCode", 0):
            print(f"{app['name']}: bez zmian ({app.get('versionCode')})")
            continue
        apk = info.get("apkUrl") or app["apkUrl"]
        try:
            size = int(fetch(apk, "HEAD").headers.get("Content-Length", 0))
        except Exception:
            size = 0
        notes = (info.get("notes") or "").strip()
        app.update(
            versionCode=code,
            versionName=info.get("versionName", app.get("versionName")),
            apkUrl=apk,
            changelog=notes.splitlines()[0].lstrip("- ").strip() if notes else app.get("changelog", ""),
        )
        if size:
            app["sizeMb"] = round(size / 1048576, 1)
        print(f"{app['name']}: -> {code}")
        changed = True
    if changed:
        with open("apps.json", "w", encoding="utf-8") as f:
            f.write(json.dumps(apps, ensure_ascii=False, indent=2) + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
