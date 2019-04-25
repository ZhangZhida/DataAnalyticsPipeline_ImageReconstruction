from consumer_client_predict import ConsumerClient
import json
import numpy as np
import cv2
import tornado.gen
import urllib.request
import boto3
# def saveimage(url,savepath = './001.jpeg'):
#     urllib.request.urlretrieve(url, savepath)
#     return

def construct_image_url(bucketName, outputName):
    return "https://s3.amazonaws.com/{bucketName}/{outputName}".format(
        bucketName=bucketName, outputName=outputName)

@tornado.gen.coroutine
def predict(image_url,mask_url):

    # first we need to download it

    # then use script to get the result.jpg
    # then upload the result.jpg
    return result_url
