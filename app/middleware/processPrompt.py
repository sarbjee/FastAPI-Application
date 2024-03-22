def promptResponse(prompt, interest, budget):
    """
    Generate personalized recommendations based on a user's prompt, selected interest area, and budget.

    Parameters:
    - prompt (str): User's text input describing what they are looking for.
    - interest (str): User's selected interest area (e.g., "Toys", "Games").
    - budget (float): User's budget constraint.

    Returns:
    - str: A response message with recommendations or a message indicating no matches were found.
    """
    # Mock data for demonstration purposes
    PRODUCT_CATALOG = [
        {"name": "Action Figure", "category": "Toys", "description": "An action figure for ages 5 and up.", "price": 20.00, "tags": ["adventure", "superhero"]},
        {"name": "Board Game", "category": "Games", "description": "A fun board game for the whole family.", "price": 30.00, "tags": ["strategy", "family"]},
        {"name": "Puzzle", "category": "Games", "description": "A challenging 1000-piece puzzle.", "price": 15.00, "tags": ["puzzle", "solitaire"]},
        # New educational toys
        {"name": "Science Kit", "category": "Educational", "description": "Explore basic scientific principles with this engaging kit.", "price": 25.00, "tags": ["science", "learning", "education"]},
        {"name": "Math Puzzle", "category": "Educational", "description": "Challenge your math skills with fun puzzles.", "price": 18.00, "tags": ["math", "education", "puzzle"]},
        {"name": "Language Learning Game", "category": "Educational", "description": "Learn new languages through interactive gameplay.", "price": 22.00, "tags": ["language", "learning", "education"]},]

    # Filter the product catalog based on the user's interest area and budget
    filtered_catalog = [product for product in PRODUCT_CATALOG if product["category"].lower() == interest.lower() and product["price"] <= budget]

    # Apply simple keyword-based recommendation logic on the filtered catalog
    recommendations = []
    keywords = prompt.lower().split()
    
    for product in filtered_catalog:
        if any(keyword in product["description"].lower() for keyword in keywords):
            recommendations.append(product["name"])
    
    # Generate the response based on the recommendations
    if recommendations:
        response = f"Based on your interest in {interest} and budget of ${budget}, we recommend: {', '.join(recommendations)}."
    else:
        response = "Sorry, we couldn't find any products matching your interests within your budget."

    return response



