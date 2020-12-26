import requests
from bs4 import BeautifulSoup
from colorama import Fore, Back, Style, init

init(autoreset=True)


def get_status_steam(url_steam):
    def out_red(text):
        print("\033[31m {}".format(text))

    def out_yellow(text):
        print("\033[33m {}".format(text))

    def out_green(text):
        print("\033[32m {}".format(text))

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    response = requests.get(url_steam, headers=headers).json()

    # STEAM_STATUS

    h = (response.get('services')[45])  # Online on Steam
    print(f"Кол-во игроков в стиме - {Fore.BLUE + h[2]}")

    z = (response.get('services')[2])  # Steam Connection Managers
    print(f"% игроков без проблем - {Fore.BLUE + z[2]}")

    g = (response.get('services')[38])  # In-Game on Steam
    print(f"Кол-во игроков в играх стим - {Fore.BLUE + g[2]}")

    c = (response.get('services')[3])  # Steam Community_status
    if 'Normal' in c:
        print(f"Статус сообщества Steam - {Fore.GREEN + c[2]}")
    elif 'Critical' in c:
        print(f"Статус сообщества Steam - {Fore.YELLOW + c[2]}")
    else:
        print(f"Статус сообщества Steam - {Fore.RED + c[2]}")

    m = (response.get('services')[60])  # Steam Web API
    if 'Normal' in m:
        print(f"Статус Steam Web API - {Fore.GREEN + m[2]}")
    elif 'Critical' in m:
        print(f"Статус Steam Web API - {Fore.YELLOW + m[2]}")
    else:
        print(f"Статус Steam Web API - {Fore.RED + m[2]}")

    j = (response.get('services')[53])  # Store_status
    if 'Normal' in j:
        print(f"Статус магазина стим - {Fore.GREEN + j[2]}")
    elif 'Critical' in j:
        print(f"Статус магазина стим - {Fore.YELLOW + j[2]}")
    else:
        print(f"Статус магазина стим - {Fore.RED + j[2]}")

    # /STEAM_STATUS

    # CS_GO_STATUS

    b = (response.get('services')[4])  # CS_GO_status
    if 'Normal' in b:
        print(f"Статус серверов cs_go - {Fore.GREEN + b[2]}")
    elif 'Critical' in b:
        print(f"Статус серверов cs_go - {Fore.YELLOW + b[2]}")
    else:
        print(f"Статус серверов cs_go - {Fore.RED + b[2]}")

    x = (response.get('services')[23])  # CS_GO Sessions Logon
    if 'Normal' in x:
        print(f"Статус подключения к серверам cs_go - {Fore.GREEN + x[2]}")
    elif 'Critical' in x:
        print(f"Статус подключения к серверам cs_go - {Fore.YELLOW + x[2]}")
    else:
        print(f"Статус подключения к серверам cs_go - {Fore.RED + x[2]}")

    d = (response.get('services')[11])  # CS_GO_Player Inventories_status
    if 'Normal' in d:
        print(f"Статус инвентаря cs_go - {Fore.GREEN + d[2]}")
    elif 'Critical' in d:
        print(f"Статус инвентаря cs_go - {Fore.YELLOW + d[2]}")
    else:
        print(f"Статус инвентаря cs_go - {Fore.RED + d[2]}")

    # /CS_GO_STATUS

    # Artifact_STATUS

    a = (response.get('services')[1])  # Artifact_status
    if 'Normal' in a:
        print(f"Статус Artifact - {Fore.GREEN + a[2]}")
    elif 'Critical' in a:
        print(f"Статус Artifact - {Fore.YELLOW + a[2]}")
    else:
        print(f"Статус Artifact - {Fore.RED + a[2]}")

    # /Artifact_STATUS

    # /Dota2_STATUS

    f = (response.get('services')[33])  # Dota2_status
    if 'Normal' in f:
        print(f"Статус Dota 2 - {Fore.GREEN + f[2]}")
    elif 'Critical' in f:
        print(f"Статус Dota 2 - {Fore.YELLOW + f[2]}")
    else:
        print(f"Статус Dota 2 - {Fore.RED + f[2]}")

    # /Dota2_STATUS

    # Team Fortress 2_STATUS

    k = (response.get('services')[55])  # Team Fortress2_status
    if 'Normal' in k:
        print(f"Статус Team Fortress 2 - {Fore.GREEN + k[2]}")
    elif 'Critical' in k:
        print(f"Статус Team Fortress 2 - {Fore.YELLOW + k[2]}")
    else:
        print(f"Статус Team Fortress 2 - {Fore.RED + k[2]}")

    # /Team Fortress 2_STATUS

    # Underlords_STATUS

    l = (response.get('services')[57])  # Underlords_status
    if 'Normal' in l:
        print(f"Статус Underlords - {Fore.GREEN + l[2]}")
    elif 'Critical' in l:
        print(f"Статус Underlords - {Fore.YELLOW + l[2]}")
    else:
        print(f"Статус Underlords - {Fore.RED + l[2]}")
    # /Underlords_STATUS

    # response.keys() - dict_keys(['time', 'online', 'services', 'graph', 'psa']) 1 - artifact


def main():
    url_steam = "https://crowbar.steamstat.us/gravity.json"
    get_status_steam(url_steam)
    print()
    k = input("Press close to exit\n")


if __name__ == '__main__':
    main()
