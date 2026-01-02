import pandas as pd

def search_pokemon():
    """Simple Pokemon search application"""
    
    # Load the Pokemon dataset
    try:
        df = pd.read_csv('pokemon.csv', index_col='Name')
        print("Pokemon database loaded successfully!")
        print(f"Total Pokemon available: {len(df)}\n")
    except FileNotFoundError:
        print("Error: pokemon.csv file not found!")
        return
    
    # Main search loop
    while True:
        pokemon = input("Enter Pokemon Name (or 'quit' to exit): ").strip()
        
        # Exit condition
        if pokemon.lower() in ['quit', 'exit', 'q']:
            print("Thanks for using Pokemon Search!")
            break
        
        # Skip empty input
        if not pokemon:
            continue
        
        # Search for Pokemon (case-insensitive)
        try:
            # Try exact match first
            result = df.loc[pokemon]
            print("\n" + "="*50)
            print(f"Pokemon Found: {pokemon}")
            print("="*50)
            print(result.to_string())
            print("="*50 + "\n")
        except KeyError:
            # Try case-insensitive search
            matches = df.index[df.index.str.lower() == pokemon.lower()]
            if len(matches) > 0:
                result = df.loc[matches[0]]
                print("\n" + "="*50)
                print(f"Pokemon Found: {matches[0]}")
                print("="*50)
                print(result.to_string())
                print("="*50 + "\n")
            else:
                print(f"\n {pokemon} not found in database.\n")

if __name__ == "__main__":  #? ensure this runs only when executed directly
    print("="*50)
    print("         POKEMON SEARCH APPLICATION")
    print("="*50 + "\n")
    search_pokemon()