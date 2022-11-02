import pymysql
from app import app
from config import mysql
from flask import jsonify
from flask import flash, request


@app.route('/kayit', methods=['GET', 'POST'])
def kayit():
    try:
        _json = request.json
        _ad = _json['ad']
        _soyad = _json['soyad']
        if request.method == 'POST':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            sqlQuery = "INSERT INTO kayit ( ad, soyad) VALUES (%s, %s)"          
            bindData = (_ad, _soyad)
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            respone = jsonify('Kullanici basariyla eklendi')
            respone.status_code = 200
            return respone
        else:
            return showMessage()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route('/list', methods=['GET'])
def list():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM kayit")
        kayitRows = cursor.fetchall()
        respone = jsonify(kayitRows)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0')
