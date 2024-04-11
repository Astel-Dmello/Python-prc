# Function to convert USD to INR
def usd_to_inr(usd_amount):
    conversion_rate = 74.51  # 1 USD = 74.51 INR (example conversion rate)
    inr_amount = usd_amount * conversion_rate
    return inr_amount

# Input USD amount from the user
usd_amount = float(input("Enter the amount in U.S. dollars: "))

# Convert USD to INR
inr_amount = usd_to_inr(usd_amount)

# Display the result
print(f"{usd_amount} U.S. dollars is equal to {inr_amount:.2f} Indian rupees.")
