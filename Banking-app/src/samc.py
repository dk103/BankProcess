#!C:\Users\M1030512\AppData\Local\Programs\Python\Python36\python.exe
import hashlib, time, cgi, os
import shelve
from http import cookies
from pathlib import Path

class session(object):

    def __init__(self, expires=None, cookies_path=None):
        string_cookies = os.environ.get('HTTP_COOKIE', '')
        self.cookies = cookies.SimpleCookie()
        self.cookies.load(string_cookies)

        if self.cookies.get('sid'):
            sid = self.cookies['sid'].value
            # Clear session cookies from other cookiess
            self.cookies.clear()

        else:
             self.cookies.clear()
             hash = hashlib.sha1()
             hash.update(str(time.time()).encode('utf-8'))
             sid = hash.hexdigest()[:10]


        self.cookies['sid'] = sid

        if cookies_path:
            self.cookies['sid']['path'] = cookies_path

        home = str(Path.home())
        session_dir = home + '\\tmp\\.session'
        directory = os.path.dirname('%s\\sess_%s' % (session_dir, sid))

        try:
            os.stat(directory)
        except:
            os.mkdir(directory)
            
        self.data = shelve.open (
            '%s/sess_%s' % (session_dir, sid),flag='c',writeback=True)
       # os.chmod('%s/sess_%s' % (session_dir, sid),"0660")

        # Initializes the expires data
        if not self.data.get('cookies'):
            self.data['cookies'] = {'expires':''}

        self.set_expires(expires)

    def close(self):
        self.data.close()

    def set_expires(self, expires=None):
        if expires == '':
            self.data['cookies']['expires'] = ''
        elif isinstance(expires, int):
            self.data['cookies']['expires'] = expires

        self.cookies['sid']['expires'] = self.data['cookies']['expires']
