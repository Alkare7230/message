# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 15:29:42 2019

@author: Alkare
"""
from flask import Flask, escape

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'
