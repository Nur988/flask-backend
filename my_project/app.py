from email import message
from flask import Flask,request
from flask_restful import Resource,Api,reqparse
from resource.user import UserRegister
from security import authenticate,identity
from flask_jwt import JWT, jwt_required
from resource.user import UserRegister
from resource.item import Item,ItemList
from resource.store import Store,StoreList

app=Flask(__name__)

# it is sacret key that should not be visible in production code
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///data.db"
app.secret_key="jose"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
api=Api(app)

@app.before_first_request
def create_all():
    db.create_all()
jwt=JWT(app,authenticate,identity)

# each class here that inherits Resource class acts as an endpoint
# each has its own get and post method that responds to the get and post request
# 




# the clss name and URL are added below to bind them as one endpoint
api.add_resource(Item,'/item/<string:name>')
api.add_resource(ItemList,'/items')
api.add_resource(UserRegister,'/register')
api.add_resource(Store,"/store/<string:name>")
api.add_resource(StoreList,"/stores")



if __name__=='__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000)