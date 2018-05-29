# def create_server():
#   print('Do your work here!')

# if __name__ == '__main__':
#   create_server()


import socket
import _thread

host = '127.0.0.1'
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(5)


import random

def ask_me(conn):
  
  default_question = (b'What is your security question?\n')
  
  conn.send(default_question)
  

  answers = [b'Of course!\n', b'Duh!\n', b'Never!\n', b'Seriously..\n', b'Yes\n', b'Always\n']

  while True:

    data = conn.recv(1024)

    x = random.randint(0, len(answers) - 1)

    reply = (answers[x])

    if data == b'hello':    #ask about how to recognize strings 
      conn.sendall(b'goodbye')    #this is just a test. It does not work yet
    else:
      conn.sendall(reply)

    conn.sendall(default_question)
  
  conn.close()



while True:

  c, addr = s.accept()
  print('Got connection from ', addr)

  _thread.start_new_thread(ask_me, (c, ))


c.close()