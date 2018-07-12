letters = {
'a' :".-",
'b' :"-...",
'c' :"-.-.",
'd' :"-..",
'e' :".",
'f' :"..-.",
'g' :"--.",
'h' :"....",
'i' :"..",
'j' :".---",
'k' :"-.-",
'l' :".-..",
'm' :"--",	
'n' :"-.",
'o' :"---",
'p' :".--.",
'q' :"--.-",
'r' :".-.",
's' :"...",
't' :"-",
'u' :"..-",
'v' :"...-",
'w' :".--",
'x' :"-..-",
'y' :"-.--",
'z' :"--.."}
ip = eval(raw_input('enter input'))
res = []
for item in ip:
    temp = ''
    for letter in item:
        temp = temp + letters[letter]
    if temp not in res:
        res.append(temp)
print(len(res))
