all: output/index.html

output/index.html: .films content/*.mkd templates/*.html
	wok

.films: films.txt
	rm content/films/*.txt
	./getfilms.py
	touch .films
