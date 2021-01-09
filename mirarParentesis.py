#  write a function that verified the correct order of the parenthesis

def run():
    message = input("Escriba el mensaje \n: ")

    open_list = ['(', '{', '[']
    close_list = [')', '}', ']']
    
    stack = []
    for i in message:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)

            if len(stack > 0) and open_list[pos] == stack[len(stack) -1]:
                stack.pop()
            else:
                return False
      
    if len(stack) == 0:
        return True
    else:
        return False
       




if __name__ == '__main__':
    if run():
        print('Orden Correcto!')
    else:
        print('Orden incorrecto!')

