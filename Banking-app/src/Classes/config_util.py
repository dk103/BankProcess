from os.path import abspath, exists
import shelve ,os 
from pathlib import Path

class config_meta:
    LOG_FILENAME = 'example.log'
    Session_userName = None
    Session_userAccountId = None
    errorPage = "errorPage.html"
    
    def update_error_page_template(content):
        str=""
      
        f_path = abspath(config_meta.errorPage)
        fileObject = open(f_path, "r")
        str=fileObject.read()
        str = str.replace("{TDATA}",content )
      
        fileObject.close()
        
        fileObject = open(f_path, "w+")
        fileObject.write(str)
        fileObject.close()
        
    
    def updateAccountValue(accId):
        session_dir = abspath("util")+ '\\tmp'
        directory = os.path.dirname('%s\\sess_%s' % (session_dir, accId))

        try:
            os.stat(directory)
        except:
            os.mkdir(directory)
            
        data = shelve.open (
            '%s/sess_%s' % (session_dir, accId),flag='c',writeback=True)
        
        data['accountId'] = accId
        config_meta.Session_userAccountId = data['accountId']
        
        data.close()