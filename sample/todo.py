from flask import request
from flask_restx import Resource, Api, Namespace, fields

# name space 로 파일 분리
# 마찬가지로 설명 수정이 가능함
Todo = Namespace(
    name = 'Todo',
    description = 'shit the fuck'
)

# .model을 통해 입력, 출력에 대한 스키마 표시
todo_fields = Todo.model('Todo', {
    'data' : fields.String(description = 'a Todo', required = True, example = 'What to do')
})

# 기존에 생성된 모델을 상속받아서 표현 가능
todo_fields_with_id = Todo.inherit('TOdo With ID', todo_fields, {
    'todo_id' : fields.Integer(description = 'a Todo ID')
})

# get post put delete 구현
todos = {}
count = 1


@Todo.route('')
class TodoPost(Resource) :
    @Todo.expect(todo_fields) # 특정 스키마가 들어올거라고 예측
    @Todo.response(201, 'Success', todo_fields_with_id) # 특정 스키마가 반환될거라고 안내
    def post(self) :    # post
        """Todo 리스트에 할일 등록을 함""" # 이런식으로 document에 설명 추가 가능
        global count
        global todos

        idx = count
        count += 1
        todos[idx] = request.json.get('data')      # json data get

        return {
            'todo_id' : idx,
            'data' : todos[idx]
        }, 201

@Todo.route('/<int:todo_id>')
@Todo.doc(params={'todo_id' : 'An ID'}) # 쿼리 파라미터에 대한 설명 명시
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

    @Todo.doc(responses={202 : 'Success'})
    @Todo.doc(responses={500 : 'Failed'})
    def delete(sel, todo_id) :
        del todos[todo_id]
        return {
            "delete" : "success"
        }, 202
