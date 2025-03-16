def main():
    
    gravity_factors = {
        "mercury": 0.38,
        "venus": 0.91,
        "mars": 0.38,
        "jupiter": 2.34,
        "saturn": 1.06,
        "uranus": 0.92,
        "neptune": 1.19
    }

    earth_weight = float(input("Enter your weight on Earth (kg): "))  
    planet = input("Enter a planet: ").strip().lower() 

    if planet in gravity_factors:  
        new_weight = earth_weight * gravity_factors[planet]  
        print(f"Your weight on {planet.capitalize()} would be: {new_weight:.2f} kg")
    else:
        print("Invalid planet name. Please enter a correct planet.")

main()

