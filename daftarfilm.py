# Data film
film_list = [
    {
        "judul": "Avengers: Endgame",
        "jam_tayang": "10:00",
        "studio": "Studio 1"
    },
    {
        "judul": "Spider-Man: No Way Home",
        "jam_tayang": "13:00",
        "studio": "Studio 2"
    },
    {
        "judul": "The Batman",
        "jam_tayang": "16:00",
        "studio": "Studio 3"
    },
    {
        "judul": "Doctor Strange",
        "jam_tayang": "19:00",
        "studio": "Studio 1"
    }
]

# Menampilkan daftar film
print("=" * 50)
print("       DAFTAR FILM DAN JADWAL TAYANG")
print("=" * 50)

for i, film in enumerate(film_list, start=1):
    print(f"\nFilm {i}")
    print(f"Judul Film : {film['judul']}")
    print(f"Jam Tayang : {film['jam_tayang']}")
    print(f"Studio     : {film['studio']}")

print("\nTerima kasih telah menggunakan sistem bioskop.")