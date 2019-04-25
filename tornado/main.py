from tornado.web import Application
from tornado.web import RequestHandler
from tornado.ioloop import IOLoop
import json
from producer_upload import upload_produce_message
from image_upload import image_upload
from model_service.model_service import predict

class ChartHandler(RequestHandler):
    pass

class RemoveHandler(RequestHandler):
    pass
class UploadHandler(RequestHandler):
    
    def get(self):
        s = "Please use POST request on /upload"
        self.write(s)
        # result_url = predict(image_url,mask_url)
        # self.render("../template/result.html",result = result_url)
    
    def post(self):
        image = self.request.body['image']
        mask = self.request.body['mask']

        if image is not None:
            s = "image received"
            print(s)
            self.write(s)
            # produce_message(message)
            message = {}

            # upload image to s3 and return output url in s3
            image_url = image_upload(image)
            mask_url = image_upload(mask)

            user_id = 'liulehui'
            
            # construct message
            message["image_url"] = image_url
            message["user_id"] = user_id
            message_json = json.dumps(message)


            # Kafka producer produce message
            if image_url is not None:
                upload_produce_message(message_json)
            
        else:
            s = "image not received"
            self.write(s)
            print(s)

        result_url = predict(image_url,mask_url)
        self.render("../template/result.html",result = result_url)


if __name__ == "__main__":
    handler_mapping = [
                       (r'/remove$', RemoveHandler),
                       (r'/upload$', UploadHandler),
                       (r'/chart$', ChartHandler)
                      ]
    application = Application(handler_mapping)
    application.listen(7777)
    IOLoop.current().start()