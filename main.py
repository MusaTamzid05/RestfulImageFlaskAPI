from flask import Flask
from flask import request

from flask_restful import Resource
from flask_restful import Api


app = Flask(__name__)
api = Api(app)

images = {}

class Image(Resource):

    def get(self, image_id):
        if image_id not in images.keys():
            return {"result" : "No image found with id {}".format(image_id)}

        return {image_id : images[image_id]}

    def post(self):
        image_id = str(len(images) + 1)
        images[image_id] = request.form["data"]
        return {image_id : images[image_id]}


api.add_resource(Image,  "/" , "/<string:image_id>")

if __name__ == "__main__":
    app.run(debug = True)
