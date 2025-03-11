import numpy as np
import matplotlib.pyplot as plt

# Parameters
average_defaults_per_month = 2  # Average number of loan defaults per month
loan_amount = 100000  # Average loan amount
loss_given_default = 0.5  # Loss given default (percentage of loan amount)
months = 12  # Number of months to simulate

# Simulate loan defaults using Poisson distribution
loan_defaults = np.random.poisson(average_defaults_per_month, months)

# Calculate potential losses
potential_losses = loan_defaults * loan_amount * loss_given_default

# Visualize monthly loan defaults
plt.bar(range(1, months + 1), loan_defaults, color='#8c1c29')
plt.title('Monthly Loan Defaults')
plt.xlabel('Month')
plt.ylabel('Number of Defaults')
plt.grid(False)
plt.show()

# Print potential losses per month
print("Potential Losses per Month:")
for month, loss in enumerate(potential_losses, start=1):
    print(f"Month {month}: ${loss:,.2f}")
