#pip install gradio -q              for installing gradio module into your local host 
import gradio
import random
def password(Hint,len_of_pass):
  hash=['~','!','@','#','$','0','1','2','3','4','5','6','7','8','9']
  shash=Hint
  for i in hash:
    shash+=i
  shash=list(shash)
  random.shuffle(shash)
  del shash[int(len_of_pass):]
  scode=''
  for i in shash:
    scode+=i
  return scode

Hint=input('Enter your password hint !! ')
lenofpass=int(input('Enter the length of password : '))
password(Hint,lenofpass)

Passgen = gradio.Interface(fn=password,inputs=['text','number'],outputs=['text']).launch()