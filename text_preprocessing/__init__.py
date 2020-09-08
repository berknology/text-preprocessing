__version__ = '0.0.9'

from .text_preprocessing import (to_lower, to_upper, remove_number, remove_itemized_bullet_and_numbering, remove_url,
                                 remove_punctuation, remove_special_character, keep_alpha_numeric, remove_whitespace,
                                 expand_contraction, normalize_unicode, remove_stopword, remove_email,
                                 remove_phone_number, remove_ssn, remove_credit_card_number, remove_name,
                                 check_spelling, tokenize_word, tokenize_sentence, stem_word, lemmatize_word,
                                 substitute_token, preprocess_text)
