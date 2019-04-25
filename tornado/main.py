from tornado.web import Application
from tornado.web import RequestHandler
from tornado.ioloop import IOLoop
import json
from producer_upload import upload_produce_message
from image_upload import image_upload
# from model_service.model_service import predict

class ChartHandler(RequestHandler):
    pass

class RemoveHandler(RequestHandler):
    pass
class UploadHandler(RequestHandler):
    
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', "POST, GET, OPTIONS")
        self.set_header('Content-Type', 'text/html')
        self.set_header("Access-Control-Allow-Credentials", 'true')

    def get(self):
        
        self.set_default_headers()
        s = "Please use POST request on /upload"
        # s = {"message": s}
        # s = json.dumps(s)
        self.set_status(200)
        self.write(s)
        # result_url = predict(image_url,mask_url)
        # self.render("../template/result.html",result = result_url)
    
    def options(self):
        self.set_default_headers()
        self.set_status(204)
        self.finish()

    def post(self):
        data = json.loads(self.request.body)
        
        print("request = ", data)
        image = self.request.body['original']
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
        # self.render("../template/result.html",result = result_url)

        # return to frontend


if __name__ == "__main__":
    handler_mapping = [
                       (r'/remove$', RemoveHandler),
                       (r'/upload$', UploadHandler),
                       (r'/chart$', ChartHandler)
                      ]
    application = Application(handler_mapping)
    application.listen(7777)
    IOLoop.current().start()