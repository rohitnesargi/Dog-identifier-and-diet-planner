import random

def get_size_category(breed_name):
    breed_name = breed_name.lower()

    small_keywords = ["pomeranian", "chihuahua", "toy", "pug", "terrier", "beagle", "corgi", "dachshund"]
    large_keywords = ["retriever", "german shepherd", "husky", "labrador", "mastiff", "dane", "saint bernard", "malamute", "boxer", "doberman"]

    for word in small_keywords:
        if word in breed_name:
            return "small"

    for word in large_keywords:
        if word in breed_name:
            return "large"

    return "medium"

def get_exact_size(breed_name, size_category):
    breed_name = breed_name.replace('_', ' ').title()
    
    # Specific sizes for popular breeds
    sizes = {
        "Golden Retriever": {"weight": "55-75 lbs (25-34 kg)", "height": "21-24 inches (53-61 cm)"},
        "Pug": {"weight": "14-18 lbs (6-8 kg)", "height": "10-13 inches (25-33 cm)"},
        "German Shepherd": {"weight": "50-90 lbs (22-40 kg)", "height": "22-26 inches (55-65 cm)"},
        "Siberian Husky": {"weight": "35-60 lbs (16-27 kg)", "height": "20-24 inches (50-60 cm)"},
        "Chihuahua": {"weight": "2-6 lbs (1-3 kg)", "height": "5-8 inches (13-20 cm)"},
        "Labrador Retriever": {"weight": "55-80 lbs (25-36 kg)", "height": "21.5-24.5 inches (55-62 cm)"},
        "Beagle": {"weight": "20-30 lbs (9-14 kg)", "height": "13-15 inches (33-38 cm)"},
        "Bulldog": {"weight": "40-50 lbs (18-23 kg)", "height": "14-15 inches (35-38 cm)"},
        "Poodle": {"weight": "40-70 lbs (18-32 kg)", "height": "15+ inches (38+ cm)"}
    }
    
    if breed_name in sizes:
        return sizes[breed_name]
        
    # Dynamic generation based on size category if breed is not in the specific list
    if size_category == "small":
        return {"weight": "10-25 lbs (4-11 kg)", "height": "10-15 inches (25-38 cm)"}
    elif size_category == "large":
        return {"weight": "60-100+ lbs (27-45+ kg)", "height": "24-30 inches (60-76 cm)"}
    else:
        return {"weight": "30-55 lbs (13-25 kg)", "height": "16-22 inches (40-55 cm)"}

def generate_diet_plan(breed_name, size):
    # Clean up the breed name for display
    display_name = breed_name.replace('_', ' ').title()
    
    # Specific specialized diets for popular breeds
    specific_diets = {
        "Golden Retriever": {
            "food": f"Premium {display_name} Joint & Coat Formula",
            "meals": "2 large meals per day (morning and evening)",
            "extras": "Salmon oil for coat, boiled carrots, lean chicken"
        },
        "Pug": {
            "food": f"Weight Management {display_name} Kibble",
            "meals": "2 small, strictly portioned meals per day",
            "extras": "Blueberries, green beans (low calorie)"
        },
        "German Shepherd": {
            "food": f"High-Energy {display_name} Performance Diet",
            "meals": "2 large meals per day",
            "extras": "Glucosamine supplements, raw beef chunks, sweet potato"
        },
        "Siberian Husky": {
            "food": f"{display_name} High-Protein Arctic Formula",
            "meals": "2 medium-large meals per day",
            "extras": "Raw fish, boiled eggs, cottage cheese"
        },
        "Chihuahua": {
            "food": f"{display_name} Toy Breed Dental Kibble",
            "meals": "3-4 tiny meals per day to prevent hypoglycemia",
            "extras": "Small pieces of boiled chicken, plain yogurt"
        }
    }
    
    # Return specific if exists
    if display_name in specific_diets:
        return specific_diets[display_name]
        
    # Seed the random generator with the breed name so the output is unique per breed but consistent!
    random.seed(breed_name)
    
    # Dynamic procedural generation based on size and breed name
    food_prefixes = ["High-Protein", "Balanced", "Holistic", "Ancestral", "Grain-Free", "Premium", "Natural"]
    food_suffixes = ["Formula", "Kibble", "Diet", "Blend", "Recipe"]
    
    small_meals = [
        "3 small meals per day to maintain energy",
        "1/4 cup 3x daily to prevent hypoglycemia",
        "Small frequent feedings (3-4 times daily)",
        "2 meals plus 1 healthy midday snack"
    ]
    
    large_meals = [
        "2 large meals per day (Morning & Night)",
        "1 big meal and 1 light evening meal",
        "2 strictly portioned meals to prevent bloat",
        "Scheduled feedings, 12 hours apart"
    ]
    
    medium_meals = [
        "2 balanced meals per day",
        "Morning and evening feedings",
        "1/2 cup twice a day",
        "2 scheduled meals"
    ]
    
    extra_items = [
        "blueberries", "boiled chicken", "carrots", "sweet potatoes",
        "green beans", "plain yogurt", "salmon oil", "cottage cheese",
        "sliced apples", "pumpkin puree", "cooked eggs"
    ]
    
    food_name = f"{random.choice(food_prefixes)} {display_name} Specific {random.choice(food_suffixes)}"
    
    if size == "small":
        meals = random.choice(small_meals)
    elif size == "large":
        meals = random.choice(large_meals)
    else:
        meals = random.choice(medium_meals)
        
    chosen_extras = random.sample(extra_items, 2)
    extras = f"{chosen_extras[0].capitalize()} and {chosen_extras[1]}"
    
    # Restore random state so we don't mess up other random calls in the app
    random.seed()
    
    return {
        "food": food_name,
        "meals": meals,
        "extras": extras
    }
