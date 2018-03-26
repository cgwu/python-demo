from django.db import connection

"""
    db: 数据库原生SQL访问帮助方法
    get_all: 返回字典列表
    get_one: 返回单个字典
    get_scalar: 返回单个值
    exec: 执行SQL语句
"""
class db:
    @staticmethod
    def get_all(str_sql, list_args=[]):
        with connection.cursor() as cursor:
            cursor.execute(str_sql, list_args)
            list_dict = db.dict_fetch_all(cursor)
        return list_dict

    @staticmethod
    def get_one(str_sql, list_args=[]):
        with connection.cursor() as cursor:
            cursor.execute(str_sql, list_args)
            one_dict = db.dict_fetch_one(cursor)
        return one_dict

    @staticmethod
    def get_scalar(str_sql, list_args=[]):
        with connection.cursor() as cursor:
            cursor.execute(str_sql, list_args)
            one_tuple = cursor.fetchone()
        if one_tuple == None:
            return None
        return one_tuple[0]

    @staticmethod
    def exec(str_sql, list_args=[]):
        with connection.cursor() as cursor:
            result = cursor.execute(str_sql, list_args)
        return result

    # 以下为帮助方法
    @staticmethod
    def dict_fetch_all(cursor):
        "Return all rows from a cursor as a dict"
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]

    @staticmethod
    def dict_fetch_one(cursor):
        desc = cursor.description
        if desc == None:
            return None
        columns = [col[0] for col in desc]
        row = cursor.fetchone()
        if row == None:
            return None
        return dict(zip(columns,row))

