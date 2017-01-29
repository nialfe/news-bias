# News Article Bias
Using Python library newspaper to determine bias
## Phases
### Search for an event
  * Put event keywords into dict
  * Comb thru articles w/ at least 50% of keywords in their keywords
  * Put rest of article's keywords into dict
  * Select top words in dict as subject
### "Synonymize": find POS associated w/ subject (in same sentence)
  * Verbs 
  * Nouns
  * Adjectives
