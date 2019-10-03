"""
bond.py
Pick a Bond movie and it'll tell you how much it grossed adjusted for inflation
"""

import sys
from easymoney.money import EasyPeasy

movies = {
    "Skyfall"                           :"304360277,2012",
    "Spectre"                           :"200074609,2015",
    "Quantum of Solace"                 :"168368427,2008",
    "Casino Royale"                     :"167445960,2006",
    "Die Another Day"                   :"160942139,2002",
    "The World Is Not Enough"           :"126943684,1999",
    "Tomorrow Never Dies"               :"125304276,1997",
    "GoldenEye"                         :"106429941,1995",
    "Moonraker"                         :"70308099,1979",
    "Octopussy"                         :"67893619,1983",
    "Thunderball"                       :"63595658,1965",
    "Never Say Never Again"             :"55432841,1983",
    "For Your Eyes Only"                :"54812802,1981",
    "The Living Daylights"              :"51185897,1987",
    "Goldfinger"                        :"51081062,1964",
    "A View to a Kill"                  :"50327960,1985",
    "The Spy Who Loved Me"              :"46838673,1977",
    "Diamonds Are Forever"              :"43819547,1971",
    "You Only Live Twice"               :"43084787,1967",
    "Live and Let Die"                  :"35377836,1973",
    "Licence to Kill"                   :"34667015,1989",
    "From Russia, with Love"            :"24796765,1964",
    "On Her Majesty's Secret Service"   :"22774493,1969",
    "The Man with the Golden Gun"       :"20972000,1974",
    "Dr. No"                            :"16067035,1963"
}

ep = EasyPeasy()

while True:
    try:
        movie = input("Please type a Bond Movie (e.g., Skyfall): ")
    except EOFError:
        sys.exit(0)

    try:
        definition = movies[movie]
    except KeyError:
        print(f'Sorry, "{movie}" is not a James Bond movie.')
        print()
        continue   #Go back up to the word "while".

    selected_movie = str({definition})
    gross,release_yr = selected_movie.split(",")
    a,gross = gross.split("'")
    release_yr,b = release_yr.split("'")
    amount = int(gross)
    rl = int(release_yr)
    print("adjusted for inflation grossed:")
    adjusted_gross = ep.normalize(amount=amount,region="CA", base_currency="USD",from_year=rl, to_year=2019, pretty_print=True)    
