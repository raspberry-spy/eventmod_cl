import traceback
import time
from yggdrasil import authenticate
import random
import subprocess
import tkinter as tk
from tkinter import filedialog
import keyboard
import os
import requests

root = tk.Tk()
root.withdraw()

clear = lambda: os.system('cls')

print("Проверка обновлений и целостности файлов")
subprocess.call('.\\git\\bin\\git.exe checkout -- .')
subprocess.call('.\\git\\bin\\git.exe clean -fd')
subprocess.call('.\\git\\bin\\git.exe pull')

def menu():
    clear()
    print('')
    print('             Добро пожаловать сука')
    print('')
    print('+----------------------------------------------+')
    print('|       Нажмите [ENTER] для запуска игры       |')
    print('|          Нажмите [S] для смены скина         |')
    print('+----------------------------------------------+')
    key = keyboard.read_key()
    if key == 'enter':
        clear()
        print("Проверка обновлений и целостности файлов")
        subprocess.call('.\\git\\bin\\git.exe checkout -- .')
        subprocess.call('.\\git\\bin\\git.exe clean -fd')
        subprocess.call('.\\git\\bin\\git.exe pull')
        print("Запуск игры...")
        subprocess.call(f'''.\\java\\bin\\java.exe "-javaagent:authlib-injector-1.2.3.jar=https://crossmine.ddns.net/" "-XX:HeapDumpPath=MojangTricksIntelDriversForPerformance_javaw.exe_minecraft.exe.heapdump" "-Dos.name=Windows 10" "-Dos.version=10.0" -Djava.library.path=".\\versions\\1.19.2\\natives" -Dminecraft.launcher.brand=EMCLauncher -Dminecraft.launcher.version=1.0 -cp ".\\libraries\\cpw\\mods\\securejarhandler\\2.1.4\\securejarhandler-2.1.4.jar";".\\libraries\\org\\ow2\\asm\\asm\\9.3\\asm-9.3.jar";".\\libraries\\org\\ow2\\asm\\asm-commons\\9.3\\asm-commons-9.3.jar";".\\libraries\\org\\ow2\\asm\\asm-tree\\9.3\\asm-tree-9.3.jar";".\\libraries\\org\\ow2\\asm\\asm-util\\9.3\\asm-util-9.3.jar";".\\libraries\\org\\ow2\\asm\\asm-analysis\\9.3\\asm-analysis-9.3.jar";".\\libraries\\net\\minecraftforge\\accesstransformers\\8.0.4\\accesstransformers-8.0.4.jar";".\\libraries\\org\\antlr\\antlr4-runtime\\4.9.1\\antlr4-runtime-4.9.1.jar";".\\libraries\\net\\minecraftforge\\eventbus\\6.0.3\\eventbus-6.0.3.jar";".\\libraries\\net\\minecraftforge\\forgespi\\6.0.0\\forgespi-6.0.0.jar";".\\libraries\\net\\minecraftforge\\coremods\\5.0.1\\coremods-5.0.1.jar";".\\libraries\\cpw\\mods\\modlauncher\\10.0.8\\modlauncher-10.0.8.jar";".\\libraries\\net\\minecraftforge\\unsafe\\0.2.0\\unsafe-0.2.0.jar";".\\libraries\\com\\electronwill\\night-config\\core\\3.6.4\\core-3.6.4.jar";".\\libraries\\com\\electronwill\\night-config\\toml\\3.6.4\\toml-3.6.4.jar";".\\libraries\\org\\apache\\maven\\maven-artifact\\3.8.5\\maven-artifact-3.8.5.jar";".\\libraries\\net\\jodah\\typetools\\0.8.3\\typetools-0.8.3.jar";".\\libraries\\net\\minecrell\\terminalconsoleappender\\1.2.0\\terminalconsoleappender-1.2.0.jar";".\\libraries\\org\\jline\\jline-reader\\3.12.1\\jline-reader-3.12.1.jar";".\\libraries\\org\\jline\\jline-terminal\\3.12.1\\jline-terminal-3.12.1.jar";".\\libraries\\org\\spongepowered\\mixin\\0.8.5\\mixin-0.8.5.jar";".\\libraries\\org\\openjdk\\nashorn\\nashorn-core\\15.3\\nashorn-core-15.3.jar";".\\libraries\\net\\minecraftforge\\JarJarSelector\\0.3.16\\JarJarSelector-0.3.16.jar";".\\libraries\\net\\minecraftforge\\JarJarMetadata\\0.3.16\\JarJarMetadata-0.3.16.jar";".\\libraries\\cpw\\mods\\bootstraplauncher\\1.1.2\\bootstraplauncher-1.1.2.jar";".\\libraries\\net\\minecraftforge\\JarJarFileSystems\\0.3.16\\JarJarFileSystems-0.3.16.jar";".\\libraries\\net\\minecraftforge\\fmlloader\\1.19.2-43.2.0\\fmlloader-1.19.2-43.2.0.jar";".\\libraries\\com\\mojang\\logging\\1.0.0\\logging-1.0.0.jar";".\\libraries\\com\\mojang\\blocklist\\1.0.10\\blocklist-1.0.10.jar";".\\libraries\\com\\mojang\\patchy\\2.2.10\\patchy-2.2.10.jar";".\\libraries\\com\\github\\oshi\\oshi-core\\5.8.5\\oshi-core-5.8.5.jar";".\\libraries\\net\\java\\dev\\jna\\jna\\5.10.0\\jna-5.10.0.jar";".\\libraries\\net\\java\\dev\\jna\\jna-platform\\5.10.0\\jna-platform-5.10.0.jar";".\\libraries\\org\\slf4j\\slf4j-api\\1.8.0-beta4\\slf4j-api-1.8.0-beta4.jar";".\\libraries\\org\\apache\\logging\\log4j\\log4j-slf4j18-impl\\2.17.0\\log4j-slf4j18-impl-2.17.0.jar";".\\libraries\\com\\ibm\\icu\\icu4j\\70.1\\icu4j-70.1.jar";".\\libraries\\com\\mojang\\javabridge\\1.2.24\\javabridge-1.2.24.jar";".\\libraries\\net\\sf\\jopt-simple\\jopt-simple\\5.0.4\\jopt-simple-5.0.4.jar";".\\libraries\\io\\netty\\netty-common\\4.1.77.Final\\netty-common-4.1.77.Final.jar";".\\libraries\\io\\netty\\netty-buffer\\4.1.77.Final\\netty-buffer-4.1.77.Final.jar";".\\libraries\\io\\netty\\netty-codec\\4.1.77.Final\\netty-codec-4.1.77.Final.jar";".\\libraries\\io\\netty\\netty-handler\\4.1.77.Final\\netty-handler-4.1.77.Final.jar";".\\libraries\\io\\netty\\netty-resolver\\4.1.77.Final\\netty-resolver-4.1.77.Final.jar";".\\libraries\\io\\netty\\netty-transport\\4.1.77.Final\\netty-transport-4.1.77.Final.jar";".\\libraries\\io\\netty\\netty-transport-native-unix-common\\4.1.77.Final\\netty-transport-native-unix-common-4.1.77.Final.jar";".\\libraries\\io\\netty\\netty-transport-classes-epoll\\4.1.77.Final\\netty-transport-classes-epoll-4.1.77.Final.jar";".\\libraries\\com\\google\\guava\\failureaccess\\1.0.1\\failureaccess-1.0.1.jar";".\\libraries\\com\\google\\guava\\guava\\31.0.1-jre\\guava-31.0.1-jre.jar";".\\libraries\\org\\apache\\commons\\commons-lang3\\3.12.0\\commons-lang3-3.12.0.jar";".\\libraries\\commons-io\\commons-io\\2.11.0\\commons-io-2.11.0.jar";".\\libraries\\commons-codec\\commons-codec\\1.15\\commons-codec-1.15.jar";".\\libraries\\com\\mojang\\brigadier\\1.0.18\\brigadier-1.0.18.jar";".\\libraries\\com\\mojang\\datafixerupper\\5.0.28\\datafixerupper-5.0.28.jar";".\\libraries\\com\\google\\code\\gson\\gson\\2.8.9\\gson-2.8.9.jar";".\\libraries\\com\\mojang\\authlib\\3.11.49\\authlib-3.11.49.jar";".\\libraries\\org\\apache\\commons\\commons-compress\\1.21\\commons-compress-1.21.jar";".\\libraries\\org\\apache\\httpcomponents\\httpclient\\4.5.13\\httpclient-4.5.13.jar";".\\libraries\\commons-logging\\commons-logging\\1.2\\commons-logging-1.2.jar";".\\libraries\\org\\apache\\httpcomponents\\httpcore\\4.4.14\\httpcore-4.4.14.jar";".\\libraries\\it\\unimi\\dsi\\fastutil\\8.5.6\\fastutil-8.5.6.jar";".\\libraries\\org\\apache\\logging\\log4j\\log4j-api\\2.17.0\\log4j-api-2.17.0.jar";".\\libraries\\org\\apache\\logging\\log4j\\log4j-core\\2.17.0\\log4j-core-2.17.0.jar";".\\libraries\\org\\lwjgl\\lwjgl\\3.3.1\\lwjgl-3.3.1.jar";".\\libraries\\org\\lwjgl\\lwjgl\\3.3.1\\lwjgl-3.3.1-natives-windows.jar";".\\libraries\\org\\lwjgl\\lwjgl\\3.3.1\\lwjgl-3.3.1-natives-windows-x86.jar";".\\libraries\\org\\lwjgl\\lwjgl-jemalloc\\3.3.1\\lwjgl-jemalloc-3.3.1.jar";".\\libraries\\org\\lwjgl\\lwjgl-jemalloc\\3.3.1\\lwjgl-jemalloc-3.3.1-natives-windows.jar";".\\libraries\\org\\lwjgl\\lwjgl-jemalloc\\3.3.1\\lwjgl-jemalloc-3.3.1-natives-windows-x86.jar";".\\libraries\\org\\lwjgl\\lwjgl-openal\\3.3.1\\lwjgl-openal-3.3.1.jar";".\\libraries\\org\\lwjgl\\lwjgl-openal\\3.3.1\\lwjgl-openal-3.3.1-natives-windows.jar";".\\libraries\\org\\lwjgl\\lwjgl-openal\\3.3.1\\lwjgl-openal-3.3.1-natives-windows-x86.jar";".\\libraries\\org\\lwjgl\\lwjgl-opengl\\3.3.1\\lwjgl-opengl-3.3.1.jar";".\\libraries\\org\\lwjgl\\lwjgl-opengl\\3.3.1\\lwjgl-opengl-3.3.1-natives-windows.jar";".\\libraries\\org\\lwjgl\\lwjgl-opengl\\3.3.1\\lwjgl-opengl-3.3.1-natives-windows-x86.jar";".\\libraries\\org\\lwjgl\\lwjgl-glfw\\3.3.1\\lwjgl-glfw-3.3.1.jar";".\\libraries\\org\\lwjgl\\lwjgl-glfw\\3.3.1\\lwjgl-glfw-3.3.1-natives-windows.jar";".\\libraries\\org\\lwjgl\\lwjgl-glfw\\3.3.1\\lwjgl-glfw-3.3.1-natives-windows-x86.jar";".\\libraries\\org\\lwjgl\\lwjgl-stb\\3.3.1\\lwjgl-stb-3.3.1.jar";".\\libraries\\org\\lwjgl\\lwjgl-stb\\3.3.1\\lwjgl-stb-3.3.1-natives-windows.jar";".\\libraries\\org\\lwjgl\\lwjgl-stb\\3.3.1\\lwjgl-stb-3.3.1-natives-windows-x86.jar";".\\libraries\\org\\lwjgl\\lwjgl-tinyfd\\3.3.1\\lwjgl-tinyfd-3.3.1.jar";".\\libraries\\org\\lwjgl\\lwjgl-tinyfd\\3.3.1\\lwjgl-tinyfd-3.3.1-natives-windows.jar";".\\libraries\\org\\lwjgl\\lwjgl-tinyfd\\3.3.1\\lwjgl-tinyfd-3.3.1-natives-windows-x86.jar";".\\libraries\\com\\mojang\\text2speech\\1.16.7\\text2speech-1.16.7.jar";".\\libraries\\org\\lwjgl\\lwjgl-glfw\\3.3.1\\lwjgl-glfw-3.3.1-natives-windows-arm64.jar";".\\libraries\\org\\lwjgl\\lwjgl-jemalloc\\3.3.1\\lwjgl-jemalloc-3.3.1-natives-windows-arm64.jar";".\\libraries\\org\\lwjgl\\lwjgl-openal\\3.3.1\\lwjgl-openal-3.3.1-natives-windows-arm64.jar";".\\libraries\\org\\lwjgl\\lwjgl-opengl\\3.3.1\\lwjgl-opengl-3.3.1-natives-windows-arm64.jar";".\\libraries\\org\\lwjgl\\lwjgl-stb\\3.3.1\\lwjgl-stb-3.3.1-natives-windows-arm64.jar";".\\libraries\\org\\lwjgl\\lwjgl-tinyfd\\3.3.1\\lwjgl-tinyfd-3.3.1-natives-windows-arm64.jar";".\\libraries\\org\\lwjgl\\lwjgl\\3.3.1\\lwjgl-3.3.1-natives-windows-arm64.jar";".\\versions\\1.19.2\\1.19.2.jar" -Xmx2048m -Xms2048m -Dminecraft.applet.TargetDirectory="." -Dlog4j.configurationFile="C:\\Users\\nit\\AppData\\Roaming\\easymc-launcher\\minecraft\\assets\\objects\\bd\\client-1.12.xml" -Dfml.ignorePatchDiscrepancies=true -Dfml.ignoreInvalidMinecraftCertificates=true -XX:HeapDumpPath=MojangTricksIntelDriversForPerformance_javaw.exe_minecraft.exe.heapdump -Djava.net.preferIPv6Addresses=system -DignoreList=bootstraplauncher,securejarhandler,asm-commons,asm-util,asm-analysis,asm-tree,asm,JarJarFileSystems,client-extra,fmlcore,javafmllanguage,lowcodelanguage,mclanguage,forge-,1.19.2.jar -DmergeModules=jna-5.10.0.jar,jna-platform-5.10.0.jar -DlibraryDirectory=".\\libraries" -p .\\libraries/cpw/mods/bootstraplauncher/1.1.2/bootstraplauncher-1.1.2.jar;.\\libraries/cpw/mods/securejarhandler/2.1.4/securejarhandler-2.1.4.jar;.\\libraries/org/ow2/asm/asm-commons/9.3/asm-commons-9.3.jar;.\\libraries/org/ow2/asm/asm-util/9.3/asm-util-9.3.jar;.\\libraries/org/ow2/asm/asm-analysis/9.3/asm-analysis-9.3.jar;.\\libraries/org/ow2/asm/asm-tree/9.3/asm-tree-9.3.jar;.\\libraries/org/ow2/asm/asm/9.3/asm-9.3.jar;.\\libraries/net/minecraftforge/JarJarFileSystems/0.3.16/JarJarFileSystems-0.3.16.jar --add-modules ALL-MODULE-PATH --add-opens java.base/java.util.jar=cpw.mods.securejarhandler --add-opens java.base/java.lang.invoke=cpw.mods.securejarhandler --add-exports java.base/sun.security.util=cpw.mods.securejarhandler --add-exports jdk.naming.dns/com.sun.jndi.dns=java.naming cpw.mods.bootstraplauncher.BootstrapLauncher --username {nickname} --version 1.19.2 --gameDir "." --assetsDir ".\\assets" --assetIndex 1.19 --uuid {uuid} --accessToken {accessToken} --clientId {clientId} --userType mojang --versionType release "--width" 854 "--height" 480 --launchTarget forgeclient --fml.forgeVersion 43.2.0 --fml.mcVersion 1.19.2 --fml.forgeGroup net.minecraftforge --fml.mcpVersion 20220805.130853''')
    elif key == "s":
        clear()
        time.sleep(2)
        print('[S]: Женский вариант скина')
        print('[D]: Мужской вариант скина')
        print('Любая другая клавиша: отмена смены скина')
        key = keyboard.read_key()
        if key == "s":
            skinvar = 'slim'
        elif key == "d":
            skinvar = 'default'
        else:
            menu()
        url = "https://crossmine.ddns.net/minecraftservices/minecraft/profile/skins"
        skinpath = filedialog.askopenfilename(defaultextension="png", filetypes=[("Skin image", ".png")])
        files = {'file': open(skinpath, 'rb')}
        headers = {
            'authorization': f"Bearer {accessToken}"
        }
        data = {
            'variant': skinvar
        }
        requests.request("POST", url, files=files, headers=headers, data=data, verify=False)
        menu()
    else:
        menu()

randomClientToken = random.randint(10000, 99999)
try:
    clear()
    login = input('Логин: ')
    passw = input('Пароль: ')
    mc = authenticate(login, passw, 'Minecraft', randomClientToken, False,
                      authServer='https://crossmine.ddns.net:443/authserver')
except:
    print(traceback.format_exc())
    print('Вы ввели неправильные данные, не прошли регистрацию или серверу аутентификации пришла пизда')
else:
    accessToken = mc['accessToken']
    clientId = randomClientToken
    uuid = mc['selectedProfile']['id']
    nickname = mc['selectedProfile']['name']

    menu()



time.sleep(5)
