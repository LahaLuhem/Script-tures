import requests
import sys
import subprocess
import random


class bg:
    PINK = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    NORM = '\033[0m'

def main():
    if len(sys.argv) == 1:
        sys.exit("Please rerun the command in the format: \n ~ $ torrentcli movie name")
    args = sys.argv[1:]

    for i in args:
        if "-" in i:
            args.remove(i)
    search = ("+".join(args)).replace(" ", "+")
    sites = ["librex.extravi.dev", "librex.beparanoid.de", "search.davidovski.xyz", "search.funami.tech", "search.madreyk.xyz"]
    site = random.choice(sites)
    URL = f"https://{site}/api.php?q={search}&p=0&type=3"
    data = requests.get(url=URL)
    data = data.json()
    print(args, "\n", search, "\n", site, "\n", URL, "\n")

    numberOfOutputs = 8
    torrentStream = "vlc"

    def output(a):
        for i in range(a):
            torrent = data[i]
            if torrent["seeders"] != 0:
                name = str(torrent['name'])
                seeders = str(torrent['seeders'])
                leechers = str(torrent['leechers'])
                size = str(torrent['size'])
                source = str(torrent['source'])
                print(f"[{i + 1}]{bg.RED} {name} \n ---{bg.GREEN} [se] {seeders} {bg.PINK} [le] {leechers} {bg.BLUE} [size] {size} {bg.YELLOW} [src] {source} {bg.NORM}")

    if len(data) < numberOfOutputs:
        a = len(data)
    else:
        a = numberOfOutputs
    output(a)

    try:
        x = int(input("Which torrent would you like? ")) - 1
    except ValueError:
        print("Please enter a number between 1 and ")

    if "1337x" in data[x]['source']:
        re = str(f"https://{site}{data[x]['magnet']}")
        magnet = re
        # print(headers)
    else:
        magnet = data[x]["magnet"]

    if "-s" in sys.argv:
        subprocess.run(f"{torrentStream} '{magnet}'")
    else:
        print(magnet)
        subprocess.run(["deluge.lnk", magnet], shell=True)
try:
    main()
except KeyboardInterrupt:
    print("Exiting...")
