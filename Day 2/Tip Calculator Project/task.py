print("Assalawalaikum guys ye hai apna tip calculator!")
bill= float(input("Aur total bill kya tha kathe?"))
tip= int(input("Kitna toh bhi tip dete bade bhai? 10 12 15"))
people= int(input("kitne logo meh divide karna bade bhai?"))

bill_with_tip = tip / 100 * bill + bill
print(bill_with_tip)

bill_per_person = bill_with_tip / people
final_amount = round(bill_per_person, 2)
print(f"Ek ek jana chup chap itna dheko: ${final_amount}")





