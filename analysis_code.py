import nltk
import re
import pandas as pd

import os
from nltk.tokenize import word_tokenize, sent_tokenize
nltk.download('punkt')
folder_path='StopWords'
text_files = [f for f in os.listdir(folder_path) if f.endswith(".txt")]
stopword_dic=[]
for file_name in text_files:
    file_path = os.path.join(folder_path, file_name)
    with open(file_path, 'r') as file:
            stopword_dic = set(file.read().split())
Pos_dict_path=os.path.join('MasterDictionary', 'positive-words.txt')
Neg_dict_path=os.path.join('MasterDictionary', 'negative-words.txt')
negative_word_dic=[] 
with open(Neg_dict_path, 'r') as file:
    negative_word_dic = set(file.read().split())
negative_word_dic
positive_word_dic=[] 
with open(Pos_dict_path, 'r') as file:
    positive_word_dic = set(file.read().split())
positive_word_dic
def clean_text(text):
    words = word_tokenize(text)
    cleaned_words = [word.lower() for word in words if word.isalpha() and word.lower() not in stopword_dic]
    return cleaned_words
def calculate_positive_score(text, positive_dict):
    positive_words = [word for word in text if word in positive_dict]
    return len(positive_words)
def calculate_negative_score(text, negative_dict):
    negative_words = [word for word in text if word in negative_dict]
    return len(negative_words) * -1
def calculate_polarity_score(positive_score, negative_score):
    return (positive_score - negative_score) / (positive_score + negative_score + 0.000001)
def calculate_subjectivity_score(positive_score, negative_score, total_words):
    return (positive_score + negative_score) / (total_words + 0.000001)
def analyze_readability(text):
    sentences = sent_tokenize(text)
    total_words = len(clean_text(text))
    average_sentence_length = total_words / len(sentences)
    
    complex_words = [word for word in clean_text(text) if syllable_count(word) > 2]
    percentage_complex_words = len(complex_words) / total_words
    fog_index = 0.4 * (average_sentence_length + percentage_complex_words)

    average_words_per_sentence = total_words / len(sentences)
    complex_word_count = len(complex_words)

    return average_sentence_length, percentage_complex_words, fog_index, average_words_per_sentence, complex_word_count, total_words
def syllable_count(word):
    vowels = "aeiouy"
    count = 0

    # Handle words ending with "es" and "ed"
    if word.endswith(("es", "ed")):
        pass
    else:
        for char in word:
            if char.lower() in vowels:
                count += 1

    return count
def calculate_syllables_per_word(text):
    words = clean_text(text)
    syllables = sum(syllable_count(word) for word in words)
    return syllables / len(words)
def count_personal_pronouns(text):
    personal_pronouns = re.findall(r'\b(?:I|we|my|ours|us)\b', text, flags=re.IGNORECASE)
    return len(personal_pronouns)
def calculate_average_word_length(text):
    words = clean_text(text)
    total_characters = sum(len(word) for word in words)
    return total_characters / len(words)
output_data = []
input_data=[]
input_path=os.path.join('Extracted Data','blackassign0001')
with open(input_path, 'r') as file:
     input_data= file.read()
input_data
cleaned_text = " ".join(clean_text(input_data))
positive_score = calculate_positive_score(cleaned_text, positive_word_dic)
negative_score = calculate_negative_score(cleaned_text, negative_word_dic)
polarity_score = calculate_polarity_score(positive_score, negative_score)
subjectivity_score = calculate_subjectivity_score(positive_score, negative_score, len(cleaned_text))

avg_sentence_length, percentage_complex_words, fog_index, avg_words_per_sentence, complex_word_count, word_count = analyze_readability(input_data)

syllables_per_word = calculate_syllables_per_word(input_data)
personal_pronouns = count_personal_pronouns(input_data)
avg_word_length = calculate_average_word_length(input_data)
output_data.append([positive_score, negative_score, polarity_score, subjectivity_score,
                        avg_sentence_length, percentage_complex_words, fog_index,
                        avg_words_per_sentence, complex_word_count, word_count,
                        syllables_per_word, personal_pronouns, avg_word_length])
output_columns = ["POSITIVE SCORE", "NEGATIVE SCORE", "POLARITY SCORE", "SUBJECTIVITY SCORE",
                  "AVG SENTENCE LENGTH", "PERCENTAGE OF COMPLEX WORDS", "FOG INDEX",
                  "AVG NUMBER OF WORDS PER SENTENCE", "COMPLEX WORD COUNT", "WORD COUNT",
                  "SYLLABLE PER WORD", "PERSONAL PRONOUNS", "AVG WORD LENGTH"]

output_df = pd.DataFrame(output_data, columns=output_columns)

# Save the output DataFrame to Excel
output_df.to_excel("Output Data Structure.xlsx", index=False)
