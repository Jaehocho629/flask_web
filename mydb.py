import pymysql

db = pymysql.connect(host='localhost', port=3306, user='root', passwd='1234',db='myflaskapp')
cursor = db.cursor()
# sql = ''' 
#         CREATE TABLE users(
#             id INT(11) AUTO_INCREMENT PRIMARY KEY,  
#             name VARCHAR(100),
#             email VARCHAR(100),
#             username VARCHAR(30),
#             password VARCHAR(100),
#             register_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP)
#             ENGINE=InnoDB DEFAULT CHARSET=utf8;
#     '''

# sql = '''
#     CREATE TABLE `topic` (
# 	`id` int(11) NOT NULL AUTO_INCREMENT,
# 	`title` varchar(100) NOT NULL,
# 	`body` text NOT NULL,
# 	`author` varchar(30) NOT NULL,
# 	create_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
#     PRIMARY KEY (id)
# 	) ENGINE=innoDB DEFAULT CHARSET=utf8;

# '''

# cursor.execute(sql)
# db.commit()
# db.close()


sql_1 = 'SELECT * FROM users;'
# sql_2 = '''
#            INSERT INTO users(name,email,username,password) 
#            VALUES ('PARK','4@naver.com','PARK','1234');
#            '''

# cursor.execute(sql_2)
# db.commit()
# db.close()
# users = cursor.fetchall()
# print(users[0][1])
# # # print(result)
# cursor.execute(sql_1)
# users = cursor.fetchall()
# print(users)

name = 'SONG'
email = '5@naver.com'
username = 'SONG'
password = '1234'

sql_3 = '''
           INSERT INTO users(name,email,username,password) 
           VALUES ( %s, %s, %s, %s);
           '''
# cursor.execute(sql_3, (name,email,username,password))
# db.commit()
# db.close()


title='javascript'
body='프로토타입기반의 객체지향 프로그래밍 언어로, 스크립트 언어에 해당된다. 특수한 목적이 아닌 이상 모든 웹 브라우저에 인터프리터가 내장되어 있다. 오늘날 HTML, CSS와 함께 웹을 구성하는 요소 중 하나다.'
author='gary'
sql_7 = '''
           INSERT INTO topic(title, body, author) 
           VALUES ( %s, %s, %s);
           '''
# cursor.execute(sql_7,(title,body,author))
# db.commit()
# db.close()

# name = 'GANGNAM'
# email = '6@naver.com'
# username = 'GANGNAM'
# password = '1234'

sql_4 = '''
           INSERT INTO users(name,email,username,password) 
           VALUES ( %s, %s, %s, %s);
           '''

# cursor.execute(sql_4, (name,email,username,password))
# db.commit()
# db.close()

# sql_5 = 'DELETE FROM `myflaskapp`.`users` WHERE  `id`=5;'
# cursor.execute(sql_5)
# db.commit()
# db.close

# sql_6 = 'DELETE FROM users WHERE name="SONG";'
# cursor.execute(sql_6)
# db.commit()
# db.close

# sql_8 = 'SELECT * FROM topic;'

# cursor.execute(sql_8)
# topics = cursor.fetchall()
# print(topics)


title='python'
body='python'
author='cho'
sql_9 = '''
           INSERT INTO topic(title, body, author) 
           VALUES ( %s, %s, %s);
           '''
cursor.execute(sql_9,(title,body,author))
db.commit()
db.close()