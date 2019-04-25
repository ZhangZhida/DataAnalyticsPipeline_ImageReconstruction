import requests
import base64
import cv2
import json
if __name__ == "__main__":
    # req = requests.request('GET', 'http://127.0.0.1:7777/upload')
    # image_read = open('/home/zhida/Pictures/1__NQN6_YnxS29m8vFzWYlEg.png','rb').read()
    # image_64_encode = base64.encodestring(image_read)

    """
    Convert image to string, using opencv 
    """
    # image = cv2.imread('/Users/raleighliu/Desktop/4995_009 DA Pipeline/homework/project/Homework4995.009DAP/test_image.jpg')
    imagefile = '/Users/raleighliu/Desktop/4995_009 DA Pipeline/homework/project/Homework4995.009DAP/test_image.jpg'
    # image = cv2.imread(imagefile)
    # print(type(image))
    with open(imagefile,'rb') as f:
        image_str = f.read()
    # image_str = cv2.imencode('.jpg',image)[1].tostring()
    print(type(image_str))
    image_str = image_str.decode("utf-8")

    maskfile = '/Users/raleighliu/Desktop/4995_009 DA Pipeline/homework/project/Homework4995.009DAP/test_mask.jpg'
    mask = cv2.imread('/Users/raleighliu/Desktop/4995_009 DA Pipeline/homework/project/Homework4995.009DAP/test_mask.jpg')
    mask_str = cv2.imencode(".jpg",mask)[1].tostring()
    mask_str = mask_str.decode("utf-8")


    data = {"image":image_str,"mask":mask_str}
    print(data)

    data = json.dumps(data)
    """
    Send request
    """
    url = 'http://127.0.0.1:7777/upload'
    headers = {"content-type": "application/json"}
    r = requests.post(url, data=data)
    print(r.content)