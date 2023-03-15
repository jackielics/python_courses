import pymysql

# 连接MySQL数据库
conn = pymysql.connect(
    host='192.168.157.130',
    port=3306,
    user='jack',
    password='123',
    database='mysql',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

# 创建一个游标对象
cursor = conn.cursor()

# 执行查询语句
cursor.execute('SELECT * FROM db')

# 获取查询结果
result = cursor.fetchall()
print(result)

# 关闭游标和连接
cursor.close()
conn.close()
