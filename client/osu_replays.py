import glob
import hashlib
import json
import os
import shutil
import time
from os import path
import subprocess

username = ""
anotherUsername = ""

def getHashes():
    '''get my latest < beatmaps' hashes, save to usernameHashes.json'''

    #json part
    with open(username + 'Hashes.json', 'r') as file:
        properties = json.load(file)

    latest = properties[0]["latest"]

    jsonList = [
        {
        "latest": time.time()
        }, dict()
    ]

    hashDict = {}
    hashDict = properties[1]
    hashKeys = list(hashDict.keys())

    print("json loaded")

    #delete deleted map's hashes
    for i in hashKeys:
        if not os.path.exists("..\\Songs\\" + hashDict[i]):
            hashDict.pop(i)

    #add osu hashes
    for i in glob.iglob('..\\Songs\\*'):
        #*i = directory
        #select directory

        if os.path.isdir(i):
            for j in glob.iglob(glob.escape(i) + "\\*.osu"):    #glob.escape() neutralizes all wildcard letters
                #*j = file
                #select file

                if os.stat(j).st_mtime >= latest or os.stat(j).st_ctime >= latest:
                    for k in list(hashDict.keys()):
                        if j.split("\\")[-2] + "\\" + j.split("\\")[-1] == hashDict[k]:
                            hashDict.pop(k)
                    #something hash
                    m = hashlib.md5()
                    #read file

                    with open(j, 'rb') as f:
                        #hash https://blog.naver.com/ksg97031/221124560981
                        for b in iter(lambda: f.read(65536), b''):
                            m.update(b)

                    #update
                    hashDict.update({m.hexdigest(): path.basename(i) + "\\" + path.basename(j)})

    print("data loaded")


    #json part
    jsonList[1] = hashDict

    with open(username + 'Hashes.json', 'w') as f:
        json.dump(jsonList, f, indent=4)

    print("data saved")

def getReplays():
    '''get my latest < replays, save to property.json'''
    #? if i wrote with hashes...?

    #json part
    with open('property.json', 'r') as file:
        properties = json.load(file)
    
    latest = properties[0]["latest"]
    replaysToUP = []
    
    jsonList = [
        {
        "latest": properties[0]["latest"]
        }, []
    ]
    
    print("json loaded")
    
    
    #add osr files
    for i in glob.iglob('..\\Data\\r\\*.osr'):
        if os.stat(i).st_mtime >= latest:
            replaysToUP.append(path.basename(i))
    
    print("data loaded")
    
    
    #json part
    jsonList[1] = replaysToUP
    
    with open('property.json', 'w') as f:
        json.dump(jsonList, f, indent=4)
    
    print("data saved")

def openReplays():
    '''open replays, if you don't have map, replays will be moved to failed'''

    #json part
    with open(username + 'Hashes.json', 'r') as file:
        properties = json.load(file)

    hashDict = properties[1]

    print("json loaded")


    #main
    #load osr files
    time1 = time.time()

    while time1 + 15 > time.time():
        pass

    for i in glob.iglob('*.osr'):
        if hashDict.get(i[:32]) == None:
            shutil.copy(i, "failed")
        else:
            subprocess.run(['explorer.exe', i])
        print(i)
    
    time1 = time.time()

    while time1 + 120 > time.time():
        pass

    for i in glob.iglob('*.osr'):
        os.remove(i)

def searchHashes(searchPath = ""):
    '''search (failed map's)hashes, save in mapList.json.'''

    #json part
    with open(anotherUsername + 'Hashes.json', 'r') as file:
        properties = json.load(file)

    hashDict = properties[1]

    mapList = dict()

    print("json loaded")


    #search part
    alreadyBeing = []

    for i in [x for x in glob.iglob(searchPath + "*") if path.isdir(x)]:
        alreadyBeing.append(path.basename(i))

    for i in glob.iglob(searchPath + '*.osr'):
        if hashDict.get(path.basename(i)[:32]) == None or hashDict.get(path.basename(i)[:32]).split('\\')[0] not in alreadyBeing:
            mapList.update({path.basename(i)[:32]: hashDict.get(path.basename(i)[:32])})

    print("data loaded")


    #json part
    with open(searchPath + 'mapList.json', 'w') as f:
        json.dump(mapList, f, indent=4)

    print("data saved")