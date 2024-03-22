def promptResponse(prompt, interest):
    """
    Generate personalized recommendations based on a user's prompt and selected interest area.

    Parameters:
    - prompt (str): User's text input describing what they are looking for.
    - interest (str): User's selected interest area (e.g., "Toys", "Games").

    Returns:
    - str: A response message with recommendations or a message indicating no matches were found.
    """
    # Mock data for demonstration purposes
    PRODUCT_CATALOG = [
        {"name": "Soft Plush Teddy Bear", "category": "Baby", "description": "A cuddly teddy bear for babies and toddlers. Perfect for snuggling!", "price": 15.99, "tags": ["plush", "cute", "toy"]},
        {"name": "Interactive Baby Activity Gym", "category": "Baby", "description": "An engaging activity gym with hanging toys for sensory development. Keeps babies entertained for hours!", "price": 39.99, "tags": ["baby", "development", "activity"]},
        {"name": "Educational Alphabet Blocks", "category": "Baby", "description": "Colorful alphabet blocks for early learning and fine motor skills. Helps babies learn while having fun!", "price": 24.99, "tags": ["alphabet", "educational", "blocks"]},
        {"name": "Family Board Game Bundle", "category": "Games", "description": "A collection of classic board games for family game nights. Enjoy quality time with loved ones!", "price": 49.99, "tags": ["family", "board game", "bundle"]},
        {"name": "Challenging 1000-Piece Puzzle", "category": "Games", "description": "A beautifully illustrated puzzle to challenge your mind. Perfect for puzzle enthusiasts!", "price": 19.99, "tags": ["puzzle", "art", "challenge"]},
        {"name": "Educational Science Experiment Kit", "category": "Games", "description": "Perform exciting science experiments at home with this kit. Learn while having fun!", "price": 29.99, "tags": ["science", "educational", "experiment"]},
        {"name": "Movie Night Popcorn Maker", "category": "Entertainment", "description": "Make movie nights more enjoyable with freshly popped popcorn!", "price": 29.99, "tags": ["movie", "popcorn", "entertainment"]},
        {"name": "Karaoke Machine", "category": "Entertainment", "description": "Sing your heart out with friends and family with this karaoke machine!", "price": 99.99, "tags": ["karaoke", "music", "entertainment"]},
        {"name": "Outdoor Adventure Set", "category": "Entertainment", "description": "Encourage outdoor exploration and adventure with this fun set!", "price": 39.99, "tags": ["outdoor", "adventure", "fun"]},
        {"name": "Language Learning Book Set", "category": "Learning", "description": "Enhance language skills with this comprehensive book set for beginners.", "price": 49.99, "tags": ["language", "learning", "book"]},
        {"name": "Mathematics Workbook", "category": "Learning", "description": "Sharpen math skills with this workbook covering various topics.", "price": 19.99, "tags": ["mathematics", "learning", "workbook"]},
        {"name": "Seasonal Decorations Bundle", "category": "Seasonal", "description": "Get into the festive spirit with this bundle of seasonal decorations.", "price": 59.99, "tags": ["seasonal", "decorations", "festive"]},
        {"name": "Summer Beach Toys Set", "category": "Seasonal", "description": "Have fun in the sun with these beach toys perfect for summer!", "price": 29.99, "tags": ["summer", "beach", "toys"]},
    ]

    # Convert interest to lowercase for case-insensitive comparison
    interest = interest.lower()

    # Check if the provided interest category matches any available categories
    available_categories = set(product["category"].lower() for product in PRODUCT_CATALOG)
    if interest not in available_categories:
        return "Sorry, the provided interest category is not available."

    # Apply simple keyword-based recommendation logic on the product catalog
    recommendations = []
    keywords = prompt.lower().split()
    
    for product in PRODUCT_CATALOG:
        if interest.lower() == product["category"].lower() and any(keyword in product["description"].lower() for keyword in keywords):
            recommendations.append(product)
    
    # Generate the response based on the recommendations
    if recommendations:
        response = f"Based on your interest in {interest}, we recommend:\n"
        for item in recommendations:
            response += f"- {item['name']}: {item['description']} (Price: ${item['price']})\n"
    else:
        response = "Sorry, we couldn't find any products matching your interests."

    return response






