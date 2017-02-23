def Trie:
  def __init__(self):
    self.root = new TrieNode()

  def addWord(self, word, nextLetter, videoClip):
    current = self.root

    # Build the branch for the word
    for character in word:
      if current[character] is None:
        current[character] = new TrieNode()
      current = current[character]

    # Cap each branch with a null character, the first character 
    # of the next word, and the source video information
    if current['\0'] is None:
      current['\0'] = new TrieNode(nextLetter, videoClip)
    else:
      current['\0'].addReference(nextLetter, videoClip)

  def getWord(self, word):
    current = self.root

    for character in word:
      if current is None:
        return None
      current = current[character]

   return current['\0']