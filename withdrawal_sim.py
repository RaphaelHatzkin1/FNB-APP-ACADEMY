balance = 500

withdrawal = float(input("How much money would you like to withdraw? R"))

if withdrawal <= 0:
    print("Invalid amount. You must withdraw more than R0.")
elif withdrawal <= balance:
    balance -= withdrawal
    print(f"Withdrawal successful! Remaining balance: R{balance}")
else:
    print("Declined. Insufficient funds")