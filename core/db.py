#-*- coding: utf-8 -*-
from config import db_params, multiplier
from datetime import datetime
import psycopg


def dbconn():
    try:
        conn = psycopg.connect(**db_params)
        with conn.cursor() as cur:
            cur.execute("SELECT version();")
            db_version = cur.fetchone()
            response = f'Подключение к базе данных PostgreSQL успешно. Версия PostgreSQL: {db_version}'
            cur.close()
    except (Exception, psycopg.Error) as error:
        response = f'Ошибка PostgreSQL: {error}'
    finally:
        conn.close()
    return response

def start(user_id, nickname, subscription, admin_on, avatar_url, experience):
    try:
        conn = psycopg.connect(**db_params)
        with conn.cursor() as cur:
            cur.execute("INSERT INTO pijawcacast (user_id, nickname, subscription, admin_on, avatar_url, experience) VALUES (%s, %s, %s, %s, %s, %s)",
                            (user_id, nickname, subscription, admin_on, avatar_url, experience))
            conn.commit()
            response = 0
    except:
        conn = psycopg.connect(**db_params)
        with conn.cursor() as cur:
            cur.execute("UPDATE pijawcacast SET user_id = %s, nickname = %s, subscription = %s, admin_on = %s, avatar_url = %s WHERE user_id = %s", (user_id, nickname, subscription, admin_on, avatar_url, user_id))
            conn.commit()
            response = 1
    finally:
        conn.close()
    return response

def profile(user_id):
    try:
        conn = psycopg.connect(**db_params)
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM pijawcacast WHERE user_id = %s", (user_id,))
            rows = cur.fetchall()
            cur.execute("SELECT COUNT(*) + 1 FROM pijawcacast WHERE experience > (SELECT experience FROM pijawcacast WHERE user_id = %s)", (user_id,))
            placehold = cur.fetchone()
    except Exception as e:
        print(e) 
    return rows, placehold

def on_voice_state_update(before, after, user_id):
    try:
        conn = psycopg.connect(**db_params)
        with conn.cursor() as cur:
            if before is None and after is not None:
                cur.execute("UPDATE pijawcacast SET last_voice_join = CURRENT_TIME WHERE user_id = %s", (user_id,))
                conn.commit()
                
    except Exception as e:
        print(e)
        
def update_experience(user_id):
    try:
        conn = psycopg.connect(**db_params)
        with conn.cursor() as cur:
            cur.execute("SELECT last_voice_join FROM pijawcacast WHERE user_id = %s", (user_id,))
            last_join_time = cur.fetchone()[0]
            last_join_time = str(last_join_time)[:8]
            current_time = datetime.now().replace(microsecond=0).time()
            current_time = str(current_time)
            time1 = datetime.strptime(current_time, "%H:%M:%S")
            time2 = datetime.strptime(last_join_time, "%H:%M:%S")
            time_diff = time1 - time2
            total_seconds = time_diff.total_seconds()
            total_seconds = int(total_seconds) / 3
            total = int(total_seconds*multiplier)/100
            cur.execute("UPDATE pijawcacast SET experience = experience + %s WHERE user_id = %s", (total, user_id))
            conn.commit()
            
    except Exception as e:
        print(e)
    
def rank(user_id):
    try:
        conn = psycopg.connect(**db_params)
        with conn.cursor() as cur:
            cur.execute("SELECT experience FROM pijawcacast WHERE user_id = %s", (user_id,))
            row = cur.fetchone()
            
    except Exception as e:
        print(e)
        
    return row

def castopendota(user_message, user_id):
    try:
        conn = psycopg.connect(**db_params)
        with conn.cursor() as cur:
            cur.execute("UPDATE pijawcacast SET opendota_id = %s WHERE user_id = %s", (user_message, user_id,))
            conn.commit()
        
    except Exception as e:
        print(e) 
        
def fetchall(user_id):
    try:
        conn = psycopg.connect(**db_params)
        with conn.cursor() as cur:
            cur.execute(f"SELECT * FROM pijawcacast WHERE user_id = {user_id}")
            rows = cur.fetchall()
    except Exception as e:
        print(e) 
    return(rows)
