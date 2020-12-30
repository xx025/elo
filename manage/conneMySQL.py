import pymysql


class connect_mysql:
    def __init__(self, host="localhost", user="root", port=3306, password="root"):
        self.user = user
        self.port = port
        self.password = password
        self.host = host

    # 建立连接
    def con(self, *args):
        try:
            if args.__len__() > 0:
                self.db = pymysql.connect(host=self.host, user=self.user, port=self.port, password=self.password, database=args[0])
            else:
                self.db = pymysql.connect(host=self.host, user=self.user, port=self.port, password=self.password)

            self.cursor = self.db.cursor()
        except:
            print("建立连接失败！")

    # 关闭链接
    def close(self):
        self.cursor.close()
        self.db.close()

    # 查询
    def qure(self, sql):
        result = tuple()
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
        except:
            print("查询失败！")
        finally:
            return result

    # 更新
    def update(self, sql):
        count = 0
        try:
            count = self.cursor.execute(sql)
            self.db.commit()
        except Exception as e:
            print(e)
            print(sql)
            print("操作失败！")
            self.db.rollback()
        finally:
            return count


