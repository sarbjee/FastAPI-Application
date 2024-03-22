def promptResponse(prompt):
    # Mock data for demonstration purposes
    PRODUCT_CATALOG = [
        {"name": "Action Figure", "category": "Toys", "description": "An action figure for ages 5 and up."},
        {"name": "Board Game", "category": "Games", "description": "A fun board game for the whole family."},
        {"name": "Puzzle", "category": "Games", "description": "A challenging 1000-piece puzzle."},
    ]

    # Simple keyword-based recommendation logic
    recommendations = []
    keywords = prompt.lower().split()
    
    for product in PRODUCT_CATALOG:
        if any(keyword in product["description"].lower() for keyword in keywords):
            recommendations.append(product["name"])
    
    if recommendations:
        response = f"Based on your interest, we recommend: {', '.join(recommendations)}."
    else:
        response = "Sorry, we couldn't find any products matching your interests."

    return response


