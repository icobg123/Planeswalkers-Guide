# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding("utf-8")
import os
import json
from myapplication import app
from flask import render_template, url_for, redirect, send_from_directory, abort
from random import shuffle

# Reading through a JSON files and converting the contents into a dictionaries
json_file_planeswalker = open('myapplication/static/data/planeswalkerInfo.json')
planeswalkerString = json_file_planeswalker.read()
planeswalkerData = json.loads(planeswalkerString)

json_file_homepage = open('myapplication/static/data/homepageInfo.json')
homePageString = json_file_homepage.read()
homePageData = json.loads(homePageString)

json_file_gallery = open('myapplication/static/data/galleryInfo.json')
galleryPageString = json_file_gallery.read()
galleryData = json.loads(galleryPageString)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
homePageTitle = homePageData
galleryTitle = galleryData


@app.route("/")
def home():
    images_names = os.listdir('myapplication/static/images/backgrounds')
    shuffle(images_names)
    print (images_names)
    return render_template('home.html', slideshow=images_names,
                           planeswalker=homePageTitle)


@app.route("/planeswalkers")
# return render_template('home.html', h=h)
def get_gallery():
    images_names = os.listdir('myapplication/static/images/walkers')
    print (images_names)
    return render_template('gallery.html', images_names=images_names,
                           planeswalker=galleryTitle)


@app.route('/planeswalkers/<pwName>')
def planeswalker(pwName):
    images_names = os.listdir('myapplication/static/images/planes')
    # planeswalkerNames = planeswalker_dict.keys()
    planeswalkerNames = planeswalkerData.keys()
    if pwName in planeswalkerNames:
        pwName = planeswalkerData.get(pwName)
        return render_template('planeswalker.html', planeswalker=pwName,
                               images_names=images_names)
    else:
        return abort(404)


@app.route('/../static/images/walkers/<filename>')
def send_image(filename):
    return send_from_directory("images", filename)


@app.route('/../static/images/backgrounds/<filename>')
def send_bg_images(filename):
    return send_from_directory("images", filename)
