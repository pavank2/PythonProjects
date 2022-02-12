import json
import difflib
data = json.load(open("data.json"))


def translate(word):
   word = word.lower(); 
  
   if word in data :
    #Converting list to string
       return data[word]
    #   str1=""

     #  for val in data[word]:
      #   print (str1.join(val))
      # return "Done"  
   elif len(difflib.get_close_matches(word,data.keys())) > 0:
       
       lst = difflib.get_close_matches(word,data.keys())
       bestMatchRatio = difflib.SequenceMatcher(None,lst[0],word).ratio()
       bestMatch = lst[0]   
        
       for k in lst:
          currentRatio = difflib.SequenceMatcher(None,k,word).ratio()
          if ( currentRatio > bestMatchRatio):
              bestMatchRatio = currentRatio
              bestMatch = k
       confirmation = input("Did you mean %s? If yes,press y. if no, press any character:" % bestMatch)
       if confirmation == "y":
          return data[bestMatch]
       else:
          return "Sorry,try again"
   else:
       return "Word does not exist"
    
   

word = input("Enter word: ")
output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print (output)        
        