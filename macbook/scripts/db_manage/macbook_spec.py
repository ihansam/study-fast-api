import json
from pprint import pprint

import pymysql
from pymysql import cursors


with open("../../db_config.json") as cf:
    params: dict = json.load(cf)


connection = pymysql.connect(**params)


# # DB 생성
# with connection:
#     with connection.cursor(cursors.Cursor) as cursor:
#         cursor.execute("CREATE DATABASE mac")
#         connection.commit()

# # DB 생성 확인
# with connection:
#     with connection.cursor(cursors.Cursor) as cursor:
#         cursor.execute("SHOW DATABASES")
#         print(*cursor)


# # Table 생성
# with connection:
#     with connection.cursor(cursors.Cursor) as curs:
#         query = """
#             CREATE TABLE macbook_spec (
#                 pid INT AUTO_INCREMENT PRIMARY KEY,
#                 pname VARCHAR(255) NOT NULL UNIQUE,
#                 processor VARCHAR(255),
#                 display FLOAT,
#                 unpack INT
#                 );
#                 """
#         curs.execute(query)
#         connection.commit()

# # Data 추가
# with connection:
#     with connection.cursor(cursors.Cursor) as curs:
#         query = """
#             INSERT INTO macbook_spec (pname, processor, display, unpack)
#             VALUES(%s, %s, %s, %s);
#         """
#         values = [
#             ("Macbook Test Air", "M0", 11, 1996),
#             ("Macbook Test Pro", "M0", 12.9, 1996)
#         ]
#         curs.executemany(query, values)
#
#         connection.commit()

# Data 조회
with connection:
    with connection.cursor(cursors.DictCursor) as curs:
        curs.execute("select * from macbook_spec")
        pprint(curs.fetchall(), sort_dicts=False)
