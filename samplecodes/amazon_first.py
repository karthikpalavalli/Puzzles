from collections import Counter


def get_recommendations(num_users, users, num_books, books):
    books_to_genre = {value: key for key, values in books.items() for value in values}

    output = dict()

    for user, books in users.items():
        genre_list = [books_to_genre[book] for book in books]

        genre_freq = dict(Counter(genre_list))

        if not genre_freq:
            output[user] = []
            continue

        max_genre = max(genre_freq.values())
        output[user] = [genre for genre, freq in genre_freq.items() if freq == max_genre]

    return output


if __name__ == "__main__":
    test_users = dict()
    test_books = dict()

    test_users["Punith"] = []
    test_users["Karthik"] = ["A", "B", "A", "C"]
    test_books["G1"] = ["A"]
    test_books["G2"] = ["B"]

    print(get_recommendations(len(test_users), test_users, len(test_books), test_books))