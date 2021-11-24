from sql_alchemy import banco

#banco.Model serve para declarar que a classe é do tipo tabela do BD
class HotelModel(banco.Model):
    __tablename__ = 'hoteis'

    hotel_id = banco.Column(banco.String, primary_key=True)
    nome = banco.Column(banco.String(80))
    estrelas = banco.Column(banco.Float(precision=1))
    diaria = banco.Column(banco.Float(precision=2))
    cidade = banco.Column(banco.String(80))

    def __init__(self, hotel_id, nome, estrelas, diaria, cidade):
        self.hotel_id = hotel_id
        self.nome = nome
        self.estrelas = estrelas
        self.diaria = diaria
        self.cidade = cidade

    def json(self): #a função json converte o proprio objeto em dicionario e que vai ser convertido em json posteriormente
        return {
            "hotel_id": self.hotel_id,
            "nome": self.nome,
            "estrelas": self.estrelas,
            "diaria" : self.diaria,
            "cidade": self.cidade
        } 
    
    @classmethod
    def find_hotel(cls, hotel_id): #cls é abreviação da classe (palavra chave), seria o mesmo que escrever HotelModel

        hotel = cls.query.filter_by(hotel_id=hotel_id).first() #É um select na tabela de hoteis
        if hotel:
            return hotel
        return None

    def save_hotel(self):
        banco.session.add(self)
        banco.session.commit()

    def update_hotel(self, nome, estrelas, diaria, cidade):
        self.nome = nome
        self.estrelas = estrelas
        self.diaria = diaria
        self.cidade = cidade

    def delete_hotel(self):
        banco.session.delete(self)
        banco.session.commit()