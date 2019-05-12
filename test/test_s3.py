# coding:utf-8

import boto3
import numpy as np
import cv2
import logging

# nparr = np.fromstring(img_str, np.uint8)
# img2 = cv2.imdecode(nparr, cv2.CV_32FC4)
#
# save_filename = 'test.png'
# cv2.imwrite(save_filename, img2)
#
# bucketName = "dap-final-project-vince"
bucketName = 'lehuitest'
# Key = save_filename
# outputName = save_filename + "_uploaded2"

s3 = boto3.client('s3')
save_filename = '1.png'
key = save_filename
outputName = save_filename + '_upload1'
try:
    s3.upload_file(key,bucketName,outputName)
    print("image uploaded to S3 successfully")
    # return outputName
except ClientError as e:
    print(ClientError)
    logging.error(e)
