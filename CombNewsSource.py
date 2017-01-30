import newspaper

class CombNewsSource(object):

  def __init__(self, source, keywordSimilarity, keywordDict):
    print "init"
    self.keywordDict = keywordDict
    self.articleSource= self.buildSource(source)
    self.similarityThreshold = calculateSimilarityThreshold(keywordSimilarity)
    self.combThruSource(keywordSimilarity)
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
      self.downloadAndParseArticle(article)
      similarityCount = 0
      print "Title ", article.title
      for word in article.title:
        if word in self.keywordDict:
          similarityCount += 1
        if similarityCount >= self.similarityThreshold:
          self.addWordsToDict(article.title)
          self.addWordsToDict(article.keywords)
# not sure if I should determine similarity based on title alone or keywords included

  def calculateSimilarityThreshold(self, keywordSimilarity):
      return (keywordSimilarity / 100.0) * len(self.keywordDict)
    
  def downloadAndParseArticle(self, article):
    article.download()
    article.parse()

  def addWordsToDict(self, wordsToAdd):
    for word in wordsToAdd:
      if word in self.keywordDict:
      	self.keywordDict[str(word)] += 1
      else:
      	self.keywordDict[str(word)] = 0

sample = { "Trump": 1, "United States": 1, "judge": 1, "Pence": 1 }
test = CombNewsSource('http://cnn.com', 25, sample)
