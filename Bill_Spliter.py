def split_expenses(total_expense, num_people):
    total_expense_with_tip = total_expense * 1.05  # Adding 5% tip
    total_expense_with_gst = total_expense_with_tip * 1.18  # Adding 18% GST
    
    each_owe = total_expense_with_gst / num_people
    return total_expense_with_gst, each_owe

try:
    total_expense = float(input("Enter the total expense: $"))
    num_people = int(input("Enter the number of people: "))
    
    if num_people <= 0:
        print("The Number of people must be greater that 0\n")
    else:
        total_expense_with_gst, each_owe = split_expenses(total_expense, num_people)


        print("\n---- Bill ----")
        print(f"Bill Amount: ${total_expense // 1}")
        print(f"Tip (5%): ${total_expense * 0.05 // 1}")
        print(f"GST (18%): ${total_expense * 0.18 // 1}")
        print(f"Total Amount (incl. tip and GST): ${total_expense_with_gst // 1}")
        print(f"Each person owes: ${each_owe // 1}")
except ValueError:
    print("Invalid input. Please enter a valid number.")
