class connection_Details:
    serverName = "localhost:3306"
    user = "root"
    dbPassword = "root"
    databaseName = "accounts"
  
    def displayConnectionDetails(self):  
       print ("serverName : ", connection_Details.serverName, " user: ", connection_Details.user, " dbPassword:", connection_Details.dbPassword , " databaseName:" , connection_Details.databaseName)  
