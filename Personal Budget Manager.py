""""""
"""
Problem Statement: You are required to build a Personal Budget Management application. The application will manage budget categories like food, entertainment, utilities, etc., ensuring that budget details remain private and are accessed or modified through public methods.

    - Task 1: Define Budget Category Class
        - Create a class BudgetCategory with private attributes for category name and allocated budget.
        - Initialize these attributes in the constructor.
        - Expected Outcome: A BudgetCategory class capable of storing category details securely.
        
    - Task 2: Implement Getters and Setters
        - Write getter and setter methods for both the category name and the allocated budget.
        - Ensure that the setter methods include validation (e.g., budget should be a positive number).
        - Expected Outcome: Methods that allow controlled access and modification of the private attributes, with validation checks in place.
        
    - Task 3: Add Budget Functionality
        - Implement a method to add expenses to a category and adjust the budget accordingly.
        - Validate the expense amount before making deductions from the budget.
        - Expected Outcome: Ability to track expenses per category and update the remaining budget safely.
        
    - Task 4: Display Budget Details
        - Create a method to display the details of a budget category, including the name, allocated budget, and remaining budget after expenses.
        - Expected Outcome: Users can view a summary of each budget category, showcasing encapsulation in action.
"""


class BudgetCategory:
    def __init__(self, category_name, remaining_budget, allocated_budget):
        self.__category_name = category_name  # Categories like rent, utilities, groceries
        self.__remaining_budget = remaining_budget  # Amount of money allocated to each budget category
        self.__allocated_budget = allocated_budget

    def get_category(self):
        return self.__category_name

    def set_category(self, new_category):
        if new_category.isalpha() and 5 <= len(new_category) <= 18:
            self.__category_name = new_category
        else:
            print("Invalid category input.")

    def get_remaining_budget(self):
        return self.__remaining_budget

    def get_allocated_budget(self):
        return self.__allocated_budget

    def set_remaining_budget(self, new_budget):
        if new_budget > 0:
            self.__remaining_budget = new_budget
        else:
            print("Budget cannot be a negative number.")


def display_budget(budget):
    """Displays the information such as the category name, the planned budget, and the remaining funds after expenses."""
    category = input("What category do you want to see?: ")
    if category in budget:
        print(f"Category: {budget[category].get_category().title()}\nPlanned Budget: ${budget[category].get_allocated_budget()}\nRemaining Funds: ${budget[category].get_remaining_budget()}")


def add_category(budget):
    """Users can add a category to their budget."""
    category = input("Enter the category name: ")
    budget_for_category = float(input("Enter how much you can spend each month: $"))
    remaining_budget_for_category = budget_for_category
    budget[category] = BudgetCategory(category, budget_for_category, remaining_budget_for_category)


def add_expenses(budget):
    """Users can subtract expenses from their budget for a particular category. """
    category = input("Enter the category name: ")
    amount_input = input("Enter the amount spent: ")
    # Validation
    if category in budget:
        amount = float(amount_input)
        updated_budget = budget[category].get_remaining_budget() - amount
        budget[category].set_remaining_budget(updated_budget)
    else:
        print("Invalid Input.")


def main():
    """Displays a menu and takes the user's input to determine which function to perform."""
    budget = {}
    while True:
        action = input("Enter action\n1. Add category\n2. Add expense\n3. Display budget\n4. Exit\n").lower()
        if action == "exit" or action == "4":
            break
        try:
            if action == '1' or action == 'add category':
                add_category(budget)
            elif action == '2' or action == 'add expense':
                add_expenses(budget)
            elif action == '3' or action == 'display budget':
                display_budget(budget)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == '__main__':
    main()

