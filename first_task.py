def extract_birds(message: str) -> list[str]:
    birds = ''.join(char for char in message if char.isalpha() or char.isspace()).split()
    return birds

if __name__ == "__main__":
    pass
# Тести не хочу в код пхати але я робив
