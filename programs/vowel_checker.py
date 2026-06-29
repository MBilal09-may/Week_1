#Vowel Checker

print("Welcome!")

sentence =str(input("Write a sentence: "))
new_sentence = sentence.lower() #converting the user input in lower case

index = 0
count = 0
#a while loop which checks each character for a vowel
while index < len(sentence):
    if new_sentence[index]=="a" or new_sentence[index] =="e" or new_sentence[index] =="i" or new_sentence[index]=="o" or new_sentence[index]=="u":
        count+=1
    index+=1
    
print(f"Your sentence contains {count} vowels.")