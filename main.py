import random
spaces = [" ","\t","\n"]
punctuation = [".","!","?","\"",",","\'"]
endpunctuation = [".","!","?"]

def parse(text):
  words = []
  start = 0
  for cur, char in enumerate(text):
    if text[start] in spaces:
       start = cur
    if char in spaces or char in punctuation:
      word = text[start:cur]
      words.append(word) 
      start = cur 
  if start < len(text):
    word = text[start:]
    words.append(word) 
  return words

def buildmodel(words):
  model = {}
  for i,word in enumerate(words):
    if word not in model and word not in endpunctuation:
      model[word] = {}
    if i == 0:
      continue
    previous = words[i-1]
    if previous in endpunctuation:
      continue
    if word not in model[previous]:
      model[previous][word] = 0
    model[previous][word] += 1
  return model

def generate(model,sentence,word):
  sentence.append(word)
  if word in endpunctuation:
    return sentence
  possibilites = model[word]
  words = [k for k in possibilites.keys()]
  weights = [k for k in possibilites.values()]
  nextword = random.choices(words, weights = weights)[0]
  return generate(model, sentence, nextword)

def main():
  try:
    #filename = input("Enter file name: ")
    c = "constitution.txt"
    f = open(c)
    data = f.read()
    words = parse(data)
    model = buildmodel(words)
    sentence = generate(model,[],random.choice([word for word in words if len(word) > 0 and word[0].isupper()]))
    s = ""
    for word in sentence:
      if word in punctuation:
        s = s[:len(s)-1]
      s += word + " "
    print(s)
  except:
    print("File cannot be found. Please enter a valid file name.")
  
main() 