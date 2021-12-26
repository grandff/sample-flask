from flask import Flask, request         # 서버 구현을 위한 객체
from flask_restx import Api, Resource
from sample.todo import Todo   # api 구현을 위한 객체

app = Flask(__name__)   # flask 객체 선언, 파라미터로 어플리케이션 패키지 이름 넣어줌
# flask 객체에 api 객체 등록
# api 서버 기본 안내 설정(포트까지만 치고 들어가면 됨)
api = Api(
    app,
    version = '0.1',
    title = 'Sample Flask API Server',
    description = 'Holy Shit',
    terms_url = "/",
    contact = "dsaqaz421@gmail.com",
    license = "MIT"
)

@api.route('/hello')        # /hello 경로에 클래스 등록
class HelloWorld(Resource) :
    def get(self) :     # get 요청시 리턴 값에 해당하는 dict를 json 형태로 변환
        return {
            "hello" : "world!"
        }

# url pattern
@api.route('/hello2/<string:name>')     # url pattern으로 name 설정
class Hello(Resource) :
    def get(self, name):
        return {
            "message" : "Welcome, %s" % name
        }

# 분리한 파일 추가
api.add_namespace(Todo, '/todos')



if __name__ == "__main__" :
    app.run(debug=True, host='0.0.0.0', port=60)