import googletrans

detector = googletrans.Translator()
languages = googletrans.LANGUAGES  # dictionary of language codes and their names


def detect_language(sample_text):
    """This receives a sample of the language to be detected and 
    returns the with the name of the detected language.
    """
    language_code = detector.detect(sample_text).lang
    return languages[language_code]

