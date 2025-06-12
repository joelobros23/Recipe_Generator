```python
# ingredients.py - Created by AI Programmer

def get_user_ingredients():
    """
    Prompts the user to enter their available ingredients and returns them as a list.
    """
    ingredients = []
    print("Enter your available ingredients, separated by commas (e.g., chicken, rice, broccoli):")
    user_input = input()
    ingredients = [ingredient.strip() for ingredient in user_input.split(',')]
    return ingredients
```