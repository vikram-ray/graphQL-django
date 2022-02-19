
install:
	pip install -r requirements.txt

docker-build: install
	docker build . -t "dj-movies"
