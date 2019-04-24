from db_client import MysqlClient

def test_select(mysql_client):
    print('========== test mysql get_upload_history() ===========')
    print(mysql_client.get_upload_history())

def test_insert(mysql_client):
    fake_user_id = 'fake_user_id'
    fake_image_url = 'www.fakeimageurl.com'
    print('========== test mysql insert_image() ===========')
    print(mysql_client.insert_image(fake_user_id, fake_image_url))

if __name__ == "__main__":
    mysql_client = MysqlClient()
    test_select(mysql_client)
    test_insert(mysql_client)
    
