import re

def find_letter_pairs(line):
    pairs = []
    words = re.findall(r'\b[^\W_]+\b', line.lower(), flags=re.UNICODE)

    for i, word in enumerate(words):
        for j in range(len(word) - 1):
            pairs.append(word[j:j+2])

        if i < len(words) - 1:
            if not (word.endswith('у') and words[i+1].startswith('н')):
                if word and words[i+1]:
                    pairs.append(word[-1] + words[i+1][0])

    return pairs

def main():
    filename = "laba_9.txt"

    try:
        with open(filename, "r", encoding="utf-8") as f:
            for idx, line in enumerate(f, start=1):
                line = line.strip()
                if not line:
                    print(f"Рядок {idx}: (пустий)")
                    continue

                pairs = find_letter_pairs(line)
                unique_pairs = list(dict.fromkeys(pairs))
                selected_pairs = unique_pairs[:3]
                print(f"Рядок {idx}: {selected_pairs}")
    except FileNotFoundError:
        print(f"Файл '{filename}' не знайдено. Поклади laba_9.txt в ту ж папку, де скрипт.")

if __name__ == "__main__":

    main()
