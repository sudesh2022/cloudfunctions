import pyjokes

def main(params):
  joke=pyjokes.get_joke()
  return {
    "joke": joke
  } 

#x = main("")
#print(x["joke"])