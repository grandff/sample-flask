from flask import Flask, request         # 서버 구현을 위한 객체
from flask_restx import Api, Resource   # api 구현을 위한 객체

app = Flask(__name__)   # flask 객체 선언, 파라미터로 어플리케이션 패키지 이름 넣어줌
api = Api(app)  # flask 객체에 api 객체 등록

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

# get post put delete 구현
todos = {}
count = 1

# post
@api.route('/todos')
class TodoPost(Resource) :
    def post(self) :
        global count
        global todos

        idx = count
        count += 1
        todos[idx] = request.json.get('data')      # json data get

        return {
            'todo_id' : idx,
            'data' : todos[idx]
        }

@api.route('/todos/<int:todo_id>')
class TodoSimple(Resource) :
    def get(self, todo_id) :        # 현재 todos에 저장되어있는 값 확인
        return {
            'todo_id' : todo_id,
            'data' : todos[todo_id]
        }

    def put(self, todo_id) :
        todos[todo_id] = request.json.get('data')
        return {
            'todo_id' : todo_id,
            'data' : todos[todo_id]
        }

    def delete(sel, todo_id) :
        del todos[todo_id]
        return {
            "delete" : "success"
        }

if __name__ == "__main__" :
    app.run(debug=True, host='0.0.0.0', port=60)