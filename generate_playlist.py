
import requests

MAIN_FILE = "combined_main.m3u"
DEAD_FILE = "dead_links.m3u"
SOURCES_FILE = "sources.txt"

def is_alive(url):
    try:
        r = requests.head(url, timeout=5)
        return r.status_code < 400
    except:
        return False

def main():
    with open(SOURCES_FILE, "r") as f:
        urls = [x.strip() for x in f.readlines() if x.strip()]

    alive = []
    dead = []

    for url in urls:
        if is_alive(url):
            alive.append(url)
        else:
            dead.append(url)

    # Write alive links
    with open(MAIN_FILE, "w") as f:
        f.write("#EXTM3U\n")
        for u in alive:
            f.write(f"#EXTINF:-1,{u}\n{u}\n")

    # Write dead links
    with open(DEAD_FILE, "w") as f:
        f.write("#EXTM3U\n")
        for u in dead:
            f.write(f"#EXTINF:-1, DEAD – {u}\n{u}\n")

if __name__ == "__main__":
    main()
