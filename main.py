                    ###                 ###
                  #        __ixteeN         #
                   #                       #
                    ### -ETHFREE SCRIPT ###




import os
import sys
import time
import asyncio
import warnings
import datetime
from time import sleep

warnings.filterwarnings('ignore')

st     = "\033[1;"
red    = f"{st}31;40m"
green  = f"{st}32;40m"
yellow = f"{st}33;40m"
blue   = f"{st}34;40m"
purple = f"{st}35;40m"
cyan   = f"{st}36;40m"
white  = f"{st}37;40m"
red    = "\033[1;31;40m"
grey   = "\033[1;30;40m"
mono   = "\033[2;37;40m"
emono  = "\033[0;37;40m"
italic = "\033[3;37;40m"
etalic = "\033[0;37;40m"
reset  = white


#                         ---
#                           ----
#   CHECK MODULES & INSTALL   -----
#                           ----
#                         ---



def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
try :
    clear()
    import bs4
except ModuleNotFoundError:
       os.system('pip install bs4')
       sleep(3)
       clear()
try :
    import requests
except ModuleNotFoundError:
       os.system('pip install requests')
       sleep(3)
       clear()
try :
    import requests_toolbelt
except ModuleNotFoundError:
       os.system('pip install requests_toolbelt -q')
       sleep(3)
       clear()


import requests
import pickle
import json
import sys
import re
import datetime
import base64
import random
import string

from time import sleep
from bs4 import BeautifulSoup as Soup
from requests_toolbelt import MultipartEncoder
from getpass import getpass
c=requests.Session()


#                ---
#                  ----
#        DEF BOT     -----
#                  -----
#                ---



def banner(name):
    print (f"""
{cyan}▐▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀{white}▌
{cyan}▐       ::::::::{white} ▌
{cyan}▐     :+:    :+{white}: ▌
{cyan}▐    +:+      {white}   ▌
{cyan}▐   +#++:++#+{white}+   ▌
{cyan}▐         +#{white}+    ▌
{cyan}▐ #+#    #+{white}#     ▌
{cyan}▐ ########{white}       ▌
{cyan}▐       :{white}::::::: ▌
{cyan}▐     :+{white}:    :+: ▌
{cyan}▐    +:{white}+         ▌
{cyan}▐   +#{white}+          ▌ {italic}STATUS: ONLINE{etalic}
{cyan}▐  +#{white}+           ▌ {italic}SCRIPT: {name}{etalic}
{cyan}▐ #+{white}#    #+#     ▌ {italic}AUTHOR: SIXTEEN{etalic}
{cyan}▐ #{white}#######       ▌ {italic}CHANNEL: youtube.com/@sixteencrypto{etalic}
{cyan}▐{white}▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▌ {italic}CHANNEL: t.me/sixteenchannel{etalic}
""")


def timer (t):
     try:
        while t:
          mins, secs = divmod(t, 60)
          timer = '{:02d}m:{:02d}s'.format(mins, secs)
          x = datetime.datetime.now().strftime("%X")
          print (f"\r {white}{x} {italic}wait -", timer, end=f"{etalic}  \r")
          sleep(1)
          t -= 1
     except SystemExit:
           sys.exit("                     \r")
def write(text) :
    print (f"{etalic}{text}{etalic}\n")

def slow(text) :
   for word in text:
       print (word, end ="", flush=True)
       sleep(0.005)
def save_cookies(requests_cookiejar, filename):
    with open(filename, 'wb') as f:
        pickle.dump(c.cookies, f)
def load_cookies(filename):
    with open(filename, 'rb') as f:
         c.cookies.update(pickle.load(f))

def Get(x, headers):
    while True:
          try:

             if os.path.exists('config/cookie.txt'):
                req    = c.get(x, cookies=load_cookies('config/cookie.txt'), headers=headers)
                res    = Soup(req.content, 'html.parser')
                data   = res.prettify()
                cookie = c.cookies.get_dict()
                save_cookies(req.cookies, 'config/cookie.txt')
                return data, cookie
             else:
                req    = c.get(x, headers=headers)
                res    = Soup(req.content, 'html.parser')
                data   = res.prettify()
                cookie = c.cookies.get_dict()
                save_cookies(req.cookies, 'config/cookie.txt')
                return data, cookie

          except (ConnectionResetError,requests.exceptions.ConnectionError, ConnectionError,requests.exceptions.ChunkedEncodingError, requests.exceptions.ReadTimeout) as E :
                  pass


