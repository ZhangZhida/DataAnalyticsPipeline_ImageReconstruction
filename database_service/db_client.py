import MySQLdb
import datetime
import time

class MysqlClient:
    def __init__(self):
        self.connection = MySQLdb.connect(
            host="image-reconstruct.cbd1ayvksyji.us-east-1.rds.amazonaws.com",
            user="root",
            passwd="Zd822511",
            db="image_reconstruct"
        )
        self.connection.cursor().execute('use image_reconstruct')

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

