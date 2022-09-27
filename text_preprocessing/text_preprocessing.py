# Standard libraries
import os
import re
import string
import logging
import csv
from pathlib import Path
from functools import wraps
from unicodedata import normalize
from typing import List, Optional, Union, Callable

# Third party libraries
import contractions
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, PunktSentenceTokenizer
from nltk.stem import PorterStemmer, SnowballStemmer, LancasterStemmer, WordNetLemmatizer
from spellchecker import SpellChecker
from names_dataset import NameDataset

nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet=True)
nltk.download('punkt', quiet=True)
nltk.download('omw-1.4')

_CUSTOM_SUB_CSV_FILE_PATH = os.path.join(os.path.dirname(__file__), 'data/custom_substitutions.csv')
_IGNORE_SPELLCHECK_WORD_FILE_PATH = os.path.join(os.path.dirname(__file__), 'data/ignore_spellcheck_words.txt')

LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)


def _return_empty_string_for_invalid_input(func):
    """ Return empty string if the input is None or empty """
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'input_text' in kwargs:
            input_text = kwargs['input_text']
        else:
            try:
                input_text = args[0]
            except IndexError as e:
                LOGGER.exception('No appropriate positional argument is provide.')
                raise e
        if input_text is None or len(input_text) == 0:
            return ''
        else:
            return func(*args, **kwargs)
    return wrapper


def _return_empty_list_for_invalid_input(func):
    """ Return empty list if the input is None or empty """
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'input_text_or_list' in kwargs:
            input_text_or_list = kwargs['input_text_or_list']
        else:
            try:
                input_text_or_list = args[0]
            except IndexError as e:
                LOGGER.exception('No appropriate positional argument is provide.')
                raise e
        if input_text_or_list is None or len(input_text_or_list) == 0:
            return []
        else:
            return func(*args, **kwargs)
    return wrapper


@_return_empty_string_for_invalid_input
def to_lower(input_text: str) -> str:
    """ Convert input text to lower case """
    return input_text.lower()


@_return_empty_string_for_invalid_input
def to_upper(input_text: str) -> str:
    """ Convert input text to upper case """
    return input_text.upper()


@_return_empty_string_for_invalid_input
def remove_number(input_text: str) -> str:
    """ Remove number in the input text """
    processed_text = re.sub('\d+', '', input_text)
    return processed_text


@_return_empty_string_for_invalid_input
def remove_itemized_bullet_and_numbering(input_text: str) -> str:
    """ Remove bullets or numbering in itemized input """
    processed_text = re.sub('[(\s][0-9a-zA-Z][.)]\s+|[(\s][ivxIVX]+[.)]\s+', ' ', input_text)
    return processed_text


@_return_empty_string_for_invalid_input
def remove_url(input_text: str) -> str:
    """ Remove url in the input text """
    return re.sub('(www|http)\S+', '', input_text)


@_return_empty_string_for_invalid_input
def remove_punctuation(input_text: str, punctuations: Optional[str] = None) -> str:
    """
    Removes all punctuations from a string, as defined by string.punctuation or a custom list.
    For reference, Python's string.punctuation is equivalent to '!"#$%&\'()*+,-./:;<=>?@[\\]^_{|}~'
    """
    if punctuations is None:
        punctuations = string.punctuation
    processed_text = input_text.translate(str.maketrans('', '', punctuations))
    return processed_text


@_return_empty_string_for_invalid_input
def remove_special_character(input_text: str, special_characters: Optional[str] = None) -> str:
    """ Removes special characters """
    if special_characters is None:
        # TODO: add more special characters
        special_characters = 'å¼«¥ª°©ð±§µæ¹¢³¿®ä£'
    processed_text = input_text.translate(str.maketrans('', '', special_characters))
    return processed_text


@_return_empty_string_for_invalid_input
def keep_alpha_numeric(input_text: str) -> str:
    """ Remove any character except alphanumeric characters """
    return ''.join(c for c in input_text if c.isalnum())


@_return_empty_string_for_invalid_input
def remove_whitespace(input_text: str, remove_duplicate_whitespace: bool = True) -> str:
    """ Removes leading, trailing, and (optionally) duplicated whitespace """
    if remove_duplicate_whitespace:
        return ' '.join(re.split('\s+', input_text.strip(), flags=re.UNICODE))
    return input_text.strip()