def get(x, headers):
    while True:
          try:
             write('  Visiting Site . . .   ')
             if os.path.exists('config/cookie.txt'):
                req    = c.get(x, cookies=load_cookies('config/cookie.txt'), headers=headers)
                res    = Soup(req.content, 'html.parser')
                data   = res.prettify()
                save_cookies(req.cookies, 'config/cookie.txt')
                write('  Website Visit Completed . . . ')
                return data
             else:
                req    = c.get(x, headers=headers)
                res    = Soup(req.content, 'html.parser')
                data   = res.prettify()
                save_cookies(req.cookies, 'config/cookie.txt')
                write('  Website Visit Completed . . . ')
                return data

          except (ConnectionResetError,requests.exceptions.ConnectionError, ConnectionError,requests.exceptions.ChunkedEncodingError, requests.exceptions.ReadTimeout) as E :
                write('  Error Check Your Internert Connection .')


def post(x, y, headers):
    while True:
          try:
             write('  Sending Data . . . ')
             if os.path.exists('config/cookie.txt'):
                req    = c.post(x, y, cookies=load_cookies('config/cookie.txt'), headers=headers)
                res    = Soup(req.content, 'html.parser')
                data   = res.prettify()
                save_cookies(req.cookies, 'config/cookie.txt')
                write('  Sending Data Completed . . . ')
                return data
             else:
                req    = c.post(x, y, headers=headers)
                res    = Soup(req.content, 'html.parser')
                data   = res.prettify()
                save_cookies(req.cookies, 'config/cookie.txt')
                write('  Sending Data Completed . . . ')
                return data

          except (ConnectionResetError,requests.exceptions.ConnectionError, ConnectionError,requests.exceptions.ChunkedEncodingError, requests.exceptions.ReadTimeout) as E :
                write('  Error Check Your Internert Connection .')




    ########################################### -
    ####                                        -
            #### TALK TO THEM WITHOUT VIOLENCE. -
    ####                                        -
    ####_________________________________________


