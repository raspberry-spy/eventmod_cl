import requests, json, subprocess, os, json
from tkinter import filedialog

url = 'http://crossmine.ddns.net/'


def run(user):
    accessToken = user[0]
    uuid = user[1]
    nickname = user[2]
    print("Проверка обновлений и целостности файлов")
    subprocess.run('.\\git\\bin\\git.exe checkout -- .')
    subprocess.run('.\\git\\bin\\git.exe clean -fd')
    subprocess.run('.\\git\\bin\\git.exe pull --ff-only')
    print("Запуск игры...")
    with open('.\\win_args.txt', 'r') as file:
        data = file.read().replace('\n', '')
    subprocess.run(
        fr'''.\java\bin\java.exe {data} --username {nickname} --uuid {uuid} --accessToken {accessToken} -javaagent:authlib-injector-1.2.3.jar=http://crossmine.ddns.net/ --server crossmine.ddns.net --port 25585''')


def auth():
    login = input('Введите логин: ') + "@alt.me"
    passw = input('Введите пароль: ')
    mc = json.loads(
        requests.post(url + 'authserver' + '/authenticate', data=json.dumps(
            {"agent": {"name": 'Minecraft', "version": 1}, "username": login, "password": passw,
             "requestUser": False}), headers={'Content-Type': 'application/json'},
                      verify=False).text)
    accessToken = mc['accessToken']
    uuid = mc['selectedProfile']['id']
    nickname = mc['selectedProfile']['name']
    with open('pas.json', "w") as fw:
        pas = {
            "accessToken": accessToken,
            "uuid": uuid,
            "nickname": nickname
        }
        fw.write(json.dumps(pas))
    return accessToken, uuid, nickname


if os.path.exists('pas.json'):
    with open('pas.json', "r") as fr:
        pas = json.load(fr)
    val = requests.post(url + 'authserver' + '/validate', data=json.dumps(
        {'accessToken': pas['accessToken']}), headers={'Content-Type': 'application/json'},
                        verify=False)
    if val.status_code == 403:
        print('Ошибка входа, запрос обновления сессии')
        ref = requests.post(url + 'authserver' + '/refresh', data=json.dumps(
            {'accessToken': pas['accessToken']}), headers={'Content-Type': 'application/json'},
                            verify=False)
        if ref.status_code == 403:
            print(
                'Старая сессия не найдена в базе данных\nНеобходим повторный вход')
            user = auth()
        else:
            refj = json.loads(ref.text)
            pas = {
                "accessToken": refj['accessToken'],
                "uuid": pas['uuid'],
                "nickname": pas['nickname']
            }
            with open('pas.json', "w") as fw:
                fw.write(json.dumps(pas))
            user = [pas['accessToken'], pas['uuid'], pas['nickname']]
    else:
        user = [pas['accessToken'], pas['uuid'], pas['nickname']]
else:
    user = auth()
print('Вход выполнен')

print(
    'Список команд:\n\nstart: запуск игры (также для запуска вы можете просто нажать enter не вводя команд)\nskin: установить скин\nskinslim: установить скин с тонкими руками\nhigh: установить высокую графику\nmedium: установить среднюю графику\nlow: установить низкую графику\n1488: 卍')

while True:
    comm = input('=> ')
    if comm == '' or comm == 'play':
        break
    elif comm == 'skin':
        skinpath = filedialog.askopenfilename(defaultextension="png", filetypes=[("Skin image", ".png")])
        requests.request("PUT", f"http://crossmine.ddns.net/api/user/profile/{user[1]}/skin", headers={'authorization': f"Bearer {user[0]}"}, files={'file': open(skinpath, 'rb')}, data={'model':''}, verify=False)
    elif comm == 'skinslim':
        skinpath = filedialog.askopenfilename(defaultextension="png", filetypes=[("Skin image", ".png")])
        requests.request("PUT", f"http://crossmine.ddns.net/api/user/profile/{user[1]}/skin", headers={'authorization': f"Bearer {user[0]}"}, files={'file': open(skinpath, 'rb')}, data={'model':'slim'}, verify=False)
    elif comm == '1488':
        print('''⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⢈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⡿⠋⠈⠻⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡋⠀⠀⠀⠀⠀⠰⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣷⣀⠀⠀⠀⠀⠈⠻⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿
⣿⡿⠋⠘⠻⣿⣿⣿⣿⣦⡄⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣶⣀⠀⠀⠀⠀⠈⠻⣿
⡋⠀⠀⠀⠀⠉⠿⣿⣿⣿⣿⡧⠀⠀⠀⠀⠀⠀⠰⣿⣿⣿⣿⣶⣀⠀⠀⠀⠀⢈
⣿⣦⣀⠀⠀⠀⠀⠉⠻⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣶⣄⢀⣴⣿
⣿⣿⣿⣶⡀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣧⡄⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⡶⠀⠀⠀⠀⠀⢈⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣶⡀⢀⣴⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡋⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿''')
    elif comm == 'high':
        subprocess.run('.\\git\\bin\\git.exe checkout -- .')
        subprocess.run('.\\git\\bin\\git.exe clean -fd')
        subprocess.run('.\\git\\bin\\git.exe pull --ff-only')
        subprocess.run('.\\git\\bin\\git.exe checkout main')
    elif comm == 'medium':
        subprocess.run('.\\git\\bin\\git.exe checkout -- .')
        subprocess.run('.\\git\\bin\\git.exe clean -fd')
        subprocess.run('.\\git\\bin\\git.exe pull --ff-only')
        subprocess.run('.\\git\\bin\\git.exe checkout mid')
    elif comm == 'low':
        subprocess.run('.\\git\\bin\\git.exe checkout -- .')
        subprocess.run('.\\git\\bin\\git.exe clean -fd')
        subprocess.run('.\\git\\bin\\git.exe pull --ff-only')
        subprocess.run('.\\git\\bin\\git.exe checkout lite')
run(user)
