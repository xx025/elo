# @File    : recreate.py.

# 对image文件夹内容向数据库重建
import os

from src.inti_seting import con_db,filepath

con_db.getcon()
for i in  os.listdir(filepath):
    '''
    初始分值：1400
    初始比赛次数：0
    id:自动生成    
    '''
    sql='insert into girls(pothopath,score, comNum) VALUES (\'{}\',{},{})'.format(filepath+i,1400,0)
    print(sql)
    con_db.insert(sql)

con_db.close()