
responses = {}
polling_active = True
while polling_active:

    name = input('\nWhat is your name? ')

    prompt = 'If you could visit one place in the world, where would you go? '
    response = input(prompt)

    responses[name] = response

    continue_ = input("\nWould you like to continue [Y,N]? ")
    if continue_ == 'N':
        polling_active = False

print("\n----- Polling results -----\n")

for name,response in responses.items():
    print(f"{name} would like to visit {response}")
