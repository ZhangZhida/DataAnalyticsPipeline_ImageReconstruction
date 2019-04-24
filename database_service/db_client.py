import MySQLdb
import datetime
import time
import configparser


class MysqlClient:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read("../config.ini")
        host = config['MYSQL']['HOST']
        user = config['MYSQL']['USER']
        passwd = config['MYSQL']['PASSWD']
        db = config['MYSQL']['DB']
        print('host = ', host)
        print('user = ', user)
        print('passwd = ', "***")
        print('db = ', db)
        

        self.connection = MySQLdb.connect(
            host=host,
            user=user,
            passwd=passwd,
            db=db
        )
        self.connection.cursor().execute('use ' + db)

    def get_upload_history(self):
        cursor = self.connection.cursor()
        table_name = "image_upload"
        result = cursor.execute("""select * from {table}""".format(table=table_name))
        print(result)
        return result

    def insert_image(self, user_id, image_url):
        cursor = self.connection.cursor()
        
        upload_time = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
        table_name = "image_upload"
        sql = """insert into image_upload 
                                (user_id, image_url, upload_time)
                                values 
                                (%s, %s, %s)"""
        val = (user_id, image_url, upload_time)
        # print("sql = ", sql)
        result = cursor.execute(sql, val)
        self.connection.commit()
        
        print("insert result = ", result)

