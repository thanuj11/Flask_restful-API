from flask import Flask,request
from flask_restful import Resource, Api, reqparse

app= Flask(__name__)
api= Api(app)  # it allows use to add resource 

items=[]





class item(Resource):  #this will only access through get 
	
	def get(self,name):
		
		for i in items:
			if i['name']==name:
				return i
			return {'item':None},404
	def post(self,name):
		item={'name':name,'price':12.00}
		items.append(item)
		return item ,201
	def delete(self,name):
		global items
		items=list(filter(lambda x: x['name'] != name, items))
		return {'message':'item deleted'}
	def put(self,name):
		parser = reqparse.RequestParser()
		parser.add_argument('price',type=float,required=True,help="this cna't be blank")
		#data= request.get_json()
		data= parser.parse_args()
		item= next(filter(lambda x:x['name']==name,items),None)
		if item is None:
			#item={'name':name, 'price':17.99}
			item={'name':name, 'price':data['price']}
			items.append(item)
		else:
			item.update(data)
		return item
class ItemList(Resource):
	def get(self):
		return {'items':items}

api.add_resource(item,'/item/<string:name>')
api.add_resource(ItemList,'/item')

app.run(port=5000)

	

