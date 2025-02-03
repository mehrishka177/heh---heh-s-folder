def length_converter():
    print("Welcome to the Length Converter App!")
    units = {
        '1': ('Kilometers', 1000),
        '2': ('Meters', 1),
        '3': ('Centimeters', 0.01),
        '4': ('Millimeters', 0.001),
        '5': ('Miles', 1609.34),
        '6': ('Yards', 0.9144),
        '7': ('Feet', 0.3048),
        '8': ('Inches', 0.0254)
    }
    
    print("Select the unit you want to convert from:")
    for key, value in units.items():
        print(f"{key}: {value[0]}")
    
    from_unit = input("Enter the number corresponding to the unit: ")
    if from_unit not in units:
        print("Invalid selection.")
        return
    
    value = float(input("Enter the length value: "))
    
    print("Select the unit you want to convert to:")
    for key, value_name in units.items():
        print(f"{key}: {value_name[0]}")
    
    to_unit = input("Enter the number corresponding to the unit: ")
    if to_unit not in units:
        print("Invalid selection.")
        return
    
    converted_value = value * (units[from_unit][1] / units[to_unit][1])
    print(f"{value} {units[from_unit][0]} is equal to {converted_value:.4f} {units[to_unit][0]}")

if __name__ == "__main__":
    length_converter()