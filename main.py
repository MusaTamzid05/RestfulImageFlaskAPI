from flask import Flask
from flask import request
from flask import send_from_directory

from flask_restful import Resource
from flask_restful import Api
from flask_restful import reqparse
import werkzeug

app = Flask(__name__)
api = Api(app)

images = {}

parser = reqparse.RequestParser()
parser.add_argument("file", type = werkzeug.datastructures.FileStorage, location = "files" )
UPLOAD_DIR = "uploads"

import cv2
import os

class Image(Resource):

    def get(self, image_id):
        #this get wont do anything at the momment.
        # Its for future reference.

        if image_id not in images.keys():
            return {"result" : "No image found with id {}".format(image_id)}

        return {image_id : images[image_id]}

    def post(self):

        data = parser.parse_args()
        success , image_name =  self._upload(data)

        if success == False:
            return { "response" : "Error uploading image" }

        return send_from_directory(UPLOAD_DIR, image_name, as_attachment = True)

    def _upload(self, data):

        if data["file"] == "":
            return False, ""

        image = data["file"]
        image_name = "test.png"

        upload_path = os.path.join(UPLOAD_DIR, image_name)
        image.save(upload_path)
        return True , image_name


api.add_resource(Image,  "/" , "/<string:image_id>")

if __name__ == "__main__":
    app.run(debug = True)
