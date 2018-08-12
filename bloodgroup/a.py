def create_user(username, password):
	print username, password
create_user(username="username",
	password="password")
data = {"username":"user6","password":"pwd"}
create_user(username=data.get("username"),
	password=data.get("password"))
create_user(**data)