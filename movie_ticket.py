print("🎬 Movie Ticket Booking")

movies = ["OG", "Peddi", "Irumudi"]

print("\nAvailable Movies:")
for i, movie in enumerate(movies, start=1):
    print(i, ".", movie)

choice = int(input("\nSelect a movie: "))

if 1 <= choice <= len(movies):
    movie = movies[choice - 1]

    tickets = int(input("Enter number of tickets: "))

    price = 150
    total = tickets * price

    print("\n🎟️ Booking Successful!")
    print("Movie:", movie)
    print("Tickets:", tickets)
    print("Total Amount:", total)

else:
    print("Invalid movie choice!")