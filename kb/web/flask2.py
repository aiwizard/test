'''
한글이 보이는 Flask CSV Response 만들기
https://beomi.github.io/2017/11/28/Flask-CSV-Response/
'''

from io import StringIO
from flask import Flask, jsonify, request, Response
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) # Flask App 만들기
app.config['SQLALCHEMY_DATABASE_URI'] = '데이터베이스 URI' # SQLAlchemy DB 연결하기

db = SQLAlchemy()
db.init_app(app)

# 기타 설정을 해줬다고 가정합니다.

@app.route('/api/post/csv/') # URL 설정하기
def post_list_csv(self):
    queryset = Post.query.all()
    df = pd.read_sql(queryset.statement, queryset.session.bind) # Pandas가 SQL을 읽도록 만들어주기
    output = StringIO()
    output.write(u'\ufeff') # 한글 인코딩 위해 UTF-8 with BOM 설정해주기
    df.to_csv(output)
    # CSV 파일 형태로 브라우저가 파일다운로드라고 인식하도록 만들어주기
    response = Response(
        output.getvalue(),
        mimetype="text/csv",
        content_type='application/octet-stream',
    )
    response.headers["Content-Disposition"] = "attachment; filename=post_export.csv" # 다운받았을때의 파일 이름 지정해주기
    return response