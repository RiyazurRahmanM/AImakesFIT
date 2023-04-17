def calculate_nutrition_requirements(age, height_cm, weight_kg, activity_level, goal, gender, activity_type):
    # Calculate Basal Metabolic Rate (BMR)
    if gender == 'male':
        bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age + 5
    else:
        bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age - 161
    
    # Determine Total Daily Energy Expenditure (TDEE) based on activity level and type
    activity_level_factors = {
        'sedentary': 1.2,
        'lightly active': 1.375,
        'moderately active': 1.55,
        'very active': 1.725,
        'extra active': 1.9
    }
    activity_type_factors = {
        'cardio': 1.2,
        'weightlifting': 1.5,
        'cycling': 1.4,
        'swimming': 1.6
    }
    tdee = bmr * activity_level_factors[activity_level] * activity_type_factors[activity_type]
    
    # Determine daily macronutrient requirements
    protein_range = (0.8, 1.2)
    protein_grams = weight_kg * protein_range[0] if activity_level == 'sedentary' else weight_kg * protein_range[1]
    if age < 19:
        protein_grams *= 1.2
    elif age < 50:
        protein_grams *= 1.0
    else:
        protein_grams *= 0.8
    carb_calories = tdee * 0.45
    fat_calories = tdee * 0.2
    
    # Calculate daily calorie intake for weight loss or gain
    if goal == 'loss':
        daily_calories = tdee - 500
        if daily_calories < 1200:
            daily_calories = 1200
    elif goal == 'gain':
        daily_calories = tdee + 250
    else:
        daily_calories = tdee
    
    return {
        'protein_grams': protein_grams,
        'carb_calories': carb_calories,
        'fat_calories': fat_calories,
        'daily_calories': daily_calories
    }

age = 30
height_cm = 65
weight_kg = 75
activity_level = 'moderately active'
activity_type = 'weightlifting'
