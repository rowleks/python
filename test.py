word = "rolex"

hint = "_" * len(word)

word_list = list(word)
hint_list = list(hint)

for i, letter in enumerate(word):
    if letter in "bobzy":
        hint_list[i] = letter

word_list[2] = "w"

join_word = "".join(word_list)
join_hint = "".join(hint_list)
print(hint)
print(hint_list)
print(join_hint)