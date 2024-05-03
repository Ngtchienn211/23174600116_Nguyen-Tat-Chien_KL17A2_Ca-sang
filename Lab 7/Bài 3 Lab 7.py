print("#39. The Postman")
text = "Postman of our area, Mr. Ramesh Gupta, is a very sincere person. He knows his work very well. He can tell any address of the locality. He has detail map of the area in his mind. He is working in this for last fifteen years. We never missed any letter or parcel. He is always in his khaki uniform. For illiterate people he also read the letters. He is always smiling, although his work is quite difficult. He has to cover long distances by his cycle even in the extreme weather. He is a hard worker. I like him."

words = text.lower().split()

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

most = max(word_count, key=word_count.get)
least = min(word_count, key=word_count.get)

print("Từ có số lượng nhiều nhất:", most, "- Số lần xuất hiện:", word_count[most])
print("Từ có số lượng ít nhất:", least, "- Số lần xuất hiện:", word_count[least])

