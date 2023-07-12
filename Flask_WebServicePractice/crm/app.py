from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    # TODO : 월간 매출액 함산을 구하시오

    # 테이블로  2023-1 ~  2023-12 까지 월간 매출액을 구하는 쿼리문 작성

    # 1. DB에 접속
    conn = sqlite3.connect("/Users/jeongjaeyeong/Project/SeSac/Flask_WebServicePractice/crm/crm.db")
    # 2. 커서 만든다 (가져온다)
    cursor = conn.cursor()
    # 3. SQL 구문을 작성한다
    query = """
        SELECT
            strftime('%Y-%m', 'orders'.'OrderAt') AS month,
            SUM('items'.'UnitPrice') AS Revenue
        FROM
            'orders'
        JOIN 
            'orderitems' ON 'orders'.'Id' = 'orderitems'.'Orderid'
        JOIN
            'items' ON 'orderitems'.'ItemId' = 'items'.'id'
        GROUP BY
            strftime('%Y-%m', 'orders'.'OrderAt')

        """
    # 4. 쿼리문을 실행해서 결과를 받아온다 (리스트 형태)
    cursor.execute(query)
    # 5. 렌더 템플릿에 데이터를 전송한다.
    rows = cursor.fetchall()

    labels = []
    revenues = []

    for row in rows:
        labels.append(row[0])
        revenues.append(row[1])

    return render_template("index.html", rows=rows, labels=labels, revenues=revenues5)

if __name__ == "__main__":
    app.run(debug=True, port=8080)