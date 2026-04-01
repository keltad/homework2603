import re
from collections import Counter

def read_text() -> str:
    with open ("./text.txt", encoding='utf-8') as f:
        return f.read()
    
def analyze_text(text):
    ukr_words = r'[аА-яієїґЯІЄїҐ+\']+'

    all_words = r'[a-zA-ZА-Яа-яЁёІіЇїЄєҐґʼ\']+'
    
    numeric_values = r'\b\d+%?\b|\b[IVXLCDM]+\b'

    ukr_words = re.findall(ukr_words, text)
    all_words = re.findall(all_words, text)
    numeric_values = re.findall(numeric_values, text)

    ukr_counter = Counter(ukr_words)
    all_counter = Counter(all_words)
    num_counter = Counter(numeric_values)

    print(f"""
    --- Результати аналізу ---
    Кількість слів українською мовою: {sum(ukr_counter.values())}
    Загальна кількість слів: {sum(all_counter.values())}
    Кількість числових значень (цифри, %, римські): {sum(num_counter.values())}
        """)

if __name__ == "__main__":
    content = read_text()
    analyze_text(content)