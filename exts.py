#@project:checkDomain
#@author:chenliangfu
#@file:myfile.py
#@time:2018-7-6  15:00:00
#@Description:XX

#encoding:utf-8
from flask_sqlalchemy import SQLAlchemy
import  pymysql

pymysql.install_as_MySQLdb()
db= SQLAlchemy()