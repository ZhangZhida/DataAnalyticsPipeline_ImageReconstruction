import boto3
import numpy as np
import cv2
import logging


def image_upload(img_str):

    # decode the string to image
    nparr = np.fromstring(img_str, np.uint8)
    img2 = cv2.imdecode(nparr, cv2.CV_32FC4)
    
    # save image file to local computer
    save_filename = 'test_image.jpeg'
    cv2.imwrite(save_filename, img2)

    # upload image to S3
    bucketName = "lehuitest"
    Key = save_filename                         # filename on local computer
    outputName = save_filename   # filename on S3

    s3 = boto3.client('s3')
    try:
        s3.upload_file(Key, bucketName,outputName)
        print("image uploaded to S3 successfully")
        image_url = construct_image_url(bucketName, outputName)
        return image_url
    except ClientError as e:
        logging.error(e)
        return None
    
    
def construct_image_url(bucketName, outputName):
    return "https://s3.amazonaws.com/{bucketName}/{outputName}".format(
        bucketName=bucketName, outputName=outputName)

        

    

    