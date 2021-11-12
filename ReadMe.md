# Requirements
در این  پرو‌‌‌ژه  فقط از کتابخانه های nltk و pandas استفاده شده است.
# Preprocessing 
- ابتدا  ستاپورد ها حذف میشوند. 
- سپس semitize میشوند
-  کلمات lower case  میشوند
-  در پایان Lemmatizeمیشوند
‍‍‍‍`    def preparing(cls,word):
        wordnet_lemmatizer = WordNetLemmatizer()
        if word not in cls.stop_words:
            word = word.lower()
            stemmer = snowball.SnowballStemmer('english')
            stemmed_word= stemmer.stem(word)
            return wordnet_lemmatizer.lemmatize(stemmed_word)
        return None
		`
# Search
مراحل preprocessing  روی کلمه قابل سرچ نیز انجام میشود سپس از دیکشنری به دست آمده در بخش اول استفاده می شود در صورت پیدا شدن کله مورد جستجو اینکس آن + تعداد تکرار آن کلمه در همان اینکس بازمیگردد.
 `def get_index(self,search_word):
        for j,i in self.pre_processed_list.items():
            i:list
            count=i.count(search_word)
            if count!=0:
                    return {j:count}
        return None `
		
 `def process_and_search(self):
        matched_documents = []
        for word in word_tokenize(self.search_query):
            processed_word=Preprocessing.preparing(word)
            if processed_word not in None:
                matches = self.get_index(processed_word)
                if matches is not None:
                    matched_documents.append(matches)
        return matched_documents`
# Team member 
- fateme baghkhani
- vida gharavian
- maryam saberi
- parisa ahmadi

				
