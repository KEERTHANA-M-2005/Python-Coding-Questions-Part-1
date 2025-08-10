# A cricket batter is dismissed after facing n balls and scores m runs by
# hitting x fours, y sixes, z twos, and w ones. Write a program to calculate
# the strike rate, percentage contribution of each run type, and analyze data
# for p players to determine:
# • The player with the highest strike rate
# • The player who scored maximum runs
# • The player who scored minimum runs
# • The player who hit the most sixes
# • The player who hit the most fours

p = int(input("Enter number of players: "))

players = []

for i in range(p):
    print(f"\nEnter data for Player {i+1}:")
    name = input("Name: ")
    n = int(input("Balls faced: "))
    m = int(input("Total runs: "))
    x = int(input("Number of fours: "))
    y = int(input("Number of sixes: "))
    z = int(input("Number of twos: "))
    w = int(input("Number of ones: "))

    # Strike rate
    strike_rate = (m / n) * 100 if n > 0 else 0

    # Percent contribution of each run type
    four_runs = x * 4
    six_runs = y * 6
    two_runs = z * 2
    one_runs = w * 1

    pct_fours = (four_runs / m * 100) if m > 0 else 0
    pct_sixes = (six_runs / m * 100) if m > 0 else 0
    pct_twos = (two_runs / m * 100) if m > 0 else 0
    pct_ones = (one_runs / m * 100) if m > 0 else 0

    players.append({
        "name": name,
        "runs": m,
        "balls": n,
        "fours": x,
        "sixes": y,
        "strike_rate": strike_rate,
        "pct_fours": pct_fours,
        "pct_sixes": pct_sixes,
        "pct_twos": pct_twos,
        "pct_ones": pct_ones
    })

# Display each player's stats
print("\nPlayer Statistics:")
for player in players:
    print(f"\nName: {player['name']}")
    print(f"Runs: {player['runs']} | Balls: {player['balls']} | Strike Rate: {player['strike_rate']:.2f}")
    print(f"Fours: {player['fours']} ({player['pct_fours']:.2f}%)")
    print(f"Sixes: {player['sixes']} ({player['pct_sixes']:.2f}%)")
    print(f"Twos: {player['pct_twos']:.2f}% | Ones: {player['pct_ones']:.2f}%")

# Analysis
highest_sr = max(players, key=lambda p: p['strike_rate'])
max_runs = max(players, key=lambda p: p['runs'])
min_runs = min(players, key=lambda p: p['runs'])
most_sixes = max(players, key=lambda p: p['sixes'])
most_fours = max(players, key=lambda p: p['fours'])

print("\n--- Analysis ---")
print(f"Highest Strike Rate: {highest_sr['name']} ({highest_sr['strike_rate']:.2f})")
print(f"Maximum Runs: {max_runs['name']} ({max_runs['runs']})")
print(f"Minimum Runs: {min_runs['name']} ({min_runs['runs']})")
print(f"Most Sixes: {most_sixes['name']} ({most_sixes['sixes']})")
print(f"Most Fours: {most_fours['name']} ({most_fours['fours']})")
