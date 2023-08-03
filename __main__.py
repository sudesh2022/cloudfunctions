import pyjokes

def main(params):
  jokes=pyjokes.get_joke()

  return {
   
        "body": jokes
  }
