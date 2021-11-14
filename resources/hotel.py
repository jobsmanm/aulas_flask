from flask_restful import Resource, reqparse

hoteis = [
    {
        "hotel_id": "alpha",
        "nome": "Alpha Hotel",
        "estrelas": 4.3,
        "diaria": 301.50,
        "cidade": "Rio de Janeiro"
    },
    {
        "hotel_id": "nobre",
        "nome": "Nobre Hotel",
        "estrelas": 3.2,
        "diaria": 275.90,
        "cidade": "Rio de Janeiro"
    },
    {
        "hotel_id": "corinto",
        "nome": "Corinto Hotel",
        "estrelas": 4.8,
        "diaria": 480.50,
        "cidade": "São Paulo"
    },
]
class Hoteis(Resource):
    def get(self):
        return {"hoteis":hoteis}

class Hotel(Resource):

    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome')
    argumentos.add_argument('estrelas')
    argumentos.add_argument('diaria')
    argumentos.add_argument('cidade')

    def find_hotel(hotel_id):
        for hotel in hoteis:
            if hotel["hotel_id"] == hotel_id:
                return hotel
        return None

    def get(self, hotel_id):
        hotel = Hotel.find_hotel(hotel_id)
        if hotel:
            return hotel

        return {"message":"Hotel not found"}, 404 #not found

    def post(self, hotel_id):

        dados = Hotel.argumentos.parse_args()

        novo_hotel = {
            'hotel_id': hotel_id,
            'nome': dados['nome'],
            'estrelas': dados['estrelas'],
            'diaria': dados['diaria'],
            'cidade': dados['cidade']
        }

        hoteis.append(novo_hotel)
        return novo_hotel, 200

    def put(self, hotel_id):
        dados = Hotel.argumentos.parse_args()
        novo_hotel = {'hotel_id':hotel_id, **dados}
        hotel = Hotel.find_hotel(hotel_id)

        if hotel:
            hotel.update(novo_hotel)
            return novo_hotel, 200
        
        hoteis.append(novo_hotel)
        return novo_hotel, 201 #Created

    def delete(self, hotel_id):
        pass