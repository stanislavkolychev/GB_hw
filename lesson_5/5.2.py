# Создать текстовый файл (не программно),
# сохранить в нём несколько строк, выполнить подсчёт строк и слов в каждой строке.

with open ("text2.txt", "r", encoding='utf-8') as f_obj:
    useful = [f'{line}, {count.strip()} - {len(count.split())} слов'
              for line, count in enumerate(f_obj, 1)]
    print(*useful, f"Всего строк - {len(useful)}.", sep="\n")
