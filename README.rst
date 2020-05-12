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
* convert to lower case
* convert to upper case
* keep only alphabetic and numerical characters
* check and correct spellings
* expand contractions
* remove URL
* remove name
* remove email
* remove phone number
* remove SSN
* remove credit card number
* remove numbers
* remove special characters
* remove punctuations
* remove extra whitespace
* normalize unicode (e.g., Café -> Cafe)
* remove stop words
* substitute custom word (e.g., msft -> Microsoft)
* stem words
* lemmatize words
