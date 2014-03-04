all: output/index.html

output/index.html: .films content/*.mkd templates/*.html
	wok

.films: films.txt getfilms.py
	rm -f content/films/*.txt
	./getfilms.py
	touch .films
