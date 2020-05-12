from collections import Counter

non_letters=["1","2","3","4","5","6","7","8","9","0",":",";"," ","/n",".",","]
key_phrase_1=input("Enter the phrase:").lower()

#Removing non letters from phrase
for non_letters in non_letters:
    key_phrase_1=key_phrase_1.replace(non_letters,'')
total_occurences=len(key_phrase_1)

#Counter object
"""""A Counter is a collection where elements are stored as dictionary keys and their
counts are stored as dictionary values. Counts are allowed to be any integer
value including zero or negative counts.
"""
letter_count=Counter(key_phrase_1)
print("frequency analysisfrom the phrase:")
for key,value in sorted(letter_count.items()):
    percentage=100 * value/total_occurences
    percentage=round(percentage,2)
    print("\t \t"+key+"\t\t"+str(value)+"\t\t"+str(percentage))
ordered_letter_count=letter_count.most_common()
key_phrase_1_ordered_letters=[]
for pair in ordered_letter_count:
    key_phrase_1_ordered_letters.append(pair[0])
print("letters from high occurence to lower occurence:")
for letter in key_phrase_1_ordered_letters:
    print(letter, end='')