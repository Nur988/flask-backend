
import sqlite3
from typing import Text
from flask_restful import Resource,reqparse
from flask_jwt import JWT, jwt_required
from flask import request
from models.item import ItemModel




class Item(Resource):
    parser=reqparse.RequestParser()

    parser.add_argument('price',
            type=float,
            required=True,
            help='This field cannot be left blank'
        )
    parser.add_argument('store_id',
            type=int,
            required=True,
            help='Store id required'
        )
        
    
    @jwt_required()
    def get(self,name):
        item=ItemModel.find_by_name(name)

        if item:
            return item.json()
        return {"message":"Item not found"},404   

    

    def post(self,name):
        if ItemModel.find_by_name(name):
            # 404 is for bad request
            return {'message':"An  item with name '{}' already exists".format(name)},400
        # request hold the json data sent trhough the http request
        data=Item.parser.parse_args()
        item=ItemModel(name,**data)
        item.insert()
        return item.json(),201
    
    def delete(self,name):
        item=ItemModel.find_by_name(name)
        item.delete()
        return {"message":"Item {} has been succesfully deleted ".format(name)}
    
    def put(self,name):
        # data=request.get_json()
        data=Item.parser.parse_args()

        item=ItemModel.find_by_name(name)
      
        if item is None:
            try:
              item=ItemModel(name,**data)
            except:
                return {"message":"Error occured while inserting the item"},500   
        else:
            try:
               
               item.price=data["price"]
            except:
                return {"message":"Error occured while updating the item"},500  
        item.save_to_db()               
        return item.json()  
class ItemList(Resource):
    def get (self):
        
        return {"items":[item.json() for item in ItemModel.query.all()]}    


        