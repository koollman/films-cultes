#!/usr/bin/env python

films=file("films.txt")

base_template="""
title: "%s"
category: films
tag: 
---
%s

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
        word = normalize('NFKD', unicode(word, errors='ignore')).encode('ascii','ignore').replace("'", "")
        if word:
            result.append(word)

    result = delim.join(result)
    if result[0] == '-':
        result = result[1:]
    if result[-1] == '-':
        result = result[:-1]

    return unicode(result)

for line in films:
    line=line.strip().split('#')
    if len(line) == 1:
        comment=''
    else:
        comment=line[1].strip()
    title=line[0].strip()
    filename=slugify(title)+'.txt'

    print title
    print filename
    print '--'
    print comment
    print


    out=file('content/films/' + filename, 'w')
    out.write(base_template % (title, comment))
    out.close()

