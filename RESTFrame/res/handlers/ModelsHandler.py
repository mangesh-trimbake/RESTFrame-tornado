
from datetime import datetime
from Models import *

from Models.Model import ModelName
import sys
sys.path.append("..")

from application.common import CommonBaseHandler

import json


class ModelNames(CommonBaseHandler):

    def get(self):
        
        self.set_headers()
        response_data = {}
        
        model_names = self.db.query(ModelName).all()
        model_names = self.get_result(model_names)
        
        response_data = json.dumps({
            'success': {
                'code': "202",
                'message': "model_names fetched",
                'data': model_names
            }
        }, default=self.json_default)
        
        self.write(response_data)
        self.finish()


    def post(self):
        
        self.set_headers()
        response_data = {}

        self.write(response_data)
        self.finish()

class ModelNamesShow(CommonBaseHandler):

    def get(self, model_name_id=None):
        
        self.set_headers()
        response_data = {}
        
        model_names = self.db.query(ModelName).filter(ModelName.id == model_name_id).first()
        model_names = self.get_result(model_names)
        
        response_data = json.dumps({
            'success': {
                'code': "202",
                'message': "model_names fetched",
                'data': model_names
            }
        }, default=self.json_default)
        
        self.write(response_data)
        self.finish()


    def post(self):
        
        self.set_headers()
        response_data = {}

        self.write(response_data)
        self.finish()



class ModelNamesAdd(CommonBaseHandler):

    def get(self):
        self.render("http://localhost:8000", ip_address=ip_obj.ip_address)

    def post(self):
        self.set_headers()
        response_data = {}

        model_name = self.request_data()

        model_name = self.patch_entity(ModelName,model_name)

        try:
            model_name  = ModelName(**model_name)
            self.db.add(model_name)
            self.db.commit()
            response_data = json.dumps({
                'success': {
                    'code': "202",
                    'message': "model_name added.",
                    'data': model_name
                }
            }, default=self.json_default)

        except SQLAlchemyError as e:
            print(e.args)
            self.db.rollback()
            response_data = json.dumps({
                'error': {
                    'code': "500",
                    'message': "error occured while adding."
                }
            }, default=self.json_default)

        else:
            pass
        finally:
            pass   
        

        self.write(response_data)
        self.finish()



class ModelNamesUpdate(CommonBaseHandler):

    def get(self,model_name_id=None):
        self.set_headers()
        response_data = {}

    def post(self, model_name_id=None):
        self.set_headers()
        response_data = {}

        model_name = self.request_data()
        
        model_name = self.patch_entity(ModelName,model_name)                

        try:
            self.db.query(ModelName).filter(ModelName.id == model_name_id).update(model_name)
            self.db.commit()
            response_data = json.dumps({
                'success': {
                    'code': "202",
                    'message': "model_name updated.",
                    'data': model_name
                }
            }, default=self.json_default)

        except SQLAlchemyError as e:
            print(e.args)
            self.db.rollback()
            response_data = json.dumps({
                'error': {
                    'code': "500",
                    'message': "error occured while update."
                }
            }, default=self.json_default)

        else:
            pass
        finally:
            pass            

        self.write(response_data)
        self.finish()


