from helpers import alphabet_position, rotate_character

def encrypt(text, rot):
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    transformed = ''
    transformation = []
    rot = int(rot)
    for charxt in text:
        if charxt not in alphabet:
            transformed = transformed + charxt
            chary = charxt
            transformation.append(chary)
        else:
            rotated_index = alphabet.index(charxt) + rot    
            if rotated_index < 26:
                transformed = transformed + alphabet[rotated_index]
                if ord(charxt) < 97:
                    chary = charxt.upper()
                    chary = rotate_character(charxt, rot)
                    transformation.append(chary)
                else:
                    chary = charxt.lower()
                    chary = rotate_character(charxt, rot)
                    transformation.append(chary)
            else:
                transformed = transformed + alphabet[rotated_index % 26]
                if ord(charxt) < 97:
                    chary = charxt.upper()
                    chary = rotate_character(charxt, rot)
                    transformation.append(chary)
                else:
                    chary = charxt.lower()
                    chary = rotate_character(charxt, rot)
                    transformation.append(chary)

    transformation = ''.join(transformation)
    #print(transformation)

    return transformation
#https://docs.python.org/3/reference/compound_stmts.html

def main():
    #from sys import argv
    #print("This is what the user typed on the command line:", argv)
    text = input('Type a message:')
    rot = input('Rotate by: ')
    print(encrypt(text, rot))
    #print(alphabet_position('a'))
    #print(alphabet_position('A'))
    #print(alphabet_position('b'))
    #print(alphabet_position('y'))
    #print(alphabet_position('z'))
    #print(alphabet_position('Z'))
    #print('end of alphabet position test')
    #print(rotate_character('a', 13) + '  -> n')
    #print(rotate_character('a', 14) + '  -> o')
    #print(rotate_character('a', 0) + '  -> a')
    #print(rotate_character('c', 26)+ '  -> c')
    #print(rotate_character('c', 27)+ '  -> d')
    #print(rotate_character('A', 13)+ '  -> N')
    #print(rotate_character('z', 1)+ '   -> a')
    #print(rotate_character('Z', 2)+ '   -> B')
    #print(rotate_character('z', 37)+ '  -> k')
    #print(rotate_character('!', 37)+ '  -> !')
    #print(rotate_character('6', 13)+ '  -> 6')
    #print('end of rotate character test')
    #print("Hello no comma")
    #print(encrypt('Hello', 5))
    #print("Hello with comma no space")
    #print(encrypt('Hello,', 5))
    #print("Hello with comma and with space")
    #print(encrypt('Hello, ', 5))
    #print(encrypt('World', 5))
    #print("Should print out full encrypted Hello, World")
    #print(encrypt('a', 13))
    #print(encrypt('abcd', 13))
    #print(encrypt('LaunchCode', 13))
    #print(encrypt('LaunchCode', 1))
    #print(encrypt('Hello, World!', 5))



if __name__ == "__main__":
    main()