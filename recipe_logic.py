import json
import random

def generate_recipe(ingredients):
    """
    Generates a creative and personalized recipe based on user-provided ingredients.

    Args:
        ingredients (list): A list of strings representing the ingredients the user has.

    Returns:
        dict: A dictionary containing the recipe name, ingredients, and instructions,
              or None if a recipe could not be generated.
    """

    # Load recipe data from a JSON file (replace with a database or API if needed)
    try:
        with open("recipes.json", "r") as f:
            recipes = json.load(f)
    except FileNotFoundError:
        print("Error: recipes.json not found. Please create this file with recipe data.")
        return None
    except json.JSONDecodeError:
        print("Error: recipes.json is not a valid JSON file.")
        return None
    
    # Find recipes that match the given ingredients
    matching_recipes = []
    for recipe in recipes['recipes']:
        if all(ingredient.lower() in ' '.join(recipe['ingredients']).lower() for ingredient in ingredients):
            matching_recipes.append(recipe)

    if not matching_recipes:
        # If no exact matches, try a more lenient search (at least one ingredient matches)
        matching_recipes = [recipe for recipe in recipes['recipes'] if any(ingredient.lower() in ' '.join(recipe['ingredients']).lower() for ingredient in ingredients)]
        if not matching_recipes:
            print("No recipes found matching your ingredients.  Please try different ingredients")
            return None
        else:
            print("No exact match found. Showing recipes with at least one of your ingredients.")


    # Randomly select a matching recipe
    selected_recipe = random.choice(matching_recipes)

    return selected_recipe



if __name__ == '__main__':
    # Example usage:
    user_ingredients = ["chicken", "rice", "soy sauce"]
    recipe = generate_recipe(user_ingredients)

    if recipe:
        print("Recipe Name:", recipe['name'])
        print("Ingredients:", recipe['ingredients'])
        print("Instructions:", recipe['instructions'])
    else:
        print("No recipe found for the given ingredients.")
