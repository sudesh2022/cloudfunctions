import pyjokes

def main(params):
  joke=pyjokes.get_joke()
  return {
    "body": joke
  } 

#x = main("")
#print(x["joke"])