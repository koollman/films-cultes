#!/usr/bin/env python

import codecs

films=file("films.txt")

base_template=u"""
title: "%(titre)s"
category: films
tags: [%(genre)s]
realisateur: %(realisateur)s
sortable: %(slug)s
---
%(description)s

"""

import re
from unicodedata import normalize

# From http://flask.pocoo.org/snippets/5/
_punct_re = re.compile(r'[\t !"#$%&()*\-/<=>?@\[\\\]^_`{|},.:]+')
def slugify(text, delim=u'-'):
    """
    Generates a slug that will only use ASCII, be all lowercase, have no
    spaces, and otherwise be nice for filenames, identifiers, and urls.
    """
    result = []
    for word in _punct_re.split(text.lower()):
        word = normalize('NFKD', word).encode('ascii','ignore').replace("'", "")
        if word:
            result.append(word)

    result = delim.join(result)
    if result[0] == '-':
        result = result[1:]
    if result[-1] == '-':
        result = result[:-1]

    return unicode(result)

header=films.readline()
header=map(lambda x: x.strip().lower().decode('utf8'), header.split('#'))
base={}
for name in header:
    base[name]=''

stem_re=re.compile(r"^(The|Le|La|Les|L')\b", re.IGNORECASE)

for line in films:
    film=base.copy()
    values=line.strip().split('#')
    values=map(lambda x: x.strip().decode('utf8'), values)

    film.update(dict(zip(header, values)))

    if film['nom pour classement']:
        name=film['nom pour classement']
    else:
        name=film['titre']

    filename=slugify(name)+'.txt'

    film['slug']=slugify(stem_re.sub('', name))

    print film['titre']
    print filename, film
    print base_template % film

    out=codecs.open('content/films/' + filename, 'w', 'utf8')
    out.write(base_template % film)
    out.close()

