import nltk

class SynonymizeArticle(object):

  def __init__(self, articleText, topicWords):
    self.noun

    self.topicWords = topicWords
    self.articleText = articleText
    self.dissectArticle()

  def dissectArticle(self):
    # find topic words: add word b4 & after to pos dict
    # print
