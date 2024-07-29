def extract_birds(message: str) -> list[str]:
    birds = ''.join(char for char in message if char.isalpha() or char.isspace()).split()
    return birds

if __name__ == "__main__":
    pass
    # ОСЬ ТУТ МОЇ ТЕСТИ ->
    # print(extract_birds("Качка, Гуска; Курка. Півень: Індик"))
    # print(extract_birds("Голуб! Ластівка. Синиця; Сойка"))
    # print(extract_birds("Горобець Качка:Курка,Індик"))