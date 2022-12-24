import yake


def get_keywords(text):
    language = "ru"
    max_ngram_size = 1
    deduplication_threshold = 0.9
    numOfKeywords = 3
    custom_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_threshold,
                                                top=numOfKeywords, features=None)
    keywords = custom_kw_extractor.extract_keywords(text)
    words = [x[0] for x in keywords]
    return ','.join(words)
