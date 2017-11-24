from user import User
from werkzeug.security import safe_str_cmp
#users=[

#{
#'id':1,
#'username':'thanuj',
#'password':'7899'

#}

#]

users=[ User(1,'thanuj','7899')]
username_mapping={u.username: u for u in users}
userid_mapping={u.id: u for u in users}
#username_mapping= {'thanuj':{
#'id':1,
#'username':'thanuj',
#'password':'7899'

#}
#}
# username_mapping['thanuj']
#userid_mapping={1:{
#'id':1,
#'username':'thanuj',
#'password':'7899'

#}
#}
#userid_mapping[1]


# we gonna create the two functions 
# 1  for authentication

def authenticate(username,password):
	user= username_mapping.get(username)
	if user and safe_str_cmp(user.password,password):
	#if user and user.password==password:
		return user
def identity(payload):
	user_id= payload['identity']
	return userid_mapping.get(user_id,None)