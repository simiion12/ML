import matplotlib.pyplot as plt
import numpy as np

# Generating a more complex learning curve for a well-fitted model
training_sizes = np.linspace(10, 100, 15)
training_accuracy = np.linspace(0.5, 0.9, 15)  # Training accuracy starts low and improves
validation_accuracy = training_accuracy - 0.1 + (np.random.rand(15) - 0.5) * 0.02  # Initial larger gap that closes

# Introduce an early growth diagonal with a bit more gap at the beginning
training_accuracy[:5] += np.linspace(0, 0.1, 5)
validation_accuracy[:5] += np.linspace(0.05, 0.08, 5)

# Close the gap towards the end of the curve
validation_accuracy[-5:] = training_accuracy[-5:] - (np.random.rand(5) * 0.02)

# Ensure validation accuracy doesn't exceed training accuracy
validation_accuracy = np.clip(validation_accuracy, None, training_accuracy)

# Add some random noise to simulate real-world data
training_accuracy += (np.random.rand(15) - 0.5) * 0.02
validation_accuracy += (np.random.rand(15) - 0.5) * 0.02

# Plotting the learning curve
plt.figure(figsize=(10, 6))
plt.plot(training_sizes, training_accuracy, label='Training accuracy', color='red')
plt.plot(training_sizes, validation_accuracy, label='Validation accuracy', color='green')
plt.title('Learning Curve Demonstrating Good fit Model')
plt.xlabel('Training examples', fontsize=14, labelpad=20)  # Adjust the font size as needed
plt.ylabel('Accuracy', fontsize=14)
plt.legend()
plt.grid(True)
plt.show()
