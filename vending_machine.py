def vending(value):
    """
    Function for vending machine
    """

    notes = [1000, 500, 100, 50, 20, 10, 5, 2, 1]
    total = 0

    for i in range(len(notes)):
        if int(value/notes[i] != 0):
            total += int(value/notes[i])
            print(notes[i], 'rs notes:', int(value/notes[i]))
            value = int(value % notes[i])
        if value == 0:
            print('total notes', int(total))
            return


if __name__ == '__main__':
    amount = int(input('enter amount: '))
    vending(amount)

