# Standard libraries
from unittest import TestCase
from unittest.mock import patch, MagicMock

# Project code
from text_preprocessing import (to_lower, to_upper, remove_number, remove_url, remove_punctuations,
                                remove_special_characters, keep_alpha_numeric, remove_whitespace, expand_contractions,
                                normalize_unicode, remove_stopwords, remove_email, remove_phone_number, remove_ssn,
                                remove_credit_card_number, remove_names, check_spelling, substitute_token)
from text_preprocessing import preprocess_text


class TestTextPreprocessing(TestCase):

    def test_to_lower(self):
        # Setup
        input_text = 'HellO'
        expected_output = 'hello'
        # Actual call
        output_text = to_lower(input_text)
        # Asserts
        self.assertEqual(output_text, expected_output)

    def test_to_lower_lower_input(self):
        # Setup
        input_text = 'hello'
        expected_output = 'hello'
        # Actual call
        output_text = to_lower(input_text)
        # Asserts
        self.assertEqual(output_text, expected_output)

    def test_to_lower_upper_input(self):
        # Setup
        input_text = 'HELLO'
        expected_output = 'hello'
        # Actual call
        output_text = to_lower(input_text)
        # Asserts
        self.assertEqual(output_text, expected_output)

    def test_to_lower_none(self):
        # Setup
        input_text = None
        expected_output = ''
        # Actual call
        output_text = to_lower(input_text)
        # Asserts
        self.assertEqual(output_text, expected_output)

    def test_to_lower_empty_input(self):
        # Setup
        input_text = ''
        expected_output = ''
        # Actual call
        output_text = to_lower(input_text)
        # Asserts
        self.assertEqual(output_text, expected_output)

    def test_to_upper(self):
        # Setup
        input_text = 'HellO'
        expected_output = 'HELLO'
        # Actual call
        output_text = to_upper(input_text)
        # Asserts
        self.assertEqual(output_text, expected_output)

    def test_to_upper_lower_input(self):
        # Setup
        input_text = 'hello'
        expected_output = 'HELLO'
        # Actual call
        output_text = to_upper(input_text)
        # Asserts
        self.assertEqual(output_text, expected_output)

    def test_to_upper_upper_input(self):
        # Setup
        input_text = 'HELLO'
        expected_output = 'HELLO'
        # Actual call
        output_text = to_upper(input_text)
        # Asserts
        self.assertEqual(output_text, expected_output)

    def test_to_upper_none(self):
        # Setup
        input_text = None
        expected_output = ''
        # Actual call
        output_text = to_upper(input_text)
        # Asserts
        self.assertEqual(output_text, expected_output)

    def test_to_upper_empty_input(self):
        # Setup
        input_text = ''
        expected_output = ''
        # Actual call
        output_text = to_upper(input_text)
        # Asserts
        self.assertEqual(output_text, expected_output)

    def test_remove_number(self):
        # Setup
        input_text = 'HellO123'
        expected_output = 'HellO'
        # Actual call
        output_text = remove_number(input_text)
        # Asserts
        self.assertEqual(output_text, expected_output)

    def test_remove_number_no_number(self):
        # Setup
        input_text = 'HellO!.'
        expected_output = 'HellO!.'
        # Actual call
        output_text = remove_number(input_text)
        # Asserts
        self.assertEqual(output_text, expected_output)

    def test_remove_number_all_number(self):
        # Setup
        input_text = '987123'
        expected_output = ''
        # Actual call
        output_text = remove_number(input_text)
        # Asserts
        self.assertEqual(output_text, expected_output)

    def test_remove_number_none(self):
        # Setup
        input_text = None
        expected_output = ''
        # Actual call
        output_text = remove_number(input_text)
        # Asserts
        self.assertEqual(output_text, expected_output)

    def test_remove_number_empty_input(self):
        # Setup
        input_text = ''
        expected_output = ''
        # Actual call
        output_text = remove_number(input_text)
        # Asserts
        self.assertEqual(output_text, expected_output)

    def test_remove_url(self):
        # Setup
        input_text = 'my address is www.microsoft.com https://www.microsoft.com'
        expected_output = 'my address is  '
        # Actual call
        output_text = remove_url(input_text)
        # Asserts
        self.assertEqual(output_text, expected_output)

    def test_remove_url_no_url(self):
        # Setup
        input_text = 'my address is www.microsoft.com https://www.microsoft.com'
        expected_output = 'my address is  '
        # Actual call
        output_text = remove_url(input_text)
        # Asserts
        self.assertEqual(output_text, expected_output)

    def test_remove_url_all_url(self):
        # Setup
        input_text = 'www.microsoft.com https://www.microsoft.com'
        expected_output = ' '
        # Actual call
        output_text = remove_url(input_text)
        # Asserts
        self.assertEqual(output_text, expected_output)

    def test_remove_url_none(self):
        # Setup
        input_text = None
        expected_output = ''
        # Actual call
        output_text = remove_url(input_text)
        # Asserts
        self.assertEqual(output_text, expected_output)

    def test_remove_url_empty_input(self):
        # Setup
        input_text = ''
        expected_output = ''
        # Actual call
        output_text = remove_url(input_text)
        # Asserts
        self.assertEqual(output_text, expected_output)

    def test_remove_punctuations(self):
        # Setup
        input_text = 'Hello!!! Welcome.'
        expected_output = 'Hello Welcome'
        # Actual call
        output_text = remove_punctuations(input_text)
        # Asserts
        self.assertEqual(output_text, expected_output)

    def test_remove_punctuations_no_punctuations(self):
        # Setup
        input_text = 'Hello world'
        expected_output = 'Hello world'
        # Actual call
        output_text = remove_punctuations(input_text)
        # Asserts
        self.assertEqual(output_text, expected_output)

    def test_remove_punctuations_all_punctuations(self):
        # Setup
        input_text = '!"#$%&\'()*+,-./:;<=>?@[\\]^_{|}~'
        expected_output = ''
        # Actual call
        output_text = remove_punctuations(input_text)
        # Asserts
        self.assertEqual(output_text, expected_output)

    def test_remove_punctuations_none(self):
        # Setup
        input_text = None
        expected_output = ''
        # Actual call
        output_text = remove_punctuations(input_text)
        # Asserts
        self.assertEqual(output_text, expected_output)

    def test_remove_punctuations_empty_input(self):
        # Setup
        input_text = ''
        expected_output = ''
        # Actual call
        output_text = remove_punctuations(input_text)
        # Asserts
        self.assertEqual(output_text, expected_output)

    def test_remove_special_characters(self):
        # Setup
        input_text = 'Hello å¼« Welcome.'
        expected_output = 'Hello  Welcome.'
        # Actual call
        output_text = remove_special_characters(input_text)
        # Asserts
        self.assertEqual(output_text, expected_output)

    def test_remove_special_characters_no_punctuations(self):
        # Setup
        input_text = 'Hello world'
        expected_output = 'Hello world'
        # Actual call
        output_text = remove_special_characters(input_text)
        # Asserts
        self.assertEqual(output_text, expected_output)

    def test_remove_special_characters_all_punctuations(self):
        # Setup
        input_text = 'å¼«¥ª°©ð±§µæ¹¢³¿®ä£'
        expected_output = ''
        # Actual call
        output_text = remove_special_characters(input_text)
        # Asserts
        self.assertEqual(output_text, expected_output)

    def test_remove_special_characters_none(self):
        # Setup
        input_text = None
        expected_output = ''
        # Actual call
        output_text = remove_special_characters(input_text)
        # Asserts
        self.assertEqual(output_text, expected_output)

    def test_remove_special_characters_empty_input(self):
        # Setup
        input_text = ''
        expected_output = ''
        # Actual call
        output_text = remove_special_characters(input_text)
        # Asserts
        self.assertEqual(output_text, expected_output)

    def test_keep_alpha_numeric(self):
        # Setup
        input_text = 'Hello1 å¼«µæ Welcome2.'
        expected_output = 'Hello1å¼µæWelcome2'
        # Actual call
        output_text = keep_alpha_numeric(input_text)
        # Asserts
        self.assertEqual(output_text, expected_output)

    def test_keep_alpha_numeric_no_alphanumeric(self):
        # Setup
        input_text = '!.,*&^'
        expected_output = ''
        # Actual call
        output_text = keep_alpha_numeric(input_text)
        # Asserts
        self.assertEqual(output_text, expected_output)

    def test_keep_alpha_numeric_none(self):
        # Setup
        input_text = None
        expected_output = ''
        # Actual call
        output_text = keep_alpha_numeric(input_text)
        # Asserts
        self.assertEqual(output_text, expected_output)

    def test_keep_alpha_numeric_empty_input(self):
        # Setup
        input_text = ''
        expected_output = ''
        # Actual call
        output_text = keep_alpha_numeric(input_text)
        # Asserts
        self.assertEqual(output_text, expected_output)

    def test_remove_whitespace(self):
        # Setup
        input_text = ' Hello  Welcome. '
        expected_output = 'Hello Welcome.'
        # Actual call
        output_text = remove_whitespace(input_text)
        # Asserts
        self.assertEqual(output_text, expected_output)

    def test_remove_whitespace_strip(self):
        # Setup
        input_text = ' Hello  Welcome. '
        expected_output = 'Hello  Welcome.'
        # Actual call
        output_text = remove_whitespace(input_text, remove_duplicate_whitespace=False)
        # Asserts
        self.assertEqual(output_text, expected_output)

    def test_remove_whitespace_no_whitespace(self):
        # Setup
        input_text = 'Helloworld...'
        expected_output = 'Helloworld...'
        # Actual call
        output_text = remove_whitespace(input_text)
        # Asserts
        self.assertEqual(output_text, expected_output)

    def test_remove_whitespace_all_whitespace(self):
        # Setup
        input_text = '   '
        expected_output = ''
        # Actual call
        output_text = remove_whitespace(input_text)
        # Asserts
        self.assertEqual(output_text, expected_output)

    def test_remove_whitespace_none(self):
        # Setup
        input_text = None
        expected_output = ''
        # Actual call
        output_text = remove_whitespace(input_text)
        # Asserts
        self.assertEqual(output_text, expected_output)

    def test_remove_whitespace_empty_input(self):
        # Setup
        input_text = ''
        expected_output = ''
        # Actual call
        output_text = remove_whitespace(input_text)
        # Asserts
        self.assertEqual(output_text, expected_output)

    def test_expand_contractions(self):
        # Setup
        input_text = "This isn't a test"
        expected_output = 'This is not a test'
        # Actual call
        output_text = expand_contractions(input_text)
        # Asserts
        self.assertEqual(output_text, expected_output)

    def test_expand_contractions_no_contractions(self):
        # Setup
        input_text = 'Hello world'
        expected_output = 'Hello world'
        # Actual call
        output_text = expand_contractions(input_text)
        # Asserts
        self.assertEqual(output_text, expected_output)

    def test_expand_contractions_all_contractions(self):
        # Setup
        input_text = "cannot isn't ain't couldn't"
        expected_output = 'cannot is not are not could not'
        # Actual call
        output_text = expand_contractions(input_text)
        # Asserts
        self.assertEqual(output_text, expected_output)

    def test_expand_contractions_none(self):
        # Setup
        input_text = None
        expected_output = ''
        # Actual call
        output_text = expand_contractions(input_text)
        # Asserts
        self.assertEqual(output_text, expected_output)

    def test_expand_contractions_empty_input(self):
        # Setup
        input_text = ''
        expected_output = ''
        # Actual call
        output_text = expand_contractions(input_text)
        # Asserts
        self.assertEqual(output_text, expected_output)

    def test_normalize_unicode(self):
        # Setup
        input_text = "I love this Café"
        expected_output = 'I love this Cafe'
        # Actual call
        output_text = normalize_unicode(input_text)
        # Asserts
        self.assertEqual(output_text, expected_output)

    def test_normalize_unicode_no_special_unicode(self):
        # Setup
        input_text = 'This is a test'
        expected_output = 'This is a test'
        # Actual call
        output_text = normalize_unicode(input_text)
        # Asserts
        self.assertEqual(output_text, expected_output)

    def test_normalize_unicode_all_special_unicode(self):
        # Setup
        input_text = 'áñó'
        expected_output = 'ano'
        # Actual call
        output_text = normalize_unicode(input_text)
        # Asserts
        self.assertEqual(output_text, expected_output)

    def test_normalize_unicode_none(self):
        # Setup
        input_text = None
        expected_output = ''
        # Actual call
        output_text = normalize_unicode(input_text)
        # Asserts
        self.assertEqual(output_text, expected_output)

    def test_normalize_unicode_empty_input(self):
        # Setup
        input_text = ''
        expected_output = ''
        # Actual call
        output_text = normalize_unicode(input_text)
        # Asserts
        self.assertEqual(output_text, expected_output)

    def test_remove_stopwords(self):
        # Setup
        input_text = "This is a test!"
        expected_output = ['This', 'test', '!']
        # Actual call
        output_text = remove_stopwords(input_text)
        # Asserts
        self.assertListEqual(output_text, expected_output)

    def test_remove_stopwords_no_stopwords(self):
        # Setup
        input_text = 'Hello World.'
        expected_output = ['Hello', 'World', '.']
        # Actual call
        output_text = remove_stopwords(input_text)
        # Asserts
        self.assertListEqual(output_text, expected_output)

    def test_remove_stopwords_all_stopwords(self):
        # Setup
        input_text = 'the a your my his her'
        expected_output = []
        # Actual call
        output_text = remove_stopwords(input_text)
        # Asserts
        self.assertListEqual(output_text, expected_output)

    def test_remove_stopwords_none(self):
        # Setup
        input_text = None
        expected_output = []
        # Actual call
        output_text = remove_stopwords(input_text)
        # Asserts
        self.assertListEqual(output_text, expected_output)

    def test_remove_stopwords_empty_input(self):
        # Setup
        input_text = ''
        expected_output = []
        # Actual call
        output_text = remove_stopwords(input_text)
        # Asserts
        self.assertListEqual(output_text, expected_output)

    def test_remove_email(self):
        # Setup
        input_text = "Please email me at john.doe@email.com."
        expected_output = "Please email me at ."
        # Actual call
        output_text = remove_email(input_text)
        # Asserts
        self.assertEqual(output_text, expected_output)

    def test_remove_email_no_email(self):
        # Setup
        input_text = "Please call me (425) 425-1234."
        expected_output = "Please call me (425) 425-1234."
        # Actual call
        output_text = remove_email(input_text)
        # Asserts
        self.assertEqual(output_text, expected_output)

    def test_remove_email_all_emails(self):
        # Setup
        input_text = 'john.doe@email.com, john.doe@microsoft.com, janedoe@gmail.com'
        expected_output = ', , '
        # Actual call
        output_text = remove_email(input_text)
        # Asserts
        self.assertEqual(output_text, expected_output)

    def test_remove_email_none(self):
        # Setup
        input_text = None
        expected_output = ''
        # Actual call
        output_text = remove_email(input_text)
        # Asserts
        self.assertEqual(output_text, expected_output)

    def test_remove_email_empty_input(self):
        # Setup
        input_text = ''
        expected_output = ''
        # Actual call
        output_text = remove_email(input_text)
        # Asserts
        self.assertEqual(output_text, expected_output)

    def test_remove_phone_number(self):
        # Setup
        input_text = "Please call me at (425) 538-0116."
        expected_output = "Please call me at."
        # Actual call
        output_text = remove_phone_number(input_text)
        # Asserts
        self.assertEqual(output_text, expected_output)

    def test_remove_phone_number_no_phone(self):
        # Setup
        input_text = "Please email me"
        expected_output = "Please email me"
        # Actual call
        output_text = remove_phone_number(input_text)
        # Asserts
        self.assertEqual(output_text, expected_output)

    def test_remove_phone_number_all_phones(self):
        # Setup
        input_text = '(425) 538-1234, (425)5381234, 4255381234 425-538-1234, 425.538.1234, +1 425-538-1234'
        expected_output = ',,,, '
        # Actual call
        output_text = remove_phone_number(input_text)
        # Asserts
        self.assertEqual(output_text, expected_output)

    def test_remove_phone_number_none(self):
        # Setup
        input_text = None
        expected_output = ''
        # Actual call
        output_text = remove_phone_number(input_text)
        # Asserts
        self.assertEqual(output_text, expected_output)

    def test_remove_phone_number_empty_input(self):
        # Setup
        input_text = ''
        expected_output = ''
        # Actual call
        output_text = remove_phone_number(input_text)
        # Asserts
        self.assertEqual(output_text, expected_output)

    def test_remove_ssn(self):
        # Setup
        input_text = "My social security is 770-12-3456"
        expected_output = "My social security is "
        # Actual call
        output_text = remove_ssn(input_text)
        # Asserts
        self.assertEqual(output_text, expected_output)

    def test_remove_ssn_no_ssn(self):
        # Setup
        input_text = "Hello world!"
        expected_output = "Hello world!"
        # Actual call
        output_text = remove_ssn(input_text)
        # Asserts
        self.assertEqual(output_text, expected_output)

    def test_remove_ssn_all_ssns(self):
        # Setup
        input_text = '574-76-3766, 664-20-8576, 481-94-4099, 585-60-3079, 541714785'
        expected_output = ', , , , '
        # Actual call
        output_text = remove_ssn(input_text)
        # Asserts
        self.assertEqual(output_text, expected_output)

    def test_remove_ssn_none(self):
        # Setup
        input_text = None
        expected_output = ''
        # Actual call
        output_text = remove_ssn(input_text)
        # Asserts
        self.assertEqual(output_text, expected_output)

    def test_remove_ssn_empty_input(self):
        # Setup
        input_text = ''
        expected_output = ''
        # Actual call
        output_text = remove_ssn(input_text)
        # Asserts
        self.assertEqual(output_text, expected_output)

    def test_remove_credit_card_number(self):
        # Setup
        input_text = "Please refund me 5116937367451492"
        expected_output = "Please refund me "
        # Actual call
        output_text = remove_credit_card_number(input_text)
        # Asserts
        self.assertEqual(output_text, expected_output)

    def test_remove_credit_card_number_no_credit_card_number(self):
        # Setup
        input_text = "Hello world!"
        expected_output = "Hello world!"
        # Actual call
        output_text = remove_credit_card_number(input_text)
        # Asserts
        self.assertEqual(output_text, expected_output)

    def test_remove_credit_card_number_all_credit_card_numbers(self):
        # Setup
        input_text = '379524231139785, 5592621143924294, 6011167500016424, 4500339642915036, 4979770613611'
        expected_output = ', , , , '
        # Actual call
        output_text = remove_credit_card_number(input_text)
        # Asserts
        self.assertEqual(output_text, expected_output)

    def test_remove_credit_card_number_none(self):
        # Setup
        input_text = None
        expected_output = ''
        # Actual call
        output_text = remove_credit_card_number(input_text)
        # Asserts
        self.assertEqual(output_text, expected_output)

    def test_remove_credit_card_number_empty_input(self):
        # Setup
        input_text = ''
        expected_output = ''
        # Actual call
        output_text = remove_credit_card_number(input_text)
        # Asserts
        self.assertEqual(output_text, expected_output)

    def test_remove_names(self):
        # Setup
        input_text = "My name is Lionel Messi"
        expected_output = ['My', 'name', 'is']
        # Actual call
        output_text = remove_names(input_text)
        # Asserts
        self.assertListEqual(output_text, expected_output)

    def test_remove_names_no_names(self):
        # Setup
        input_text = 'Hello World.'
        expected_output = ['Hello', 'World', '.']
        # Actual call
        output_text = remove_names(input_text)
        # Asserts
        self.assertListEqual(output_text, expected_output)

    def test_remove_names_all_names(self):
        # Setup
        input_text = 'Paul Allen John Doe Jane Doe Lebron James'
        expected_output = []
        # Actual call
        output_text = remove_names(input_text)
        # Asserts
        self.assertListEqual(output_text, expected_output)

    def test_remove_names_none(self):
        # Setup
        input_text = None
        expected_output = []
        # Actual call
        output_text = remove_names(input_text)
        # Asserts
        self.assertListEqual(output_text, expected_output)

    def test_remove_names_empty_input(self):
        # Setup
        input_text = ''
        expected_output = []
        # Actual call
        output_text = remove_names(input_text)
        # Asserts
        self.assertListEqual(output_text, expected_output)

    def test_check_spelling(self):
        # Setup
        input_text = "Helloo world"
        expected_output = "hello world"
        # Actual call
        output_text = check_spelling(input_text)
        # Asserts
        self.assertEqual(output_text, expected_output)

    def test_check_spelling_list(self):
        # Setup
        input_text = ["Helloo", "world"]
        expected_output = "hello world"
        # Actual call
        output_text = check_spelling(input_text)
        # Asserts
        self.assertEqual(output_text, expected_output)

    def test_check_spelling_no_spelling_error(self):
        # Setup
        input_text = "Hello world!"
        expected_output = "hello world !"
        # Actual call
        output_text = check_spelling(input_text)
        # Asserts
        self.assertEqual(output_text, expected_output)

    def test_check_spelling_no_spelling_error_list(self):
        # Setup
        input_text = ["hello", "world"]
        expected_output = "hello world"
        # Actual call
        output_text = check_spelling(input_text)
        # Asserts
        self.assertEqual(output_text, expected_output)

    def test_check_spelling_all_errors(self):
        # Setup
        input_text = 'Helllo worlld nicee to meeet yuu'
        expected_output = 'hello world nice to meet you'
        # Actual call
        output_text = check_spelling(input_text)
        # Asserts
        self.assertEqual(output_text, expected_output)

    def test_check_spelling_all_errors_list(self):
        # Setup
        input_text = ['Helllo', 'worlld', 'nicee', 'to', 'meeet', 'yuu']
        expected_output = 'hello world nice to meet you'
        # Actual call
        output_text = check_spelling(input_text)
        # Asserts
        self.assertEqual(output_text, expected_output)

    def test_check_spelling_none(self):
        # Setup
        input_text = None
        expected_output = ''
        # Actual call
        output_text = check_spelling(input_text)
        # Asserts
        self.assertEqual(output_text, expected_output)

    def test_check_spelling_empty_input(self):
        # Setup
        input_text = ''
        expected_output = ''
        # Actual call
        output_text = check_spelling(input_text)
        # Asserts
        self.assertEqual(output_text, expected_output)

    def test_check_spelling_empty_list_input(self):
        # Setup
        input_text = []
        expected_output = ''
        # Actual call
        output_text = check_spelling(input_text)
        # Asserts
        self.assertEqual(output_text, expected_output)

    def test_substitute_token(self):
        # Setup
        input_list = ['hello', 'world', 'msft']
        expected_output = ['hello', 'world', 'Microsoft']
        # Actual call
        output_text = substitute_token(input_list)
        # Asserts
        self.assertListEqual(output_text, expected_output)

    def test_substitute_no_custom_token(self):
        # Setup
        input_list = ['hello', 'world']
        expected_output = ['hello', 'world']
        # Actual call
        output_text = substitute_token(input_list)
        # Asserts
        self.assertListEqual(output_text, expected_output)

    def test_substitute_all_custom_tokens(self):
        # Setup
        input_list = ['fyi', 'btw', 'apr', 'mon']
        expected_output = ['for your information', 'by the way', 'April', 'Monday']
        # Actual call
        output_text = substitute_token(input_list)
        # Asserts
        self.assertListEqual(output_text, expected_output)

    def test_substitute_token_none_input(self):
        # Setup
        input_text = None
        expected_output = []
        # Actual call
        output_text = substitute_token(input_text)
        # Asserts
        self.assertListEqual(output_text, expected_output)

    def test_substitute_token_empty_list_input(self):
        # Setup
        input_text = []
        expected_output = []
        # Actual call
        output_text = substitute_token(input_text)
        # Asserts
        self.assertListEqual(output_text, expected_output)

    @patch("text_preprocessing.text_preprocessing.to_lower", autospec=True)
    @patch("text_preprocessing.text_preprocessing.remove_url", autospec=True)
    @patch("text_preprocessing.text_preprocessing.remove_email", autospec=True)
    @patch("text_preprocessing.text_preprocessing.remove_phone_number", autospec=True)
    @patch("text_preprocessing.text_preprocessing.expand_contractions", autospec=True)
    @patch("text_preprocessing.text_preprocessing.check_spelling", autospec=True)
    @patch("text_preprocessing.text_preprocessing.remove_special_characters", autospec=True)
    @patch("text_preprocessing.text_preprocessing.remove_punctuations", autospec=True)
    @patch("text_preprocessing.text_preprocessing.remove_whitespace", autospec=True)
    @patch("text_preprocessing.text_preprocessing.normalize_unicode", autospec=True)
    @patch("text_preprocessing.text_preprocessing.remove_stopwords", autospec=True)
    @patch("text_preprocessing.text_preprocessing.remove_names", autospec=True)
    @patch("text_preprocessing.text_preprocessing.substitute_token", autospec=True)
    @patch("text_preprocessing.text_preprocessing.lemmatize_word", autospec=True)
    def test_preprocess_text(self,
                             mock_lemmatize_word: MagicMock,
                             mock_substitute_token: MagicMock,
                             mock_remove_names: MagicMock,
                             mock_remove_stopwords: MagicMock,
                             mock_normalize_unicode: MagicMock,
                             mock_remove_whitespace: MagicMock,
                             mock_remove_punctuations: MagicMock,
                             mock_remove_special_characters: MagicMock,
                             mock_check_spelling: MagicMock,
                             mock_expand_contractions: MagicMock,
                             mock_remove_phone_number: MagicMock,
                             mock_remove_email: MagicMock,
                             mock_remove_url: MagicMock,
                             mock_to_lower: MagicMock):
        # Setup
        input_text = 'a test'
        # Actual call
        _ = preprocess_text(input_text)
        # Asserts
        mock_to_lower.assert_called_once()
        mock_remove_url.assert_called_once()
        mock_remove_email.assert_called_once()
        mock_remove_phone_number.assert_called_once()
        mock_expand_contractions.assert_called_once()
        mock_check_spelling.assert_called_once()
        mock_remove_special_characters.assert_called_once()
        mock_remove_punctuations.assert_called_once()
        mock_remove_whitespace.assert_called_once()
        mock_normalize_unicode.assert_called_once()
        mock_remove_stopwords.assert_called_once()
        mock_remove_names.assert_called_once()
        mock_substitute_token.assert_called_once()
        mock_lemmatize_word.assert_called_once()

    @patch("text_preprocessing.text_preprocessing.to_lower", autospec=True)
    @patch("text_preprocessing.text_preprocessing.remove_url", autospec=True)
    @patch("text_preprocessing.text_preprocessing.remove_email", autospec=True)
    @patch("text_preprocessing.text_preprocessing.remove_phone_number", autospec=True)
    def test_preprocess_text_custom(self,
                                    mock_remove_phone_number: MagicMock, mock_remove_email: MagicMock,
                                    mock_remove_url: MagicMock, mock_to_lower: MagicMock):
        # Setup
        input_text = 'a test'
        # Actual call
        pipeline_functions = [mock_to_lower, mock_remove_url, mock_remove_email, mock_remove_phone_number]
        _ = preprocess_text(input_text, pipeline_functions)
        # Asserts
        mock_to_lower.assert_called_once()
        mock_remove_url.assert_called_once()
        mock_remove_email.assert_called_once()
        mock_remove_phone_number.assert_called_once()
