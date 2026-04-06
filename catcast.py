import requests
import re

# Список каналов (добавляй свои)
channels = {
    "balacan_tv": "https://example.catcast.tv/channel-page"
}

headers = {
    "User-Agent": "Mozilla/5.0",
    "Referer": "https://catcast.tv/"
}

def find_m3u8(url):
    try:
        response = requests.get(url, headers=headers, timeout=10)
        html = response.text

        # ищем ссылку .m3u8
        match = re.search(r'https?://[^"]+\.m3u8[^"]*', html)

        if match:
            return match.group(0)
        else:
            return None
    except Exception as e:
        print(f"Ошибка: {e}")
        return None

def create_playlist():
    content = "#EXTM3U\n"

    for name, url in channels.items():
        stream = find_m3u8(url)

        if stream:
            print(f"[OK] {name}")
            content += f'#EXTINF:-1,{name}\n{stream}\n'
        else:
            print(f"[FAIL] {name}")

    with open("catcast.m3u8", "w", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":
    create_playlist()
