
# coding: utf-8

# In[ ]:


#Libraries import
from bs4 import BeautifulSoup
import urllib.request
import nltk

#extract text from webpage
response = urllib.request.urlopen('http://php.net/')
#read the response in a html
html = response.read()
soup = BeautifulSoup(html,"html5lib")
text = soup.get_text(strip=True) 
#tokenize the text.
tokens = [t for t in text.split()] 
#frequency of the words using nltk.
freq = nltk.FreqDist(tokens) 
for key,val in freq.items(): 
 print (str(key) + ':' + str(val))

