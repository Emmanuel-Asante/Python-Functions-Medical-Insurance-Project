# Create calculate_insurance_cost() function below: 
def calculate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
  estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
  message = "The estimated insurance cost for " + name + " is " + str(estimated_cost) + " dollars."
  print(message)
  return (message, estimated_cost)

# Calculate the difference in insurance costs for a given two individuals
def calculate_difference_in_insurance_costs(cost1, cost2):
  difference = abs(cost1 - cost2)
  print("The difference in insurance cost is " + str(difference) + " dollars.")
  return difference


# Estimate Maria's insurance cost
maria_insurance_cost = calculate_insurance_cost(name = "Maria", age = 28, sex = 0, bmi = 26.2, num_of_children = 3, smoker = 0)

# Estimate Omar's insurance cost 
omar_insurance_cost = calculate_insurance_cost(name = "Omar", age = 35, sex = 1, bmi = 22.2, num_of_children = 0, smoker = 1)

# Estimate my own insurance cost
my_insurance_cost = calculate_insurance_cost(name = "Emmanuel", age = 26, sex = 1, bmi = 26.2, num_of_children = 0, smoker = 0)

# Display a new line
print("\n")

# Difference in insurance costs for Maria and Omar
difference_in_insurance_cost_maria_omar = calculate_difference_in_insurance_costs(5469.0, 28336.0)

# Difference in insurance costs for Emmanuel and Omar
difference_in_insurance_cost_emmanuel_and_omar = calculate_difference_in_insurance_costs(3566.0, 28336.0)

# Difference in insurance costs for Emmanuel and Maria
difference_in_insurance_cost_emmanuel_and_maria = calculate_difference_in_insurance_costs(3566.0, 5469.0)