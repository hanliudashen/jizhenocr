#!/usr/bin/python
# -*- coding: UTF-8 -*-
#极诊团队
#Author 刘翰

from flask import Flask, render_template, request

# 系统
import os
import tensorflow as tf
import pickle

# 自定义


app = Flask(__name__)

flags = tf.app.flags


flags.DEFINE_string('ckpt_path', os.path.join('modelfile', 'ckpt'), '保存模型的位置')
flags.DEFINE_string('map_file', 'maps.pkl', '存放字典映射及标签映射')
flags.DEFINE_string('config_file', 'config_file', '配置文件')

FLAGS = tf.app.flags.FLAGS



@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/getPer', methods=["POST"])
def getPer():
    source = request.form.get('per')
    return " "


# @app.route('/getOrg', methods=["POST"])
# def getOrg():
#     source = request.form.get('org')
#     if source is None or source is "":
#         return "输入不能为空，请重新出入"
#     result = evaluate_line(source)
#     print(type(result))
#     if result is None:
#         return "没有可识别的实体"
#     entites = result['entities']
#     org = []
#     for entity in entites:
#         if entity['type'] == "DIS":
#             org.append(entity['word'])
#     return " ".join(org)




if __name__ == '__main__':
    app.run(debug=True, port='5000', host='127.0.0.1')
