import copy

# Training Dataset (Given Data)
training_data = [
    ['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Rainy', 'Cold', 'High', 'Strong', 'Warm', 'Change', 'No'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Cool', 'Same', 'Yes']
]

# Check if hypothesis is consistent with example
def is_consistent(h, x):
    for i in range(len(h)):
        if h[i] != '?' and h[i] != x[i]:
            return False
    return True


# Check if h1 is more general than h2
def more_general(h1, h2):
    for x, y in zip(h1, h2):
        if x != '?' and x != y:
            return False
    return True


def candidate_elimination(data):
    num_attr = len(data[0]) - 1

    # Initialize S and G
    S = ['Ø'] * num_attr
    G = [['?'] * num_attr]

    print("Initial S:", S)
    print("Initial G:", G)
    print("====================================")

    for example in data:
        x = example[:-1]
        label = example[-1].lower()

        if label == 'yes':  # Positive Example
            
            # Remove inconsistent hypotheses from G
            G = [g for g in G if is_consistent(g, x)]

            # Generalize S minimally
            for i in range(num_attr):
                if S[i] == 'Ø':
                    S[i] = x[i]
                elif S[i] != x[i]:
                    S[i] = '?'

        elif label == 'no':  # Negative Example
            
            new_G = []
            for g in G:
                if is_consistent(g, x):
                    for i in range(num_attr):
                        if g[i] == '?':
                            if S[i] != '?' and S[i] != 'Ø':
                                new_h = copy.deepcopy(g)
                                new_h[i] = S[i]
                                new_G.append(new_h)
                else:
                    new_G.append(g)

            G = new_G

        print("Example:", example)
        print("S:", S)
        print("G:", G)
        print("------------------------------------")

    return S, G


# Run Algorithm
final_S, final_G = candidate_elimination(training_data)

print("\nFinal Specific Boundary (S):", final_S)
print("Final General Boundary (G):", final_G)