@_return_empty_string_for_invalid_input
def expand_contraction(input_text: str) -> str:
    """ Expand contractions in input text """
    return contractions.fix(input_text)


@_return_empty_string_for_invalid_input
def normalize_unicode(input_text: str) -> str:
    """ Normalize unicode data to remove umlauts, and accents, etc. """
    processed_tokens = normalize('NFKD', input_text).encode('ASCII', 'ignore').decode('utf8')
    return processed_tokens


@_return_empty_list_for_invalid_input
def remove_stopword(input_text_or_list: Union[str, List[str]], stop_words: Optional[set] = None) -> List[str]:
    """ Remove stop words """

    if stop_words is None:
        stop_words = set(stopwords.words('english'))
    if isinstance(stop_words, list):
        stop_words = set(stop_words)
    if isinstance(input_text_or_list, str):
        tokens = word_tokenize(input_text_or_list)
        processed_tokens = [token for token in tokens if token not in stop_words]
    else:
        processed_tokens = [token for token in input_text_or_list
                            if (token not in stop_words and token is not None and len(token) > 0)]
    return processed_tokens


@_return_empty_string_for_invalid_input
def remove_email(input_text: str) -> str:
    """ Remove email in the input text """
    regex_pattern = '[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}'
    return re.sub(regex_pattern, '', input_text)


@_return_empty_string_for_invalid_input
def remove_phone_number(input_text: str) -> str:
    """ Remove phone number in the input text """
    regex_pattern = '(?:\+?(\d{1,3}))?[-. (]*(\d{3})[-. )]*(\d{3})[-. ]*(\d{4})(?: *x(\d+))?'
    return re.sub(regex_pattern, '', input_text)


@_return_empty_string_for_invalid_input
def remove_ssn(input_text: str) -> str:
    """ Remove social security number in the input text """
    regex_pattern = '(?!219-09-9999|078-05-1120)(?!666|000|9\d{2})\d{3}-(?!00)\d{2}-(?!0{4})\d{4}|(' \
                    '?!219099999|078051120)(?!666|000|9\d{2})\d{3}(?!00)\d{2}(?!0{4})\d{4}'
    return re.sub(regex_pattern, '', input_text)


@_return_empty_string_for_invalid_input
def remove_credit_card_number(input_text: str) -> str:
    """ Remove credit card number in the input text """
    regex_pattern = '(4[0-9]{12}(?:[0-9]{3})?|(?:5[1-5][0-9]{2}|222[1-9]|22[3-9][0-9]|2[3-6][0-9]{2}|27[01][' \
                    '0-9]|2720)[0-9]{12}|3[47][0-9]{13}|3(?:0[0-5]|[68][0-9])[0-9]{11}|6(?:011|5[0-9]{2})[0-9]{12}|(' \
                    '?:2131|1800|35\d{3})\d{11})'
    return re.sub(regex_pattern, '', input_text)


@_return_empty_list_for_invalid_input
def remove_name(input_text_or_list: Union[str, List[str]]) -> List[str]:
    """ Remove name in the input text """
    name_searcher = NameDataset()
    if isinstance(input_text_or_list, str):
        tokens = word_tokenize(input_text_or_list)
        processed_tokens = [token for token in tokens
                            if (not name_searcher.search_first_name(token)) and
                               (not name_searcher.search_last_name(token))]
    else:
        processed_tokens = [token for token in input_text_or_list
                            if (not name_searcher.search_first_name(token)) and
                               (not name_searcher.search_last_name(token)) and token is not None and len(token) > 0]
    return processed_tokens


def check_spelling(input_text_or_list: Union[str, List[str]], lang='en',
                   ignore_word_file_path: Union[str, Path] = _IGNORE_SPELLCHECK_WORD_FILE_PATH) -> str:
    """ Check and correct spellings of the text list """
    if input_text_or_list is None or len(input_text_or_list) == 0:
        return ''
    spelling_checker = SpellChecker(language=lang, distance=1)
    # TODO: add acronyms into spell checker to ignore auto correction specified by _IGNORE_SPELLCHECK_WORD_FILE_PATH
    spelling_checker.word_frequency.load_text_file(ignore_word_file_path)
    if isinstance(input_text_or_list, str):
        if not input_text_or_list.islower():
            input_text_or_list = input_text_or_list.lower()
        tokens = word_tokenize(input_text_or_list)
    else:
        tokens = [token.lower() for token in input_text_or_list if token is not None and len(token) > 0]
    misspelled = spelling_checker.unknown(tokens)
    for word in misspelled:
        tokens[tokens.index(word)] = spelling_checker.correction(word)
    return ' '.join(tokens).strip()


