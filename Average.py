import code

word: str = 'sami'

print('Original Word - Input')
print(word)

print('Modifier Word - Output')
print(word.upper())

print (ord('h'))

#konverto shkronjen e pare ne shkronje te madhe
word: str = 'sami'
new_chars: list[chr(1)] = []


print('Original Word - input')
print(word)

print(f'shkronja e pare eshte: {word[0]}')
code: int = ord(word[0]);

print(f'kodi i shkronjes se pare eshte: {code}')
new_code = code - 32
alpha: chr = chr(new_code)

print(f'Rikthimi i kodit ASCII ne shkroje {alpha}')
print("Hello")
