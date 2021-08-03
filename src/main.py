from pymongo import MongoClient
import pprint

connection_string = 'mongodb://mongoadmin:secret@localhost:27017/admin?authSource=admin&authMechanism=SCRAM-SHA-1'

if __name__ == '__main__':
    mongo = MongoClient(connection_string)

    database = mongo['my-database']

    cliente = {
        'nome': 'Marcelo Ikejima',
        'empresa': '4i',
        'animais_estimacao': [
            {'nome': 'Fred', 'tipo': 'Cachorro'},
            {'nome': 'Pan', 'tipo': 'Cachorro'}]
    }

    cliente_collection = database.get_collection('cliente')

    result = cliente_collection.insert_one(cliente)
    pprint.pprint(result)

    doc = cliente_collection.find_one({'_id': result.inserted_id})
    pprint.pprint(doc)

    clientes = [
        {
            'nome': 'Gabriel Claret',
            'empresa': '4i',
            'hobbies': ['Video Game']
        },
        {
            'nome': 'Maria Eduarda',
            'empresa': '4i',
        },
        {
            'nome': 'Henrique Lang',
            'empresa': '4i',
            'idiomas': ['Portugues']
        },
    ]

    for _cliente in clientes:
        cliente_collection.insert_one(_cliente)

    docs = cliente_collection.find({})

    for doc in docs:
        pprint.pprint(doc['nome'])
