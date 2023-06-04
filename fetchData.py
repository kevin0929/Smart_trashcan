import pymysql

def init_database():
    """
    initially config database
    and connect to return cursor
    """

    db_setting = {
        "host": "host IP",
        "port": "db port number",
        "user": "username",
        "password": "password",
        "db": "database name",
    }
    
    try:
        conn = pymysql.connect(**db_setting)
        cursor = conn.cursor()
        return cursor
    except Exception as e:
        print(f"{e}")
        raise

def get_data():
    """
    To fetch data from db
    and sent it to router "/"
    """
    
    cursor = init_database()
    cursor.execute("SELECT time, weight FROM trashcan ORDER BY time DESC LIMIT 1")
    result = cursor.fetchone()
    time, weight = result[0], result[1]
    
    return time, weight