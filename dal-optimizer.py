import pandas as pd
import numpy as np

# Create DataFrame with dal nutritional info
data = {
    'Protein': [22.3, 24.0, 21.0, 25.0, 25.2],
    'Lysine': [1670, 1930, 1510, 1900, 1900],
    'Methionine': [270, 370, 220, 230, 220],
    'Cysteine': [220, 250, 210, 200, 240],
    'Tryptophan': [240, 240, 230, 250, 200],
    'Threonine': [800, 860, 760, 850, 800],
    'Leucine': [1750, 1870, 1680, 1800, 1700],
    'Isoleucine': [860, 900, 850, 930, 900],
    'Valine': [1050, 1080, 970, 1120, 1000],
    'Histidine': [670, 610, 610, 630, 680],
    'Phe_Tyr': [1740, 1700, 1500, 1650, 1750]
}

dals = ['Toor', 'Moong', 'Chana', 'Masoor', 'Urad']
df = pd.DataFrame(data, index=dals)

# Daily requirements for 80kg man
requirements = {
    'Protein': 64000,
    'Lysine': 2400,
    'Methionine': 1120,
    'Cysteine': 1120,
    'Tryptophan': 640,
    'Threonine': 1600,
    'Leucine': 4720,
    'Isoleucine': 2000,
    'Valine': 2640,
    'Histidine': 1120,
    'Phe_Tyr': 3360
}

# Function to calculate nutritional values for given proportions
def calculate_nutrition(proportions):
    total = sum(proportions)
    if total == 0:
        return None
    normalized = [p/total for p in proportions]
    result = {}
    for nutrient in df.columns:
        result[nutrient] = sum(df[nutrient] * normalized) * total
    return result

# Try different combinations
best_proportions = [60, 80, 50, 40, 50]  # Starting point in grams
best_result = calculate_nutrition(best_proportions)

# Calculate and format results
final_result = calculate_nutrition(best_proportions)
total_grams = sum(best_proportions)

# Create results table
results_data = {
    'Dal Type': dals,
    'Quantity (g)': best_proportions,
    'Percentage': [f"{(p/total_grams*100):.1f}%" for p in best_proportions]
}

result_df = pd.DataFrame(results_data)
print("\nOptimal Dal Combination:")
print(result_df.to_string(index=False))

# Create nutrition comparison table
nutrition_data = {
    'Nutrient': list(requirements.keys()),
    'Required': list(requirements.values()),
    'Provided': [final_result[n] for n in requirements.keys()],
    'Percentage Met': [f"{(final_result[n]/requirements[n]*100):.1f}%" for n in requirements.keys()]
}

nutrition_df = pd.DataFrame(nutrition_data)
print("\nNutritional Analysis:")
print(nutrition_df.to_string(index=False))
