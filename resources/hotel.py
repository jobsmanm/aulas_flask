from flask_restful import Resource, reqparse
from models.hotel import HotelModel

class Hoteis(Resource):
    def get(self):
        return {'hoteis':[hotel.json() for hotel in HotelModel.query.all()]}, #select * from hotel
    

class Hotel(Resource):
    
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome', type=str, required=True, help="The 'nome' field cannot be made blank.")
    argumentos.add_argument('estrelas', type=float, required=True, help="The 'estrelas' field cannot be made blank.")
    argumentos.add_argument('diaria', type=float)
    argumentos.add_argument('cidade', type=str, required=True, help="The 'cidade' field cannot be made blank.")
    
    def get(self, hotel_id):
        
        hotel = HotelModel.find_hotel(hotel_id)
        if hotel:
            return hotel.json()
        
        return {"message":"Hotel not found"}, 404 #not found

    def post(self, hotel_id):
        if HotelModel.find_hotel(hotel_id):
            return {"message":"Hotel id '{}' already exits.".format(hotel_id)}, 400 #Bad request

        dados = Hotel.argumentos.parse_args()
        hotel = HotelModel(hotel_id, **dados)
        try:
            hotel.save_hotel()
        except:
            return {'message': 'A internal error ocurred trying to save hotel.'}, 500 #Internal Server Error
        return hotel.json()

    def put(self, hotel_id):
        dados = Hotel.argumentos.parse_args()
        

        #novo_hotel = {'hotel_id':hotel_id, **dados}
        hotel = HotelModel.find_hotel(hotel_id)

        if hotel:
            hotel.update_hotel(**dados)
            hotel.save_hotel()
            return hotel.json(), 200

        hotel = HotelModel(hotel_id, **dados) #Instancia Hotel
        try:
            hotel.save_hotel()
        except:
            return {'message': 'A internal error ocurred trying to save hotel.'}, 500 #Internal Server Error
        return hotel.json(), 201 #Created

    def delete(self, hotel_id):
        hotel = HotelModel.find_hotel(hotel_id)
        if hotel:
            try:
                hotel.delete_hotel()
            except:
                return {'message': 'A internal error ocurred trying to delete hotel.'}, 500 #Internal Server Error
            return {'message': 'Hotel deleted!'}, 201 

        return {'message': 'Hotel not found!'}