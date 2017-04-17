from dai3syou import No20

lines = No20.extract_from_json(u"イギリス").split("\n")

for line in lines:
    if "Category" in line:
        print(line)

#print([line for line in lines if "Category" in line])