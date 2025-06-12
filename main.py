# main.py - Created by AI Programmer

import recipe_logic

def main():
    print("Welcome to the Personalized Recipe Generator!")
    ingredients = recipe_logic.get_user_ingredients()
    if ingredients:
        recipe = recipe_logic.generate_recipe(ingredients)
        print("\nHere's your personalized recipe:")
        print(recipe)
    else:
        print("No ingredients provided. Recipe generation aborted.")

if __name__ == "__main__":
    main()
