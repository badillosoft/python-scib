from pymongo import MongoClient

client = MongoClient()

db = client.cic

db.usuarios.insert_many([
	{
		"usuario": "pepe",
		"clave": "123"
	},
	{
		"usuario": "batman",
		"clave": "robin"
	},
	{
		"usuario": "ax9000",
		"clave": "xa0009"
	}
])

client.close()

print "Usuarios creados"