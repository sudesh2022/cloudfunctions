import pyjokes
import json

def main(params):
  joke=pyjokes.get_joke()
  mydic = { "body": joke}
  x= json.dumps(mydic)
  return x

#x = main("")
#print(x)