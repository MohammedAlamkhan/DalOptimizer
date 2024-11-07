# Optimal Dal Combination for Complete Amino Acid Profile

## Overview
This study optimizes the combination of five different types of dal (Indian lentils) to meet the daily amino acid requirements of an adult male. The optimization aims to provide complete protein nutrition while minimizing total consumption quantity.

## Subject Specifications
- Height: 6 feet (183 cm)
- Weight: 80 kg
- Activity Level: Moderate
- Gender: Male

## Input Data

### Dal Varieties Analyzed
1. Toor Dal (Pigeon Pea)
2. Moong Dal (Green Gram)
3. Chana Dal (Bengal Gram)
4. Masoor Dal (Red Lentil)
5. Urad Dal (Black Gram)

### Nutritional Parameters
- Total Protein
- Essential Amino Acids:
  - Lysine
  - Methionine
  - Cysteine
  - Tryptophan
  - Threonine
  - Leucine
  - Isoleucine
  - Valine
  - Histidine
  - Phenylalanine + Tyrosine

## Methodology

### 1. Requirement Calculation
- Base protein requirement: 0.8g/kg body weight
- Essential amino acid requirements based on WHO/FAO recommendations
- Values scaled for 80kg body weight

### 2. Optimization Approach
- Objective: Meet or exceed all amino acid requirements
- Constraint: Minimize total quantity of dal
- Method: Linear optimization with nutritional constraints
- Proportions adjusted to maintain practical serving sizes

### 3. Assumptions
- All nutritional values are for raw dal
- Bioavailability is considered uniform across dal types
- Cooking losses are not factored
- No consideration for anti-nutritional factors
- Values are for uncooked dal weight

## Results

### Optimal Dal Combination
| Dal Type    | Quantity (g) | Percentage |
|-------------|-------------|------------|
| Toor Dal    | 60          | 21.4%      |
| Moong Dal   | 80          | 28.6%      |
| Chana Dal   | 50          | 17.9%      |
| Masoor Dal  | 40          | 14.3%      |
| Urad Dal    | 50          | 17.9%      |
| **Total**   | **280g**    | **100%**   |

### Nutritional Achievement
| Nutrient                | Required (mg) | Provided (mg) | Achievement % |
|------------------------|---------------|---------------|---------------|
| Protein                | 64000         | 65800         | 102.8%       |
| Lysine                 | 2400          | 4990          | 207.9%       |
| Methionine             | 1120          | 734           | 65.5%        |
| Cysteine               | 1120          | 627           | 56.0%        |
| Tryptophan             | 640           | 650           | 101.6%       |
| Threonine              | 1600          | 2279          | 142.4%       |
| Leucine                | 4720          | 4928          | 104.4%       |
| Isoleucine             | 2000          | 2486          | 124.3%       |
| Valine                 | 2640          | 2923          | 110.7%       |
| Histidine              | 1120          | 1792          | 160.0%       |
| Phenylalanine+Tyrosine | 3360          | 4670          | 139.0%       |

## Limitations

1. **Sulfur Amino Acids**: The combination meets only ~60% of methionine and cysteine requirements
2. **Practical Considerations**: Total quantity (280g) may be high for single-day consumption
3. **Bioavailability**: Actual absorption may vary based on preparation methods and individual factors

## Recommendations

1. **Complementary Foods**: Include cereals (rice, wheat) to address methionine deficiency
2. **Preparation**: Soak and properly cook dal to improve digestibility
3. **Distribution**: Split total quantity into 3-4 meals throughout the day
4. **Individual Adjustment**: Scale quantities based on personal factors (activity level, age, weight)

## Future Work

1. Include cooking methods' impact on amino acid availability
2. Analyze cost optimization while maintaining nutritional adequacy
3. Study seasonal availability impact on optimal combinations
4. Incorporate anti-nutritional factors in the optimization model

## References
- WHO/FAO protein and amino acid requirements in human nutrition
- USDA Food Composition Database
- Indian Food Composition Tables
