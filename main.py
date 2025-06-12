```python
# main.py - Created by AI Programmer

import recipe_logic
import recipe_templates

def main():
    print("Welcome to the Personalized Recipe Generator!")
    ingredients = recipe_logic.get_user_ingredients()
    if ingredients:
        recipe = recipe_logic.generate_recipe(ingredients)
        if recipe:
            formatted_recipe = recipe_templates.format_recipe(recipe)
            print("\nHere's your personalized recipe:")
            print(formatted_recipe)
        else:
            print("Failed to generate a recipe with the provided ingredients.")
    else:
        print("No ingredients provided. Recipe generation aborted.")

if __name__ == "__main__":
    main()
```