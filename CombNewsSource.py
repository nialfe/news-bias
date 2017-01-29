import newspaper

class CombNewsSource(object):

  def __init__(self, source, keywordSimilarity, keywordDict):
    print "init"
    self.keywordDict = keywordDict
    self.articleSource= self.buildSource(source)
    self.combThruSource(keywordSimilarity)
# comb thru source articles
# get keywords
# if at least keywordSimilarity% of keywords exist in keywordDict, 
# put keywords into dict
# return dict

  def buildSource(self, source):
    print "building source of ", source
    return newspaper.build(source, memoize_articles=False)

  def combThruSource(self, keywordSimilarity):
    print "combThruSoure"
    for article in self.articleSource.articles: 
      article.download()
      article.parse()
      similarityCount = 0
      similarityThreshold = (keywordSimilarity / 100.0) * len(self.keywordDict)
      print "Title ", article.title
      for word in article.title:
        if word in self.keywordDict:
          similarityCount += 1
        if similarityCount >= similarityThreshold:
          self.addKeywordToDict(article.title)

  def addKeywordToDict(self, keywords):
    print "cool"

sample = { "Trump": 1, "United States": 1, "judge": 1, "Pence": 1 }
test = CombNewsSource('http://cnn.com', 25, sample)
