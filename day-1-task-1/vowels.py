sentence=str(input("Enter a sentance: "))
vowel_count=0
for char in sentence:
    if char.lower() in ("a","e","i","o","u"):
        vowel_count+=1

print(vowel_count)
