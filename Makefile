mongo:
	docker pull mongo:4.0
	docker stop mongo-demo || true
	docker rm mongo-demo || true
	docker run --name mongo-demo -e MONGO_INITDB_ROOT_USERNAME=mongoadmin -e MONGO_INITDB_ROOT_PASSWORD=secret -p 27017:27017 mongo