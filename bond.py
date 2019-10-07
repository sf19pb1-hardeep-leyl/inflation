"""
bond.py
Pick a Bond movie and it'll tell you how much it grossed adjusted for inflation.
"""

import sys
from easymoney.money import EasyPeasy

movies = {
    "Skyfall":                         (2012, 304_360_277),
    "Spectre":                         (2015, 200_074_609),
    "Quantum of Solace":               (2008, 168_368_427),
    "Casino Royale":                   (2006, 167_445_960),
    "Die Another Day":                 (2002, 160_942_139),
    "The World Is Not Enough":         (1999, 126_943_684),
    "Tomorrow Never Dies":             (1997, 125_304_276),
    "GoldenEye":                       (1995, 106_429_941),
    "Moonraker":                       (1979,  70_308_099),
    "Octopussy":                       (1983,  67_893_619),
    "Thunderball":                     (1965,  63_595_658),
    "Never Say Never Again":           (1983,  55_432_841),
    "For Your Eyes Only":              (1981,  54_812_802),
    "The Living Daylights":            (1987,  51_185_897),
    "Goldfinger":                      (1964,  51_081_062),
    "A View to a Kill":                (1985,  50_327_960),
    "The Spy Who Loved Me":            (1977,  46_838_673),
    "Diamonds Are Forever":            (1971,  43_819_547),
    "You Only Live Twice":             (1967,  43_084_787),
    "Live and Let Die":                (1973,  35_377_836),
    "Licence to Kill":                 (1989,  34_667_015),
    "From Russia, with Love":          (1964,  24_796_765),
    "On Her Majesty's Secret Service": (1969,  22_774_493),
    "The Man with the Golden Gun":     (1974,  20_972_000),
    "Dr. No":                          (1963,  16_067_035)
}

ep = EasyPeasy()

while True:
    try:
        movie = input("Please type a Bond Movie (e.g., Skyfall): ")
    except EOFError:
        sys.exit(0)

    try:
        release_year, gross = movies[movie] #movies[movie] is a tuple, release_year and gross are ints
    except KeyError:
        print(f'Sorry, "{movie}" is not a James Bond movie.')
        print()
        continue   #Go back up to the word "while".

    adjusted_gross = ep.normalize(
        amount = gross,
        region = "US",
        base_currency = "USD",
        from_year = release_year,
        to_year = 2018
    )

    print(f"Adjusted for inflation, grossed ${adjusted_gross:,.2f}")
    print()
