#  write a function that verified the correct order of the parenthesis

def search_key(msg, key):

    if len(key ) > 1 : 
        return "No se pueden buscar palabras"
    for i in msg:
        if i == key:
            return True


def run():
    message = input("Escriba el mensaje \n: ")
    key = input("mensaje o Letra a buscar: ")
    
    if search_key(message, key):
        print('yes')
    else:
        print('no')
       




if __name__ == '__main__':
    run()
