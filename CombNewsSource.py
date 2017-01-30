import newspaper

class CombNewsSource(object):

  def __init__(self, source, keywordSimilarity, keywordDict):
    print "init"
    self.keywordDict = keywordDict
    self.articleSource= self.buildSource(source)
#Will need list for ease of access
    self.articleUrls = []
    self.similarityThreshold = self.calculateSimilarityThreshold(keywordSimilarity)
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
      self.addArticleIfSimilarityThresholdHit(article)
      	
# not sure if I should determine similarity based on title alone or keywords included
  def addArticleIfSimilarityThresholdHit(self, article):
    similarCount = 0
    similarCount += self.addWordsIfSimilar(article.title.split(), article, similarCount)
    self.addWordsIfSimilar(article.keywords, article, similarCount)

  def addWordsIfSimilar(self, words, article, similarityCount):
    for word in words:
      print word
      if word in self.keywordDict:
      	similarityCount += 1
      if similarityCount >= self.similarityThreshold:
      	self.addArticleToCollection(article)
    return similarityCount

  def addArticleToCollection(self, article):
    print "\n\n\nAdding ", article.title
    self.addWordsToDict(article.title)
    self.addWordsToDict(article.keywords)
    self.articleUrls.append(article.url) 

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

sample = { "Trump": 1, "ban": 1, "judge": 1, "Pence": 1, "refugee": 1}
test = CombNewsSource('http://cnn.com', 25, sample)
