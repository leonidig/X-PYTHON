
def extract_birds(message: str) -> list[str]:
    birds = ''.join(char for char in message if char.isalpha() or char.isspace()).split()
    return birds

# Тести не хочу в код пхати але я робив



def fix_ingredients(ingredients: list[str]) -> list[str]:
    if not isinstance(ingredients, list):
        raise TypeError("ingredients must be a list")
    if not all(isinstance(item, str) for item in ingredients):
        raise TypeError("All elements must be strings")


    # Можу так -> return [element[::-1] if not element.lower().startswith("z") else element for element in ingredients]

    fixed_ingredients = []
    for ingredient in ingredients:
        if not ingredient.casefold().startswith("z"):
            fixed_ingredients.append(ingredient[::-1])
        else:
            fixed_ingredients.append(ingredient)

    return fixed_ingredients



if __name__ == "__main__":
    pass
# Тести не хочу в код пхати але я робив