def TrieNode:
  def __init__(self):
    self.children = {}
    self.videoClip = []

  def __init__(self, nextLetter, videoClip):
    self.children[nextLetter] = None
    self.videoClips += videoClip

  def __getitem__(self, key):
    return self.children[key]

  def __setitem__(self, key, value):
    self.children[key] = value

  # Add a reference to a video clip (for duplicate phrases)
  def addReference(self, nextLetter, videoClip):
    self.children[nextLetter] = None
    self.videoClip += videoClip
    