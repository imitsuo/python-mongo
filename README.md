# python-mongo

#### Robomongo
Faça o download do Robomongo https://robomongo.org/

 
 Inicie o Mongo no container com o comando:
 ```
 make mongo
 ```

Crie o virtualenv:
 ```
 virtualenv venv -p python3
 source venv/bin/activate
 pip install -r requirements.txt
 ```

 ## Differences:

 ### Predefined Schema ==> Schemaless (on save)
 ### Tables ==> Collections
 
 ### Normalization ==> Documents
Table: Clients
- id
- name

Table: Phones
- id
- number
- client_id

Document: Clients
{
    "id": ,
    "name": ,
    "phones": [
        {
            "id": ,
            "number": 
        }
    ]
}

### "Sql queries" x "Functions"

```db.inventory.find( { status: "D" } )```

```SELECT * FROM inventory WHERE status = "D"```