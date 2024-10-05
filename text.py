def save_text(filename = "Test.txt"):
    text = input("Ingresa el texto: ")
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)
    print(f"Texto guardado en '{filename}'")


def paginate_text(input_file = "Test.txt", output_file= "Test_dividido.txt"):
    with open(input_file, "r", encoding="utf-8") as file:
        text = file.read()

    pages = [text[i:i + 30] for i in range(0, len(text), 30)]

    with open(output_file, "w", encoding="utf-8") as file:
        for i, page in enumerate(pages, start=1):
            file.write(f"página {i}: \"{page}\"\n")

        file.write(f"\n{len(pages)} página(s), {len(text)} caracteres en total")

    print(f"Texto dividido en páginas y guardado en '{output_file}'")

