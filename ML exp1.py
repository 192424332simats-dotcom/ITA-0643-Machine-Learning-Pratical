# FIND-S Algorithm Implementation

# Training dataset
training_data = [
    ['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Rainy', 'Cold', 'High', 'Strong', 'Warm', 'Change', 'No'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Cool', 'Same', 'Yes']
]

def find_s(data):
    
    # Number of attributes (excluding target)
    num_attributes = len(data[0]) - 1
    
    # Initialize hypothesis to most specific
    hypothesis = ['Ø'] * num_attributes
    
    print("Initial Hypothesis:", hypothesis)
    print("=================================")
    
    # Iterate through each training example
    for i, example in enumerate(data):
        
        attributes = example[:-1]
        label = example[-1].lower()
        
        # Consider only positive examples
        if label == 'yes':
            for j in range(num_attributes):
                if hypothesis[j] == 'Ø':
                    hypothesis[j] = attributes[j]
                elif hypothesis[j] != attributes[j]:
                    hypothesis[j] = '?'
        
        print(f"Step {i+1}: {example}")
        print("Current Hypothesis:", hypothesis)
        print("---------------------------------")
    
    return hypothesis


# Run FIND-S Algorithm
final_hypothesis = find_s(training_data)

print("\nFinal Most Specific Hypothesis:")
print(final_hypothesis)
