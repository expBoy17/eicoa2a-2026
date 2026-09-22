# engineer_calc.py
def build_menu():
    """
    Build and return the list of menu options for the Engineering Calculator.
    """
    options = [
        "Calculate Resistance",
        "Convert mm to Inches",
        "Convert Inches to mm",
        "Convert cm to Inches",
        "Convert Inches to cm",
        "Exit"
    ]
    return options

def display_menu():
    options = build_menu()
    print("Engineering Calculator Menu:")
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")
