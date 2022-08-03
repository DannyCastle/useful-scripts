birthdays = {'Daniel':'Apr 19', 'Kaylyn':'July 19', 'Ashton':'Jan 26'}

while True:
    print('Enter a name to look up their birthday (or blank to quit): ')
    name = str(input())
    if name == '':
        break

    if name in birthdays:
        print(name + '\'s birthday is on ' + birthdays[name])
    else:
        print('I do not have the birthday for ' + name)
        print('What is their birthday?')
        newBirthday = input()
        birthdays[name] = newBirthday
        print('Birthday database updated.')
        
