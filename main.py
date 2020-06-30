from flask import Flask
from flask import request
from flask import send_from_directory

from flask_restful import Resource
from flask_restful import Api


app = Flask(__name__)
api = Api(app)

images = {}

import cv2

class Image(Resource):

    def get(self, image_id):
        if image_id not in images.keys():
            return {"result" : "No image found with id {}".format(image_id)}

        return {image_id : images[image_id]}

    def post(self):

        image_name = request.form["data"]
        return send_from_directory("results", image_name, as_attachment = True)



api.add_resource(Image,  "/" , "/<string:image_id>")

if __name__ == "__main__":
    app.run(debug = True)
