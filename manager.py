#@project:checkDomain
#@author:chenliangfu
#@file:myfile.py
#@time:2018-7-6  15:00:00
#@Description:XX

from flask_script import  Manager
from flask_migrate import Migrate,MigrateCommand
from zlktqa import app
from exts import db
from models import User,Question,Answer

manager = Manager(app)
migrate = Migrate(app,db)



manager.add_command('db',MigrateCommand)

if __name__ =='__main__':
    manager.run()



