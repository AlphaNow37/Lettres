# fonction qui transforme un text
def ascii_text(text):
    text = text.lower()
    lines = text.split("\n")
    result = ""
    for line in lines:
        l1, l2, l3 = "", "", ""
        for lettre in line:
            partie1, partie2, partie3 = letters[lettre].split("\n")
            l1 += partie1 + " "
            l2 += partie2 + " "
            l3 += partie3 + " "
        result += f"{l1}\n{l2}\n{l3}\n"
    return result

# fonction qui retourne une liste de gros char
def get_chars():
    # tu dois avoir le fichier "letters"
    with open("letters") as file:
        contenu = file.read()
        lines = contenu.split("\n")
        letters = {}
        chars = [
            "abcdefghijklmnop",
            "qrstuvwxyz ",
            "1234567890",
            "!?.():;,/\\=²\"'-+*|[]~%",
            "{}^€"
        ]
        for group_line in range(0, len(lines), 4):
            l1, l2, l3, sep = lines[group_line:group_line+4]
            sep = sep.split("+")
            line_letters = []
            avant = 0
            x = 0
            while x < len(sep):
                len_letter = len(sep[x])
                line_letters.append("\n".join(
                    (l1[avant+1: avant+len_letter-1], l2[avant+1: avant+len_letter-1], l3[avant+1: avant+len_letter-1])))
                avant += len_letter + 1
                x += 1
            letters.update(dict(zip(chars[group_line//4], line_letters)))
    return letters
