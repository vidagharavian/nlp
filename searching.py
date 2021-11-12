from nltk import word_tokenize
from nltk.stem import snowball

from preprocessing import Preprocessing


class Search():
    pre_processed_list = None
    search_query=None

    def __init__(self,pre_processed_list,search_query) -> None:
        self.search_query=search_query
        self.pre_processed_list=pre_processed_list

    def process_and_search(self):
        matched_documents = []

        for word in word_tokenize(self.search_query):
            processed_word=Preprocessing.preparing(word)
            if processed_word not in None:
                matches = self.get_index(processed_word)
                if matches is not None:
                    matched_documents.append(matches)
        return matched_documents

    def get_index(self,search_word):
        for j,i in self.pre_processed_list.items():
            i:list
            count=i.count(search_word)
            if count!=0:
                    return {j:count}
        return None
preprocessor=Preprocessing()
preprocessor.get_plot_summaries_obj()
searcher=Search(preprocessor.pd_phase1,'develop')
print(searcher.process_and_search())


