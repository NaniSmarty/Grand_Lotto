import psycopg2
import logging
# import pandas as pd
from GILogger import *
def DB_connect():
    try: 
        conn = psycopg2.connect(database="GrandLottoonlinedb", user="postgres", password="GiChn32*", host="192.168.10.210", port="5432",options='-c statement_timeout=500')
        return conn
    except Exception as e:
        app_log.exception(e)
        
        
def DB_commit(conn):
    try:
        conn.commit()
    except Exception as e:
        app_log.exception(e)

def DB_rollback(conn):
    try:
        conn.rollback()
    except Exception as e:
        app_log.exception(e)

def DB_close(conn):
    try:
        conn.close()
    except Exception as e:
        app_log.exception(e)
def DB_callsp(conn, input, input1):
    try:
        cur = conn.cursor()
        #cur.callproc('get_production_Deployment', [72, ])
        #cur.execute("CALL getterminaldetails_login_v2(%s, %s);", (sub_str[1], sub_str[2]))
        #input="CALL getterminaldetails_login_v2(%s, %s);"
        #input1=sub_str[1], sub_str[2];
        cur.execute(input, input1)
        list_result = cur.fetchall()
        result = ""
        result = result.join(list_result[0])
        return result
    except Exception as e:
        app_log.exception(e)
