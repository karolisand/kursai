# Nuoroda: https://youtu.be/kqtD5dpn9C8?si=LM-uoUxN9aq-AP9j&t=2181
# Destytojo galutinis veikiantis:
weight = float(input("Weigh: "))
measurement = input("(k)kg or (l)lb: ")

if measurement.upper() == "K":
    converted = weight / 0.45
    print("weigh in LBs: " + str(converted))
elif measurement.upper() == "L":
    converted = weight * 0.45
    print("weigh in KG: " + str(converted))
else:
    print("you need to choose l or k")




# Mano galutinis veikiantis:
# weight = input("Weigh: ")
# measurement = input("(k)kg or (l)lb: ")

# if measurement.upper() == "K":
#     converted = float(weight) / 0.45
#     print("weigh in LBs: " + str(converted))
# elif measurement.upper() == "L":
#     converted = float(weight) * 0.45
#     print("weigh in KG: " + str(converted))
# else:
#     print("you need to choose l or k")


# Pirmas dublis:
# if measurement == str("l"):
#     print("skaicius")
# elif measurement == str("k"):
#     print("bbz")

print("")
print("Done")

# int() -> 100; float() -> 4.99; bool() -> True/False; str() -> Text
