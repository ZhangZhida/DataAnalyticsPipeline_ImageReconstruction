import requests
import base64
import cv2

if __name__ == "__main__":
    # req = requests.request('GET', 'http://127.0.0.1:7777/upload')
    # image_read = open('/home/zhida/Pictures/1__NQN6_YnxS29m8vFzWYlEg.png','rb').read()
    # image_64_encode = base64.encodestring(image_read)

    """
    Convert image to string, using opencv 
    """
    image = cv2.imread('/home/zhida/Pictures/1__NQN6_YnxS29m8vFzWYlEg.png')
    img_str = cv2.imencode('.png', image)[1].tostring()
    

    """
    Send request
    """
    url = 'http://127.0.0.1:7777/upload'
    r = requests.post(url, data=img_str)
    print(r.content)