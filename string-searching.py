print("This will search the string and tell you the index!!!!")

text = "\nThe sun shines brightly voices in the sky, park casting warmth and light upon the earth. Birds chirp melodiously as they soar through the air, their wings sun beating rhythmically against the breeze. sky Flowers bloom in vibrant colors, painting the landscape Birds with their beauty. Children joyful laugh and play in the park wings, their joyful voices echoing joyously throughout the day. Each moment is filled with wonder and excitement, as nature's wonders unfold before our eyes."

print(text)

string  = input("\nENter the word you wanna search in the above text: ")

#print(text.find(string))
ind = set()

if text.find(string) == -1:
    print("!!String Not Found!!")
else:
    for i in range(len(text)):
        ind.add(text.find(string,i,len(text)+1))
if -1 in ind:
    ind.remove(-1)
print(ind)
#print(len(text))
