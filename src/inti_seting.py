'''
测试数据库连接配置
数据库文件索引是否完整
'''

import json
from pathlib import Path

import pymysql


class MYSQL():
    # 初始化方法
    def __init__(self, host, port, user, passwd, dbName, charsets):
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.dbName = dbName
        self.charsets = charsets

    # 连接数据库
    def getcon(self):
        self.db = pymysql.Connect(
            host=self.host,
            port=self.port,
            user=self.user,
            passwd=self.passwd,
            db=self.dbName,
            charset=self.charsets
        )
        self.cursor = self.db.cursor()

    # 关闭链接
    def close(self):
        self.cursor.close()
        self.db.close()

    # 查询列表数据
    def get_all(self, sql):
        res = None
        try:
            self.cursor.execute(sql)
            res = self.cursor.fetchall()
        except:
            print("查询失败！")
        return res

    # 修改数据
    def edit(self, sql):
        return self.insert(sql)

    # 插入数据
    def insert(self, sql):
        count = 0
        try:
            count = self.cursor.execute(sql)
            self.db.commit()
        except:
            print("操作失败！")
            self.db.rollback()
        return count


class connect_db:

    def __init__(self):
        self.dbcon = None
        self.filepath = None
        try:
            with open('src\setting.json', 'r', encoding='utf-8') as load_f:
                load_dict = json.load(load_f)
                self.dbcon = self.test_con(load_dict["mysqldb"])  # 获取连接对象
        except:
            print("src\setting.json加载失败")

    def test_con(self, dict_):
        new_conmysql = MYSQL(host=dict_['host'], port=dict_['port'],
                             user=dict_['user'], passwd=dict_['passwd'],
                             dbName=dict_['dbName'], charsets="utf8")
        try:
            new_conmysql.getcon()
            new_conmysql.close()
        except:
            print("测试数据库连接错误")
            return False
        else:
            print("测试连接数据库成功")
            return new_conmysql


class testFilePath():
    def __init__(self):
        self.filepath = None
        try:
            with open('src/setting.json', 'r', encoding='utf-8') as load_f:
                load_dict = json.load(load_f)
                self.filepath = self.check_dir(load_dict["imgpath"])
        except:
            print("src/setting.json加载失败")

    def check_dir(self, path):
        my_file = Path(path)
        try:
            my_file.resolve()
        except FileNotFoundError:
            print("目录不存在")
        else:
            return path


filepath = testFilePath().filepath

con_db = connect_db().dbcon

