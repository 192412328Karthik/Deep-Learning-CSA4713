
# Probability Distributions and Bayes' Theorem

# Part 1: Probability Distribution of a Fair Die
print("1. Probability Distribution")

outcomes = [1, 2, 3, 4, 5, 6]
probability = 1 / len(outcomes)

for outcome in outcomes:
    print("Outcome:", outcome,
          "Probability:", round(probability, 4))

print("Total Probability:", round(probability * len(outcomes), 2))


# Part 2: Bayes' Theorem
print("\n2. Bayes' Theorem")

# Given probabilities
p_disease = 0.01
p_positive_given_disease = 0.90
p_positive_given_no_disease = 0.05

# Calculate total probability of a positive test
p_positive = (
    p_positive_given_disease * p_disease
    + p_positive_given_no_disease * (1 - p_disease)
)

# Apply Bayes' Theorem
p_disease_given_positive = (
    p_positive_given_disease * p_disease
) / p_positive

print("Probability of positive test:",
      round(p_positive * 100, 2), "%")

print("Probability of disease given positive test:",
      round(p_disease_given_positive * 100, 2), "%")
