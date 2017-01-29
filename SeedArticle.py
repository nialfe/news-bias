import newspaper

class SeedArticle(object):

  def __init__(self, articleUrl):
    print "init"
    self.article = self.buildSourceFromUrl(articleUrl)
    self.keywords = {}
    self.article.download()
    self.article.parse()
    self.article.nlp()

    self.readPython()

  def buildSourceFromUrl(self, url):
    print "building source of ", url
    return newspaper.Article(url=url)

  def getTopicWords(self):
    self.addWordsToDict(self.article.title.split())
    self.addWordsToDict(self.article.keywords)
    return self.keywords

  def addWordsToDict(self, wordsToAdd):
    print wordsToAdd
    for word in wordsToAdd:
      if word in self.keywords:
      	self.keywords[str(word)] += 1
      elif word not in self.stopwords:
      	self.keywords[str(word)] = 0

  def readPython(self):
    s = open('excluded_words.txt', 'r').read()
    self.stopwords = eval(s)

  def printDict(self, dictToPrint):
    for item in dictToPrint.iteritems():
      print item

test = SeedArticle('http://www.cnn.com/2017/01/29/politics/donald-trump-travel-ban-green-card-dual-citizens/index.html')
print "\ngetting topic words"
for word, freq in test.getTopicWords().iteritems():
  print word
