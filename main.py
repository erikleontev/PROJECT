meme_dict = {
            "КРИНЖ": "Что-то очень странное или стыдное",
            "ЛОЛ": "Что-то очень смешное",
            "КРИПОВЫЙ": "страшный, пугающий",
            "АГРИТЬСЯ": "злитьcя"
            }
for i in range(5):
    word = input("Введите непонятное слово (большими буквами!): ")
            
    if word in meme_dict.keys():
        print(meme_dict[word])
    # Что делать, если слово нашлось?
    else:
        print('данного слова нет в словаре')
    # Что делать, если слово не нашлось?
