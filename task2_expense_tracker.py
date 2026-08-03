total = 0
count = 1
print("Expense Tracker")
print("================")

while True:
    try:
        new_expense = int(input(f"Enter expense {count} (0 for stop command): "))
        if new_expense<0:
            print("Expense cannot be negative. Try again.")
            continue
        elif new_expense==0:
            count-=1
            break
        total += new_expense
        count += 1
    except ValueError:
        print("Invalid Data. Try again.")
        continue


print(f"Thank you for using Expense Tracker!\n Total expense: {total}")
print(f"Number of Expenses: {count}")