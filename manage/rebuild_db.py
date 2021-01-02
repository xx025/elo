# @File    : recreate.py.

# 对image文件夹内容向数据库重建
import os

from manage.conneMySQL import connect_mysql

filepath = "../image"

connect = connect_mysql()

connect.con()
print(connect.qure("show databases;"))
print(connect.update("create database if not exists beautgirl0x3"))  # 查询数据库
print(connect.qure("show databases;"))
connect.close()

connect.con("beautgirl0x3")
print(connect.update(
    '''CREATE TABLE IF NOT EXISTS `girls` ( `id` int(11) NOT NULL AUTO_INCREMENT,  `pothopath` varchar(77) DEFAULT NULL,  `score` double DEFAULT '1400',  `comNum` int(11) DEFAULT NULL,  PRIMARY KEY (`id`)) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;'''))
print(connect.qure("show tables"))  # 查询表格

connect.update('truncate girls')

for i in os.listdir(filepath):
    '''
    初始分值：1400
    初始比赛次数：0
    id:自动生成
    '''
    t = os.path.abspath(filepath).replace("\\","\\\\" )
    sql = 'insert into girls(pothopath,score, comNum) VALUES (\"{}\",{},{})'.format(t+"\\\\"+i, 1400, 0)
    print(sql)
    connect.update(sql)

connect.close()
