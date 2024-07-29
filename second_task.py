def fix_ingredients(ingredients: list[str]) -> list[str]:
    if not isinstance(ingredients, list):
        raise TypeError("ingredients must be a list")
    if not all(isinstance(item, str) for item in ingredients):
        raise TypeError("All elements must be strings")

    fixed_ingredients = []
    for ingredient in ingredients:
        if not ingredient.casefold().startswith("z"):
            fixed_ingredients.append(ingredient[::-1])
        else:
            fixed_ingredients.append(ingredient)

    return fixed_ingredients

if __name__ == "__main__":
    pass
    # ОСЬ ТУТ МОЇ ТЕСТИ ->
    # print(fix_ingredients(["sugar", "zmilk", "retaW", "salt", "honey"]))
    # print(fix_ingredients(["zFlour", "liO", "hcaetS"]))
    # print(fix_ingredients(["zSalt", "retniW", "kcab"]))
