from typing import List


class MovieRentingSystem:
    movies = [[]]  # [[shop i, movie i, price i]] (sorted by price)
    shops = 0
    rent_state = {}  # __movie_key : [0/1, price]
    movie_shops = {}  # movie : [[shop i, price i]] (sorted by price)
    rented = {}  # price : [[shop i, movie i]]

    def __init__(self, n: int, entries: List[List[int]]):
        # entries[i] = [shop i, movie i, price i]

        self.movies = entries
        self.shops = n
        self.movies = sorted(self.movies, key=lambda x: x[2])
        self.rented = {}

        self.rent_state = {}
        for movie in self.movies:
            self.rent_state[self.__movie_key(movie[0], movie[1])] = [
                0, movie[2]]

        self.movie_shops = {}
        for movie in self.movies:
            if movie[1] in self.movie_shops:
                self.movie_shops[movie[1]].append([movie[0], movie[2]])
            else:
                self.movie_shops[movie[1]] = [[movie[0], movie[2]]]

    def search(self, movie: int) -> List[int]:
        selected = []

        if not movie in self.movie_shops.keys():
            return []

        for entry in self.movie_shops[movie]:
            if len(selected) == 5:
                break
            shop = entry[0]
            price = entry[1]
            if self.rent_state[self.__movie_key(shop, movie)][0] == 1:
                continue
            selected.append([shop, movie, price])

        selected = sorted(selected, key=lambda x: (x[2], x[0]))
        output = []
        for entry in selected:
            output.append(entry[0])
        return output

    def rent(self, shop: int, movie: int) -> None:
        self.rent_state[self.__movie_key(shop, movie)][0] = 1

        price = self.rent_state[self.__movie_key(shop, movie)][1]
        if price in self.rented:
            self.rented[price].append([shop, movie])
        else:
            self.rented[price] = [[shop, movie]]

    def drop(self, shop: int, movie: int) -> None:
        self.rent_state[self.__movie_key(shop, movie)][0] = 0

        price = self.rent_state[self.__movie_key(shop, movie)][1]
        self.rented[price].remove([shop, movie])

    def report(self) -> List[List[int]]:
        output = []

        prices = sorted(list(self.rented.keys()))
        for price in prices:
            movies = self.rented[price]
            if movies:
                movies = sorted(movies, key=lambda x: (x[0], x[1]))
            for movie in movies:
                if len(output) == 5:
                    break
                else:
                    output.append(movie)

        return output

    def __movie_key(self, shop: int, movie: int) -> str:
        return f'{shop}-{movie}'  # Shop - Movie

    # Your MovieRentingSystem object will be instantiated and called as such:
    # obj = MovieRentingSystem(n, entries)
    # param_1 = obj.search(movie)
    # obj.rent(shop,movie)
    # obj.drop(shop,movie)
    # param_4 = obj.report()
