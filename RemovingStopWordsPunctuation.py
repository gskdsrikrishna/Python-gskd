import re
from nltk.corpus import stopwords
from string import punctuation

# Removing stopwords and punctuation
text = "This is a sample sentence, containing stopwords and punctuation!"
stopwords_set = set(stopwords.words('english'))
cleaned_text = ' '.join(word for word in text.split() if word.lower() not in stopwords_set)
cleaned_text = re.sub(r'[^\w\s]', '', cleaned_text)  # Removing punctuation
print(cleaned_text)  # Output: 'sample sentence containing stopwords punctuation'
