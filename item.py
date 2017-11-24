from flask import Flask,request
from flask_restful import Resource,Api,reqparse
from flask_jwt import JWT,jwt_required

import sqlite3




class Item(Resource):
	@jwt_required()
	def get(self,name):
		item1=self.find_by_name(name)
		if item1:
			return item1
		return {'message':'item not found'}
		
		#for item in items:
		#	if item["name"]==name:
		#		return item
	@classmethod
	def find_by_name(cls,name):
		conn=sqlite3.connect('data.db')
		cursor=conn.cursor()
		query="select * from items where name=?"
		result=cursor.execute(query,(name,))
		row=result.fetchone()
		conn.close()
		if row:
			return {'item':{'name':row[0],'price':row[1]}}
	def post(self,name):
		parser=reqparse.RequestParser()
		parser.add_argument('price',
		type=float,
		required=True,
		help="this can't be left blank"
		)
		if self.find_by_name(name):
			return {"message":"already exists"}
		
		
		
		data= parser.parse_args()
		#data=request.get_json()
		item={"name":name,"price":data["price"]}
		try:
			self.insert(item)
		except:
			return {"message":"exception occured"},500
		return item, 201
	@classmethod
	def insert(cls,item):
		conn=sqlite3.connect('data.db')
		cursor=conn.cursor()
		query="insert into items values (?,?)"
		cursor.execute(query,(item['name'],item['price']))
		
		conn.commit()
		conn.close()
	
	
	
	def delete(self,name):
		conn=sqlite3.connect('data.db')
		cursor=conn.cursor()
		query="delete from items where name=?"
		cursor.execute(query,(name,))
		
		conn.commit()
		conn.close()
		return{'message':"item deleted"}
		
		
		
		#global items
		#for item in items:
		#	if item["name"]==name:
		#		items.remove(item)
		#		return{"message":"item deleted"}
	def put(self,name):
		parser=reqparse.RequestParser()
		parser.add_argument('price',
		type=float,
		required=True,
		help="this can't be blank"
		)
		
		data= parser.parse_args()
		item=self.find_by_name(name)
		updated_item={'name':name,'price':data['price']}
		#item= next(filter(lambda x:x['name']==name ,items),None)
		if item is not None:
			try:
				self.insert(updated_item)
			except:
				return{"message":"error occured"}
		else:
			self.update(updated_item)
		return item
	@classmethod
	def update(cls,item):
		conn=sqlite3.connect('data.db')
		cursor=conn.cursor()
		query="update items set price=? where name=?"
		cursor.execute(query,(item['price'],item['name']))
		
		conn.commit()
		conn.close()
class ItemList(Resource):
	def get(self):
		conn=sqlite3.connect('data.db')
		cursor=conn.cursor()
		query="select * from items"
		result=cursor.execute(query)
		items=[]
		for row in result:
			items.append({'name':row[0],'price':row[1]})
		conn.commit()
		conn.close()
		return {'items':items}

		