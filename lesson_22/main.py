import json

# text = [1, 5.3, True, None, [1,2], (5,7, "ENG", "RUS")]
# f = open("я генадий.json", "w")
# json.dump(text, f, ensure_ascii=False)
# b = json.dump(text, ensure_ascii=False)
# f.close()

# f = open("я генадий.json", "r", encoding="utf-8")
# # content = f.read()
# content = json.load(f)
# print(content)
# print(type(content))
# f.close()


# f = open("file.txt", "r", encoding="utf-8")
#
# con = f.readlines()
# print(con)
# f.close()
# dict = {}
# for element in con:
#     print(element)
#     lom = element.split(": ")
#     print(lom[0])
#     print(lom[1])
#     dict[lom[0]] = lom[1].rstrip("\n")
#
# print(dict)
# ff = open("я генадий.json", "w", encoding="utf-8")
# json.dump(dict, ff, ensure_ascii=False)
# ff.close

#Second task
f = open("я генадий.json", "w", encoding="utf-8")
con = json.load(f)
f.close
print(con)
for i, em in enumerate(con):
    if type(em) == str:
        con[i] += "!"
print(con)











