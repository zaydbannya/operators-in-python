amount=int(input("inter the number"))
note_1=amount//100
note_2=(amount%100)//50
note_3=((amount%100)%50)//10
print("notes of 100 rupee",note_1)
print("notes of 50 rupee",note_2)
print("notes of 10 rupee",note_3)