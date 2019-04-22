from tornado.web import Application
from tornado.web import RequestHandler
from tornado.ioloop import IOLoop
import json
from producer_upload import upload_produce_message
from image_upload import image_upload


class ChartHandler(RequestHandler):
    pass

class RemoveHandler(RequestHandler):
    pass

class UploadHandler(RequestHandler):
    
    def get(self):
        s = "Please use POST request on /upload"
        self.write(s)
    
    def post(self):
        image = self.request.body
        if image is not None:
            s = "image received"
            print(s)
            self.write(s)
            # produce_message(message)
            
            # upload image to s3
            image_name = image_upload(image)
            
            # Kafka producer produce message
            if image_name is not None:
                upload_produce_message(image_name)
            
        else:
            s = "image not received"
            self.write(s)
            print(s)


if __name__ == "__main__":
    handler_mapping = [
                       (r'/remove$', RemoveHandler),
                       (r'/upload$', UploadHandler),
                       (r'/chart$', ChartHandler)
                      ]
    application = Application(handler_mapping)
    application.listen(7777)
    IOLoop.current().start()