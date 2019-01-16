import spacy;

# main
if __name__ == '__main__':
    nlp=spacy.load('fr_core_news_md')
    doc=nlp(u"bonjour je m'appelle Laurent Leturgez. Je suis né le 06/02/1978 et j'habite près de Lille")
    for token in doc:
        print("{0}\t{1}".format(token.text, token.shape_))
    for ent in doc.ents:
        print (ent.text, ent.label_, )