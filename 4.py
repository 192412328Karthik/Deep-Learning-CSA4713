
import math

# Actual and predicted probability distributions
P = [0.7, 0.3]
Q = [0.6, 0.4]

entropy = 0
cross_entropy = 0
kl_divergence = 0

for p, q in zip(P, Q):
    entropy -= p * math.log2(p)
    cross_entropy -= p * math.log2(q)
    kl_divergence += p * math.log2(p / q)

print("Actual Distribution:", P)
print("Predicted Distribution:", Q)
print("Entropy:", round(entropy, 4), "bits")
print("Cross-Entropy:", round(cross_entropy, 4), "bits")
print("KL Divergence:", round(kl_divergence, 4), "bits")
