from flask import Flask,request
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required
from security import authenticate,identity

app= Flask(__name__)
app.secret_key= 'thanuj'
api= Api(app)  # it allows use to add resource 


jwt= JWT(app,authenticate,identity) # jwt creates a new end point /auth then all username and password will be send for authenticate fucniton if matched we returns the user 
#jwt calls the identity fucniton and gets the correct user 

items=[]





class item(Resource):  #this will only access through get 
	@jwt_required()
	# this get method requires jwt token to be executed
	# this get method requires jwt token to be executed
	# this get method requires jwt token to be executed
	def get(self,name):
		item=next(filter(lambda x:x['name'] ==name, items ),None) # the next gives the first item that matches our filter but when no items match then it wil break
		return {'item':None},200 if item else 404
	def post(self,name):
		if next(filter(lambda x:x['name'] ==name, items ),None):
			return {'message':"an item with this name already exists"},400
		data= request.get_json()
		item={'name':name,'price':12.00}
		items.append(item)
		return item ,201
	def delete(self,name):
		global items
		items=list(filter(lambda x: x['name'] != name, items))
		return {'message':'item deleted'}
class ItemList(Resource):
	def get(self):
		return {'items':items}

api.add_resource(item,'/item/<string:name>')
api.add_resource(ItemList,'/item')

app.run(port=5000)

	

