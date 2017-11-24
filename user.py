import sqlite3
from flask_restful import Resource,reqparse

class User:
	def __init__(self,_id,username,password):
		self.id=_id
		self.username=username
		self.password=password
	def find_by_username(self,username):
		conn= sqlite3.connect('data.db')
		cursor=conn.cursor()
		query="select * from users where username=?"
		result=cursor.execute(query,(username,))
		row =result.fetchone()
		if row:
			user=User(row[0],row[1],row[2])
		else:
			user=None
		conn.close()
		return user
	def find_by_id(self,_id):
		conn= sqlite3.connect('data.db')
		cursor=conn.cursor()
		query="select * from users where id=?"
		result=cursor.execute(query,(_id,))
		row =result.fetchone()
		if row:
			user=User(row[0],row[1],row[2])
		else:
			user=None
		conn.close()
		return user

class UserRegister(Resource):
	def post(self):
		parser=reqparse.RequestParser()
		#parser=reqparse.RequestParser()
		parser.add_argument('username',
		type=str,
		required=True,
		help="this can't be left blank"
		)
		parser.add_argument('password',
		type=str,
		required=True,
		help="fill this"
		)
		data=parser.parse_args()
		if User.find_by_username(User,username=data['username']):
			return {"message":"user already exists"},400
		conn=sqlite3.connect('data.db')
		cursor=conn.cursor()
		query="insert into users values(null,?,?)"
		cursor.execute(query,(data['username'],data['password']))
		
		conn.commit()
		conn.close()
		return {"message":"user created successfully"} , 201