from flask_restful import Resource
from models.store import StoreModel



class Store(Resource):

    def get(self,name):
        
        if StoreModel.find_by_name(name):
            return StoreModel.find_by_name(name).json()
        
        return {"message":"Store not found"}

    def delete(self,name):
        store=StoreModel.find_by_name(name)

        if store:
            store.delete()
        else:
            return {"message":"Store not found"},404    

    def post(self,name):
        store=StoreModel.find_by_name(name)

        if store:
            return {"message":"Store already exists"}
        else:
            store=StoreModel(name)
            store.save_to_db()    

        return store.json(),201    



class StoreList(Resource):
        
    def get(self):
        return {"Stores":[store.json() for store in StoreModel.query.all()]}    