def _password():
    def get(x, headers):
        while True:
          try:
             req    = c.get(x, headers=headers)
             res    = Soup(req.content, 'html.parser')
             data   = res.prettify()
             return data
             break

          except (ConnectionResetError,requests.exceptions.ConnectionError, ConnectionError,requests.exceptions.ChunkedEncodingError, requests.exceptions.ReadTimeout) as E :
               pass

    def post(x, y, headers):
        while True:
          try:
             req    = c.post(x, y, headers=headers)
             res    = Soup(req.content, 'html.parser')
             data   = res.prettify()
             return data
             break

          except (ConnectionResetError,requests.exceptions.ConnectionError, ConnectionError,requests.exceptions.ChunkedEncodingError, requests.exceptions.ReadTimeout) as E :
              pass

    def ip():
        try:
         url = "https://ipinfo.io/json"
         data= get(url, headers=[])
         ip = json.loads(data)['ip']
         return ip
        except Exception as E:
               print (f'''#################################\n   {red}ERROR WHILE FETCHING INFO{reset}\n\n{cyan}SOLUTIONS -⟩\n\n{green}1. USE OR DISABLE VPN{reset}\n{green}2. RERUN {reset}\n\n#################################''')
               sys.exit()

    def update_licence(dictionary):
        url= "https://rentry.co/licences2/edit"
        headers= {"content-type":"application/x-www-form-urlencoded",
                  "referer" : url}
        data= get(url, headers)
        token= re.search('<input name="csrfmiddlewaretoken" type="hidden" value="(\w+)',data)[1]
        payload= f'csrfmiddlewaretoken={token}&text={dictionary}&edit_code=licences&new_edit_code=&new_url='
        headers= {"content-type":"application/x-www-form-urlencoded",
                  "referer" : url,}
        data= post(url, payload, headers)

    def send_licence(text):
        url= "https://rentry.co"
        headers= {"content-type":"application/x-www-form-urlencoded",
                  "referer" : url}

        data= get(url, headers)
        token= re.search('<input name="csrfmiddlewaretoken" type="hidden" value="(\w+)',data)[1]
        payload= f'csrfmiddlewaretoken={token}&text={text}&edit_code=&new_edit_code=&new_url='
        headers= {"content-type":"application/x-www-form-urlencoded",
                  "referer" : url,}
        data= post(url, payload, headers)
        new_url = re.search('<a class="btn btn-light squared" href="(.*)" role="button">',data)[1]
        new_url = url+new_url
        gen_alias = ''.join(random.sample(string.ascii_letters + string.digits, 5))

        generate_link = json.loads(get(f"https://api.cuty.io/quick?token=91468df5b8815e94d72eca27e&url={new_url}&alias=sixteen{gen_alias}", headers=[]))
        generate_link2 = json.loads(get(f"https://exe.io/api?api=909bb8ea5285523642bc1b308677a88af41e3307&url={new_url}&alias=sixteen{gen_alias}", headers=[]))
        return generate_link["short_url"], generate_link2["shortenedUrl"]

    try:
      gen_hash = "".join(random.sample(string.ascii_letters + string.digits, 16))
      ipad = ip()
      licences = get('https://rentry.co/licences2/raw', headers=[])
      if ipad not in licences:
         licences = json.loads(licences.replace("'", '"'))
         licences[f'{ipad}'] = gen_hash
         update_licence(licences)
         quick = send_licence(gen_hash)
         while True:
               print (f"{reset}LINK [a]: {green}{quick[0]}{reset}\nLINK [b]: {purple}{quick[1]}{reset}")
               Input = input("  Enter Your Licence: ")
               if Input == gen_hash:
                  write('\n  Licence Correct Success Verification.')
                  break
               else:
                  write('\n  Licence Wrong Invalid Verification.')
                  clear()
      else:
         licence = json.loads(licences.replace("'", '"'))[ipad]
         quick = send_licence(licence)
         while True:
               print (f"{reset}LINK [a]: {green}{quick[0]}{reset}\nLINK [b]: {purple}{quick[1]}{reset}")
               Input = input("  Enter Your Licence: ")
               if Input == licence:
                  write('\n  Licence Correct Success Verification.')
                  break
               else:
                  write('\n  Licence Wrong Invalid Verification.')
                  clear()
      clear()
    except ZeroDivisionError as Error:
           print (Error)


#+++++                                   +++++#
# +++++++++                         ++++++++  #
#      ++++++ MAKE CONFIGURATION  ++++++      #
# +++++++++                         ++++++++  #
#+++++                                   +++++#


def _config():

    if not os.path.exists('config'):
       os.mkdir('config')

    try:
       pass#word()
    except KeyboardInterrupt:
           sys.exit()

    if not os.path.exists('config/data.json'):

       email = input(f"\n   EMAIL:  ")
       password = input(f"\n   PASSWORD:  ")
       user_agent = input(f"\n   USER-AGENT:  ")

       sleep(2)
       write('\n  Saving Configuration - [/config/data.json] .')
       clear()

       dict= {"user": email,
                "password": password,
                "user-agent": user_agent}
       dump= json.dumps(dict, indent=4)
       with open('config/data.json', 'w') as file:
            file.write(dump)

    _data= json.load(open('config/data.json', 'r'))
    user= _data['user']
    password= _data['password']
    useragent= _data['user-agent']
    return user, password, useragent


try:
   config_data= _config()
   user= config_data[0]
   password= config_data[1]
   useragent= config_data[2]
except KeyboardInterrupt:
       sys.exit()



#           --------------------
#      ———————————————————————————————
#              DEFINE
#                     CAPTCHA
#      ———————————————————————————————
#           --------------------


def captcha():
    def post(x, y, headers):
        while True:
          try:
             req    = c.post(x, y, headers=headers)
             res    = Soup(req.content, 'html.parser')
             data   = res.prettify()
             return data
             break

          except (ConnectionResetError,requests.exceptions.ConnectionError, ConnectionError,requests.exceptions.ChunkedEncodingError, requests.exceptions.ReadTimeout) as E :
              pass

    url= "https://iconcaptcha.one/api.php"
    payload= '{\"theme\":\"light\"}'
    data= json.loads(post (url, payload, headers={'user-agent': useragent}))
    id= data["id"]
    cap= '{"id":"'+id+'","posX":10,"posY":51}'
    captcha= base64.b64encode(cap.encode()).decode()
    write('  Tying Bypass Captcha . . . ')
    return captcha



   #   #### #### # #  #
   #   #  # #    # ## #
   #   #  # # ## # # ##
   ### #### #### # #  s



