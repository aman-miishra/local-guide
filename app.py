from kiro import Kiro

kiro = Kiro(context_file="product.md")

text = input("Enter Mumbai slang: ")
result = kiro.ask(text)

print("Meaning:", result)
