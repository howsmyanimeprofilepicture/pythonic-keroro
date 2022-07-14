def get_prompt(num_spc: int = 20, path="prompt.txt"):
    with open("prompt.txt", "r", encoding="utf-8") as f:
        raw_text = f.readlines()

    return [line.replace("\n", " ") + " " * num_spc for line in raw_text]

