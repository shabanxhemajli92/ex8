#Task1
text="Berlin is a world city of culture, politics, media and science."
print(len(text))
#Task2
text="Berlin is a world city of culture, politics, media and science."
first_char=text[0]
last_char=text[-1]
print(first_char + last_char)
#Task3
text="Berlin is a world city of culture, politics, media and science."
first_three=text[0:3]
print(first_three.upper())
#Task4
text="Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital"
b_appears=text.count("b")
print("B appears: " + str(b_appears) + "" ,"times")
#Task 5
text="Berlin straddles the banks of the Spree, which flows into the Havel (a tributary of the Elbe) in the western borough of Spandau."
last_ten=text[-10:]
print("Last ten characters: ",str(last_ten)) 