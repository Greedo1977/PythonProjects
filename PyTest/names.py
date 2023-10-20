from name_function import get_formatted_name, get_name_reverse


print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break

    last = input("Please give me a last name: ")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print(f"\nNeatly formatted name: {formatted_name}")

    reverse_name = get_name_reverse(first, last)
    print(f"\nNeatly formatted reverse name: {reverse_name}")
