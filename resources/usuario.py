from typing_extensions import Required
from flask_restful import Resource, reqparse
from models.usuario import UserModel

class User(Resource):
    # /usuarios/{user_id}
    def get(self, user_id):
        
        user = UserModel.find_user(user_id)
        if user:
            return user.json()
        
        return {"message":"User not found"}, 404 #not found

    def delete(self, user_id):
        user = UserModel.find_user(user_id)
        if user:
            try:
                user.delete_user()
            except:
                return {'message': 'A internal error ocurred trying to delete user.'}, 500 #Internal Server Error
            return {'message': 'User deleted!'}, 201 

        return {'message': 'User not found!'}

class UserRegister(Resource):
    #/cadastro/
    def post(self):
        atributos = reqparse.RequestParser()
        atributos.add_argument('login',type=str, required=True, help="The 'login' field cannot be made blank.")    
        atributos.add_argument('senha',type=str, required=True, help="The 'senha' field cannot be made blank.")
        dados = atributos.parse_args()

        if UserModel.find_by_login(dados['login']):
            return {"message":"The login '{}' already exists.".format(dados['login'])}

        user = UserModel(**dados)
        user.save_user()
        return {'message:':"user cread successfully!"}, 201 #Created