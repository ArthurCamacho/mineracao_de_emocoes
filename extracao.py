import nltk

def linha_separadora():
    print('--------------------------------------------------------------------------------------')

# Base de dados onde as frases são os PREVISORES e as emoções sao as CLASSES (META)
# Usada para fazer a classificação de novos valores (inputs)
base = [('eu sou admirada por muitos','alegria'),
        ('me sinto completamente amado','alegria'),
        ('amar e maravilhoso','alegria'),
        ('estou me sentindo muito animado novamente','alegria'),
        ('eu estou muito bem hoje','alegria'),
        ('que belo dia para dirigir um carro novo','alegria'),
        ('o dia está muito bonito','alegria'),
        ('estou contente com o resultado do teste que fiz no dia de ontem','alegria'),
        ('o amor e lindo','alegria'),
        ('nossa amizade e amor vai durar para sempre', 'alegria'),
        ('estou amedrontado', 'medo'),
        ('ele esta me ameacando a dias', 'medo'),
        ('isso me deixa apavorada', 'medo'),
        ('este lugar e apavorante', 'medo'),
        ('se perdermos outro jogo seremos eliminados e isso me deixa com pavor', 'medo'),
        ('tome cuidado com o lobisomem', 'medo'),
        ('se eles descobrirem estamos encrencados', 'medo'),
        ('estou tremendo de medo', 'medo'),
        ('eu tenho muito medo dele', 'medo'),
        ('estou com medo do resultado dos meus testes', 'medo')]

# Stopwords são palavras que não ajudam para identificar qual a classe que o caso receberá
stopwords = ['a', 'agora', 'algum', 'alguma', 'aquele', 'aqueles', 'de', 'deu', 'do', 'e', 'estou', 'esta', 'esta',
             'ir', 'meu', 'muito', 'mesmo', 'no', 'nossa', 'o', 'outro', 'para', 'que', 'sem', 'talvez', 'tem', 'tendo',
             'tenha', 'teve', 'tive', 'todo', 'um', 'uma', 'umas', 'uns', 'vou']

# Recebe a lista de stopwords da lib nltk
stopwordsnltk = nltk.corpus.stopwords.words('portuguese')


def remove_stopwords(texto):
    """Texto - lista de sets - frases classificadas //
       A função remove das frases as stopwords contidas em cada uma delas"""
    frases = []
    for palavras, emocao in texto:
        sem_stop = [palavra for palavra in palavras.split() if palavra not in stopwordsnltk]
        frases.append((sem_stop, emocao))
    return frases


def aplica_stemmer(texto):
    """Função que aplica o algoritmo de stemmer para remover os radicais das palavras e deixar somente o nucleo"""    
    
    # Cria um objeto STEMMER que sera usado para remover os radicais
    # IMPORTANTE!!!
    # O stem usado vai depender do que deve ser tratado, por exemplo
    # Esse stem (RSLPStemmer) é compativel com portgues, por isso usamos ele
    stemmer = nltk.stem.RSLPStemmer()
    frases_stemmadas = []
    for frase, emocao in texto:
        # Cria uma lista com as palavras da frase após serem processessadas pelo stemmer
        # Remove também as stopwords
        pos_stemming = [str(stemmer.stem(palavra)) for palavra in frase.split() if palavra not in stopwordsnltk]
        # Acrescenta na lista um set contendo as palavras stemmadas e a emocao que corresponde a elas
        frases_stemmadas.append((pos_stemming, emocao))

    return frases_stemmadas


def busca_palavras(frases):
    """Recebe como parametro uma lista que contenha:
       Index 0 = uma tuple com as plavras restantes da frase
       Index 1 = a emoção que corresponde à frase //
       Deve retornar uma lista contendo todas as palavras presentes na 'frases' """

    todas_palavras = []
    for palavras, emocao in frases:
        todas_palavras.extend(palavras)
    
    return todas_palavras


def frequencia(lista_palavras):
    """Recebe uma lista de plavras e então gera um dict beaseado na quantidade de aparições"""
    freq_palavras = nltk.FreqDist(lista_palavras)

    return freq_palavras


def busca_palavras_unicas(dict_palavras_freq):
    """Recebe um dicionario que contenha palavras (chave) e frequencia (valor)
       retorna uma lista com todas as palavras do dict (chaves)"""

    unicas = dict_palavras_freq.keys()

    return(unicas)

sem_stop = remove_stopwords(base)
print(sem_stop)
linha_separadora()
base_stemmada_sem_stopwords = aplica_stemmer(base)
print(base_stemmada_sem_stopwords)
linha_separadora()
todas_palavras_stemmadas = busca_palavras(base_stemmada_sem_stopwords)
print(todas_palavras_stemmadas)
linha_separadora()
frequencia_palavras_stemmadas = frequencia(todas_palavras_stemmadas)
print(frequencia_palavras_stemmadas.most_common()) # O most so serve para exibir na ordem decrescente de frequenica, sem o metodo retorna objeto
linha_separadora()
palavras_unicas_stemmadas = busca_palavras_unicas(frequencia_palavras_stemmadas)
print(palavras_unicas_stemmadas)

