==================================================
Text preprocessing for Natural Language Processing
==================================================

A python package for text preprocessing task in natural language processing.

Usage
-----
To use this text preprocessing package,

.. code-block:: python

    from text_preprocessing import preprocess_text

    # Preprocess text using default preprocess functions in the pipeline
    text_to_process = 'Helllo, I am John Doe!!! My email is john.doe@email.com. Visit our website www.johndoe.com'
    preprocessed_text = preprocess_text(text_to_process)
    print(preprocessed_text)

    # Preprocess text using custom preprocess functions in the pipeline
    preprocess_functions = [to_lower, remove_email, remove_url, remove_punctuations, lemmatize_word]
    preprocessed_text = preprocess_text(text_to_process, preprocess_functions)
    print(preprocessed_text)


Features
--------

.. csv-table::
   :header: "Feature", "Function"
   :widths: 50, 35

    "convert to lower case", "to_lower"
    "convert to upper case", "to_upper"
    "keep only alphabetic and numerical characters", "keep_alpha_numeric"
    "check and correct spellings", "check_spelling"
    "expand contractions", "expand_contraction"
    "remove URLs", "remove_url"
    "remove names", "remove_name"
    "remove emails", "remove_email"
    "remove phone numbers", "remove_phone_number"
    "remove SSNs", "remove_ssn"
    "remove credit card numbers", "remove_credit_card_number"
    "remove numbers", "remove_number"
    "remove special characters", "remove_special_character"
    "remove punctuations", "remove_punctuation"
    "remove extra whitespace", "remove_whitespace"
    "normalize unicode (e.g., Café -> Cafe)", "normalize_unicode"
    "remove stop words", "remove_stopword"
    "tokenize words", "tokenize_word"
    "tokenize sentences", "tokenize_sentence"
    "substitute custom words (e.g., msft -> Microsoft)", "substitute_token"
    "stem words", "stem_word"
    "lemmatize words", "lemmatize_word"