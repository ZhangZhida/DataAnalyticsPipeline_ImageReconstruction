from consumer_client import ConsumerClient
from db_client import MysqlClient
import json

if __name__ == "__main__":
    c = ConsumerClient()
    mysql = MysqlClient()
    
    while True:
        msg = c.consume_message()
        
        # decode message and convert it to json object
        msg = msg.decode('utf-8')
        msg = json.loads(msg)

        user_id = msg['user_id']
        image_url = msg['image_url']

        print("user_id = ", user_id)
        print("image_url = ", image_url)

        # insert image to database
        if image_url is not None:
            mysql.insert_image(user_id=user_id, image_url=image_url)
        
        mysql.get_upload_history()

        
    
    