def tokenize_word(input_text: str) -> List[str]:
    """ Converts a text into a list of word tokens """
    if input_text is None or len(input_text) == 0:
        return []
    return word_tokenize(input_text)


def tokenize_sentence(input_text: str) -> List[str]:
    """ Converts a text into a list of sentence tokens """
    if input_text is None or len(input_text) == 0:
        return []
    tokenizer = PunktSentenceTokenizer()
    return tokenizer.tokenize(input_text)


@_return_empty_list_for_invalid_input
def stem_word(input_text_or_list: Union[str, List[str]],
              stemmer: Optional[Union[PorterStemmer, SnowballStemmer, LancasterStemmer]] = None
              ) -> List[str]:
    """ Stem each token in a text """
    if stemmer is None:
        stemmer = PorterStemmer()
    if isinstance(input_text_or_list, str):
        tokens = word_tokenize(input_text_or_list)
        processed_tokens = [stemmer.stem(token) for token in tokens]
    else:
        processed_tokens = [stemmer.stem(token) for token in input_text_or_list if token is not None and len(token) > 0]
    return processed_tokens


@_return_empty_list_for_invalid_input
def lemmatize_word(input_text_or_list: Union[str, List[str]],
                   lemmatizer: Optional[WordNetLemmatizer] = None
                   ) -> List[str]:
    """ Lemmatize each token in a text by finding its base form """
    if lemmatizer is None:
        lemmatizer = WordNetLemmatizer()
    if isinstance(input_text_or_list, str):
        tokens = word_tokenize(input_text_or_list)
        processed_tokens = [lemmatizer.lemmatize(token) for token in tokens]
    else:
        processed_tokens = [lemmatizer.lemmatize(token)
                            for token in input_text_or_list if token is not None and len(token) > 0]
    return processed_tokens


def substitute_token(token_list: List[str], sub_dict: Optional[dict] = None) -> List[str]:
    """ Substitute each token by another token, e.g., 'vs' -> 'versus' """
    # TODO: add more custom substitutions in the csv file specified by _CUSTOM_SUB_CSV_FILE_PATH
    if token_list is None or len(token_list) == 0:
        return []
    if sub_dict is None:
        with open(_CUSTOM_SUB_CSV_FILE_PATH, 'r') as f:
            csv_file = csv.reader(f)
            sub_dict = dict(csv_file)
    processed_tokens = list()
    for token in token_list:
        if token in sub_dict:
            processed_tokens.append(sub_dict[token])
        else:
            processed_tokens.append(token)
    return processed_tokens


def preprocess_text(input_text: str, processing_function_list: Optional[List[Callable]] = None) -> str:
    """ Preprocess an input text by executing a series of preprocessing functions specified in functions list """
    if processing_function_list is None:
        processing_function_list = [to_lower,
                                    remove_url,
                                    remove_email,
                                    remove_phone_number,
                                    remove_itemized_bullet_and_numbering,
                                    expand_contraction,
                                    check_spelling,
                                    remove_special_character,
                                    remove_punctuation,
                                    remove_whitespace,
                                    normalize_unicode,
                                    remove_stopword,
                                    remove_name,
                                    substitute_token,
                                    lemmatize_word]
    for func in processing_function_list:
        input_text = func(input_text)
    if isinstance(input_text, str):
        processed_text = input_text
    else:
        processed_text = ' '.join(input_text)
    return processed_text


if __name__ == '__main__':
    text_to_process = 'Helllo, I am John Doe!!! My email is john.doe@email.com. Visit our website www.johndoe.com'
    preprocessed_text = preprocess_text(text_to_process)
    print(preprocessed_text)

    preprocess_functions = [to_lower, remove_email, remove_url, remove_punctuation, lemmatize_word]
    preprocessed_text = preprocess_text(text_to_process, preprocess_functions)
    print(preprocessed_text)
