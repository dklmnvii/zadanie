class SubjectIndex:
 
    def __init__(self):
        self.index = {}

    def generate_from_keyboard(self):
 
        while True:
            word = input("Введите слово (или 'q' для выхода): ")
 
            if word == 'q':
                break

            page_numbers = []
 
            while len(page_numbers) < 10:
                page = input("Введите номер страницы (или 'q' для завершения): ")
                if page == 'q':
                    break
                page_numbers.append(page)

            self.add_word(word, page_numbers)

    def add_word(self, word, page_numbers):
 
        if word in self.index:
            self.index[word].extend(page_numbers)
 
        else:
            self.index[word] = page_numbers

    def output_index(self):
        for word, page_numbers in sorted(self.index.items()):
            print(f"{word}: {', '.join(page_numbers)}")

    def get_page_numbers(self, word):
 
        if word in self.index:
            return self.index[word]
 
        else:
            return []

    def delete_word(self, word):
 
        if word in self.index:
            del self.index[word]
            print(f"Удален '{word}' по индексу.")
 
        else:
            print(f"'{word}' не найдено в индексе.")

index = SubjectIndex()
index.generate_from_keyboard()
index.output_index()

word = input("Введите слово, чтобы получить номера страниц: ")
page_numbers = index.get_page_numbers(word)

print(f"Номера страниц для '{word}': {', '.join(page_numbers)}.")
word_to_delete = input("Введите слово для удаления из индекса: ")
index.delete_word(word_to_delete)