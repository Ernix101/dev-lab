import pandas as pd

pokemon_file_path = "C:/dev-lab/tutorials/pandas-intro/pokemon-2.csv"  # !!!THIS IS A DIFFERENT CSV

df = pd.read_csv(pokemon_file_path)

# Filtering = Keeping the rows that match a condition

healthy_pokemon = df[df["HP"] >= 80]            # Above 80 is a really healthy one
strong_pokemon = df[df["Attack"] >= 90]         # Best strength is in attack above 90
generation2_pokemon = df[df["Generation"] == 2]
# water_pokemon = df[df["Type1"] == "Water"]            # If you're looking with one criteria of type1
water_pokemon = df[(df["Type 1"] == "Water") | 
                   (df["Type 2"] == "Water")]           # If Type 1 or Type 2 is Water, return it. "|" - or logical operator

ff_pokemon = df[(df["Type 1"] == "Fire") &
                (df["Type 2"] == "Flying")]                # If a pokemon's Type 1 is Fire and Type 2 is Flying

print(ff_pokemon)
