#!/usr/bin/python3
# -*- coding: utf-8 -*-

# This Application is used to classtify images using Tensorflow (InceptionV3) and build on Flask Framework.
import os, uuid
from flask import Flask
from image_rec import ImageRec

app = Flask(__name__)
app.image_rec = ImageRec()

if __name__ == "__main__":
    file_name = 'target.jpg'
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    results = app.image_rec.run(file_path)