def login():
    print ('\n\n\n')
    url= "https://freeth.in/signup/?op=s"
    headers= {"user-agent": useragent}
    headers["x-csrf-token"] = "".join(random.sample(string.ascii_letters, 12))
    cookies = {'csrf_token': f'{headers["x-csrf-token"]}'}
    c.cookies.update(cookies)
    while True:
          data= get(url, headers=headers)
          payload= f"csrf_token=&op=login_new&btc_address={user}&password={password}&tfa_code="
          headers["content-type"] = "application/x-www-form-urlencoded"
          headers["x-requested-with"] = "com.cookiegames.smartcookie"
          data= post("https://freeth.in/", payload, headers)
          if 'e:Incorrect login details' in data:
            write(f'  Wrong Credentials Entered . . .')
            os.system('rm config/data.json')
            sys.exit ('  Error:Incorrect login details')

          elif 's:123:123:123:123' in data:
             write('  Login Success . . . ')
             data = get("https://freeth.in/?op=home", headers)
             return data

          else:
             print (data)


def BD(data):
    balance = re.search('''<span id="balance_small">
         (.*)
        </span>''',data)[1]
    banner("ETHFREE")
    slow (f"\n{white}🏧 BALANCE:  {green}{balance} ETH{reset} \n\n")




##### ##### #   # ##### ##### #######
#     #   # #   # #   # #        #
#     #   # #   # #     ##       #
####  ##### #   # #     ####     #
#     #   # #   # #   # #        #
#     #   # ##### ##### #####    #




def _main():
    headers= {"user-agent": useragent}
    url = "https://freeth.in/?op=home"
    data = Get("https://freeth.in/?op=home", headers)
    if "$('.free_play_time_remaining').countdown({" in data[0]:
        write (f"  Roll Completed This Hour . . . ")
        seconds = re.search("""\$\('.free_play_time_remaining'\).countdown\(\{
                        until: \+(.*),""", data[0])[1]
        minutes = int(seconds)/60
        write ("  Left minutes: "+str(minutes))
        sleep(60*5)
    token = data[1]['csrf_token']
    client_seed = re.search('<input id="next_client_seed" type="text" value="(.*)"/>',data[0])[1]
    payload = f"csrf_token={token}&op=free_play&fingerprint=64d03558eaca2570eadbadc362365989&client_seed={client_seed}&fingerprint2=2526924704&pwc=1&h_recaptcha_response="
    headers["content-type"] = "application/x-www-form-urlencoded"
    data = post ("https://freeth.in/", payload, headers)
    if 'Someone has already played from this IP in the last hour.' in data:
        minutes = re.search("You need to wait for (.*) minutes",data)[1]
        write ("  Left minutes: "+str(minutes))
        write ("  Sleeping for 5 minutes...!")
        sleep(60*5)
    elif 's:' in data:
        data= data.split(':')
        number= data[1]
        balance= data[2]
        earned= data[3]
        tokens= data[14]

        x = datetime.datetime.now().strftime("%X")
        slow (f"{cyan}{x} {white}- Lucky Number: {green}{number}{white} Won: {green}{earned} ETH{etalic}{reset} \n")
        slow (f"         - {white}Balance: {yellow}{balance} ETH{white} Tokens Left: {cyan}{tokens}{etalic}\n")
        slow (f'{cyan+ "-".center(49, "-")+reset}\n')
        write ("  Sleeping for 5 minutes...!")
        sleep(60*5)


def main():
    try:
      Data= login()
      BD(Data)
      while True:
            try:
              _main()
            except Exception as error:
                  pass
    except KeyboardInterrupt:
           write('  Exiting By CTRL+C KEYBOARD INTERRUPT .')
           sys.exit('  Execution Stopped Due To CTRL+C Command .')
    except Exception as error:
           pass



if __name__ == '__main__':
   main()










#_____________________________Finished_________________________________
#--------------------------------------------------------------------
