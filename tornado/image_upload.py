import boto3
import numpy as np
import cv2
import logging


def image_upload(img_str):

    nparr = np.fromstring(img_str, np.uint8)
    img2 = cv2.imdecode(nparr, cv2.CV_32FC4)
    save_filename = 'test.png'
    cv2.imwrite(save_filename, img2)

    bucketName = "dap-final-project-vince"
    Key = save_filename
    outputName = save_filename + "_uploaded2"

    s3 = boto3.client('s3')
    try:
        s3.upload_file(Key,bucketName,outputName)
        print("image uploaded to S3 successfully")
        return outputName
    except ClientError as e:
        logging.error(e)
        return None
    
    

        

    

    