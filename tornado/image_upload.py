import boto3
import numpy as np
import cv2
import logging
import base64
from PIL import Image

def get_image_from_dataurl(dataUrl, save_filename, img_type):
	# start = dataUrl.find(";base64")
	# img_str = None
	img = None
	# if start != -1:
	# 	img_str = dataUrl[start + 7:]
	# 	base64.decode(img_str, img)

	if img_type == 'jpg':
		if save_filename[-4:] != '.jpg':
			print("save_filename MUST be *.jpg!!!")
			returns
		
		tmp_png_save_filename = save_filename[:-4] + '.png'

		# first save as png file
		with open(tmp_png_save_filename, 'wb') as f:
			f.write(base64.decodestring(dataUrl.split(',')[1].encode()))

		# convert png to jpg file
		# im = Image.open(tmp_png_save_filename)
		
		png = Image.open(tmp_png_save_filename).convert('RGBA')
		background = Image.new('RGBA', png.size, (255,255,255))

		alpha_composite = Image.alpha_composite(background, png)
		alpha_composite = alpha_composite.convert("RGB")
		alpha_composite.save(save_filename, 'JPEG', quality=100)
	elif img_type == 'png':
		with open(save_filename, 'wb') as f:
			f.write(base64.decodestring(dataUrl.split(',')[1].encode()))
	else:
		print('image type has to be .jpg or .png!!!')

	# im = im.convert('RGB')
	# im.save(save_filename)


	# return img


def image_upload(dataUrl, save_filename, img_type):

    # decode (base64) the string to image
    # nparr = np.fromstring(img_str, np.uint8)
    # img2 = cv2.imdecode(nparr, cv2.CV_32FC4)
    
	get_image_from_dataurl(dataUrl, save_filename, img_type)

    # save image file to local computer
	# save_filename = 'test_image.png'
	# cv2.imwrite(save_filename, img)

    # upload image to S3
	bucketName = "lehuitest"
	#bucketName = "dap-final-project-vince"
	Key = save_filename                         # filename on local computer
	outputName = save_filename   # filename on S3
	
	s3 = boto3.client('s3')
	try:
		s3.upload_file(Key, bucketName, outputName)
		print("image uploaded to S3 successfully")
		image_url = construct_image_url(bucketName, outputName)
		return image_url
	except ClientError as e:
		logging.error(e)
		return None
    
    
def construct_image_url(bucketName, outputName):
    return "https://s3.amazonaws.com/{bucketName}/{outputName}".format(
        bucketName=bucketName, outputName=outputName)

        

    

    
