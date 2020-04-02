import time
import os
import json
import glob
import shutil
from os import path

username = ""
anotherUsername = ""

def checker():
    '''with property.json, send user's missing replay files'''
    if username == "firo":
        driv = "N:\\"
    else:
        driv = "O:\\"

    #json part
    with open(driv + 'osu!_Replays\\property.json', 'r') as file:
        properties = json.load(file)
        print("read json")

    latest = properties[0]["latest"]
    aleadyRepl = properties[1]

    jsonList = [
        {
        "latest": latest   #time = latest 'copied file''s date
        }, []
    ]

    print("json loaded")


    #main
    replToUP = []
    newLatest = latest

    for i in glob.iglob('D:\\Games\\osu!_Replays\\r\\*.osr'):
        itime = os.stat(i).st_mtime

        if itime >= latest and path.basename(i) not in aleadyRepl:
            replToUP.append(i)
            if newLatest < itime: newLatest = itime

    jsonList[0]["latest"] = newLatest

    print("data loaded")

    for i in replToUP:
        shutil.copy(i, driv + 'osu!_Replays')

    print("data copied")


    #json part
    with open(driv + 'osu!_Replays\\property.json', 'w') as f:
        json.dump(jsonList, f, indent=4)

    print("data saved")

def saveHash():
    '''save user's hash.json to server'''
    if username == "firo":
        driv = "N:\\"
    else:
        driv = "O:\\"

    shutil.copy(driv + 'osu!_Replays\\' + username +'Hashes.json', '.\\')

def sendHash():
    '''get another user's hash.json'''
    if username == "firo":
        driv = "N:\\"
    else:
        driv = "O:\\"

    shutil.copy(anotherUsername + 'Hashes.json', driv + 'osu!_Replays')

def sendMapList():
    '''send user's failed mapList.json, if there is folder which is not in mapList.json, remove it'''
    if username == "firo":
        driv = "N:\\"
    else:
        driv = "O:\\"
    
    #main
    time1 = time.time()
    shutil.copy(driv + 'osu!_Replays\\failed\\maplist.json', 'D:\\Games\\osu!_Replays\\' + username + 'MissingMaps\\')

    while time1 + 5 > time.time():
        pass

    #json part
    with open('D:\\Games\\osu!_Replays\\' + username + 'MissingMaps\\mapList.json', 'r') as file:
        hashDict = json.load(file)

    mapListValues = []

    #main2
    for i in hashDict.values():
        if i != None:
            mapListValues.append(i.split("\\")[0])

    for i in glob.iglob('D:\\Games\\osu!_Replays\\' + username + 'MissingMaps\\*'):
        if os.path.isdir(i) and path.basename(i) not in mapListValues:  #if not in mapList.json
            shutil.rmtree(i)
    
def sendMissingMaps():
    '''send anoteher user's missing maps'''
    if username == "firo":
        driv = "N:\\"
    else:
        driv = "O:\\"

    #json part
    with open('D:\\Games\\osu!_Replays\\' + anotherUsername + 'MissingMaps\\mapList.json', 'r') as file:
        hashDict = json.load(file)

    mapFolderName = set()  #missing maps list

    for i in hashDict.values():
        if i != None:
            mapFolderName.add(i.split("\\")[0])

    #main
    for i in glob.iglob('D:\\Games\\osu!_Replays\\' + anotherUsername + 'MissingMaps\\*'):
        if os.path.isdir(i) and path.basename(i) in mapFolderName:
            mapFolderName.discard(path.basename(i))

    for i in mapFolderName:
        shutil.copytree(driv + 'Songs\\' + i, 'D:\\Games\\osu!_Replays\\' + anotherUsername + 'MissingMaps\\' + i) 

def getMissingMaps():
    '''get user's missing maps'''
    if username == "firo":
        driv = "N:\\"
    else:
        driv = "O:\\"

    #main
    alreadyBeing = []

    for i in [x for x in glob.iglob(driv + 'osu!_Replays\\failed\\*') if path.isdir(x)]:
        alreadyBeing.append(path.basename(i))

    for i in glob.iglob('D:\\Games\\osu!_Replays\\' + username + 'MissingMaps\\*'):
        if os.path.isdir(i):
            if path.basename(i) not in alreadyBeing:
                shutil.copytree(i, driv + 'osu!_Replays\\failed\\' + path.basename(i))
            else:
                shutil.rmtree(i)