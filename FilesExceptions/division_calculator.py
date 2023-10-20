print ('Give me two numbers, and I\'ll divide them')
print('Enter \'q\' to quit.')

while True:
    first_number = input('\nEnter first number: ')
    if first_number == 'q':
        break

    second_number = input('Enter second number: ')
    if second_number == 'q':
        break

    try: # The only code in try block is code that might cause exception
        answer = int(first_number)/int(second_number)
    except ZeroDivisionError:
        print("You cannot divide by 0")
    except ValueError:
        print("Please provide a number")
    else: # comes here if code in try is successful
        print(answer)
