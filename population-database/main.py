# population_queries.py
# Name Wolfgang Meyer
# Date 4-21-25
# Population Database Query Program
# SDEV 1200

import sqlite3

def main():
    conn = sqlite3.connect('cities.db')
    cur = conn.cursor()

    while True:
        print("\nPopulation Database Menu")
        print("1. Display cities sorted by population (ascending)")
        print("2. Display cities sorted by population (descending)")
        print("3. Display cities sorted by name")
        print("4. Display total population")
        print("5. Display average population")
        print("6. Display city with highest population")
        print("7. Display city with lowest population")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            display_sorted_by_population(cur, ascending=True)
        elif choice == '2':
            display_sorted_by_population(cur, ascending=False)
        elif choice == '3':
            display_sorted_by_name(cur)
        elif choice == '4':
            display_total_population(cur)
        elif choice == '5':
            display_average_population(cur)
        elif choice == '6':
            display_highest_population_city(cur)
        elif choice == '7':
            display_lowest_population_city(cur)
        elif choice == '8':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

    conn.close()

def display_sorted_by_population(cur, ascending=True):
    order = 'ASC' if ascending else 'DESC'
    cur.execute(f"SELECT CityName, Population FROM Cities ORDER BY Population {order}")
    rows = cur.fetchall()
    print("\nCities sorted by population:")
    for row in rows:
        print(f"{row[0]:20}{row[1]:,.0f}")

def display_sorted_by_name(cur):
    cur.execute("SELECT CityName, Population FROM Cities ORDER BY CityName")
    rows = cur.fetchall()
    print("\nCities sorted by name:")
    for row in rows:
        print(f"{row[0]:20}{row[1]:,.0f}")

def display_total_population(cur):
    cur.execute("SELECT SUM(Population) FROM Cities")
    total = cur.fetchone()[0]
    print(f"\nTotal population of all cities: {total:,.0f}")

def display_average_population(cur):
    cur.execute("SELECT AVG(Population) FROM Cities")
    average = cur.fetchone()[0]
    print(f"\nAverage population of all cities: {average:,.0f}")

def display_highest_population_city(cur):
    cur.execute("SELECT CityName, Population FROM Cities ORDER BY Population DESC LIMIT 1")
    row = cur.fetchone()
    print(f"\nCity with the highest population: {row[0]} ({row[1]:,.0f})")

def display_lowest_population_city(cur):
    cur.execute("SELECT CityName, Population FROM Cities ORDER BY Population ASC LIMIT 1")
    row = cur.fetchone()
    print(f"\nCity with the lowest population: {row[0]} ({row[1]:,.0f})")

if __name__ == '__main__':
    main()
