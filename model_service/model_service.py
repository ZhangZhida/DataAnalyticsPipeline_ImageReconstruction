import json
import numpy as np
import cv2
import tornado.gen
import urllib.request
import boto3
import os
import logging

def saveimage(url,savepath = './001.jpeg'):
    urllib.request.urlretrieve(url, savepath)
    return

def construct_image_url(bucketName, outputName):
    return "https://s3.amazonaws.com/{bucketName}/{outputName}".format(
        bucketName=bucketName, outputName=outputName)

@tornado.gen.coroutine
def predict(image_url,mask_url):

    # first we need to download it
    image_name = image_url.split("/")[-1]
    image_path = "./kafka/image/"
    saveimage(image_url,image_path + image_name)

    mask_name = mask_url.split("/")[-1]
    mask_path = "./kafka/mask/"
    saveimage(mask_url,mask_path + mask_name)
    # then use script to get the result.jpg
    os.system("python script.py {} {}".format(image_path + image_name, mask_path + mask_name))

    # then upload the result.jpg
    save_filename = 'result.jpg'
    bucketName = "lehuitest"
    Key = save_filename  # filename on local computer
    outputName = save_filename  # filename on S3
    s3 = boto3.client('s3')
    try:
        s3.upload_file(Key, bucketName, outputName)
        print("image uploaded to S3 successfully")
        result_url = construct_image_url(bucketName, outputName)
        return result_url
    except ClientError as e:
        logging.error(e)
        return None

