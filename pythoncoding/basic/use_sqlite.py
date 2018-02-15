# 导入库：
import os, sqlite3


# 创建文件：
db_file = os.path.join(os.path.dirname(__file__), 'test.db')
if os.path.isfile(db_file):
    os.remove(db_file)
    
# 初始数据：
# 连接到数据库：
conn = sqlite3.connect(db_file)
# 创建cursor：
cursor = conn.cursor()
# 创建user表：
cursor.execute('create table user(id varchar(20) primary key, name varchar(20), score int)')
# 插入记录：
cursor.execute(r"insert into user values ('A-001', 'Adam', 95)")
cursor.execute(r"insert into user values ('A-002', 'Bart', 62)")
cursor.execute(r"insert into user values ('A-003', 'Lisa', 78)")
# 关闭cursor和connection:
cursor.close()
conn.commit()
conn.close()

# 定义函数，返回指定分数区间的名字，按分数从低到高排序：
def get_score_in(low, high):
    try:
        con = sqlite3.connect(db_file)
        cursor = con.cursor()
        cursor.execute("select * from user where score > ? AND score <= ? ORDER BY score", (str(low), str(high)))
        temp = cursor.fetchall()
        print(temp)
    finally:
        cursor.close()
        conn.close()
    return [i[1] for i in temp]
    
    
# 测试：
assert get_score_in(80, 95) == ['Adam'], get_score_in(80, 95)
assert get_score_in(60, 80) == ['Bart', 'Lisa'], get_score_in(60, 80)
assert get_score_in(60, 100) == ['Bart', 'Lisa', 'Adam'], get_score_in(60, 100)

print('Pass')