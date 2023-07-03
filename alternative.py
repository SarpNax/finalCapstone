fact2 = "          The$first$electronic$computer$ENIAC$weighed$more$than$27$tons.          "
fact2 = fact2.replace("$", "WOW!")
print(fact2)
fact2 = fact2.strip()
print(fact2)
fact2 = fact2.split("WOW!")
print(fact2)

print("Example 3: ")

sentence = "ThisHELLOisHELLOrandomHELLOtextHELLOweHELLOareHELLOgoingHELLOtoHELLOsplitHELLOapart"
split_sentence = sentence.split("HELLO")
split_sentence2 = " ".join(split_sentence)
print(split_sentence2)

print("Example 5: ")
string_list = ["I", "like", "to", "join", "lists", "to", "make", "strings"]
list_joined = " ".join(string_list)
print(list_joined)