import csv
import sys
from funcy import print_durations

# Maps names to a set of corresponding person_ids
names = {}

# Maps person_ids to a dictionary of: name, birth, movies (a set of movie_ids)
people = {}

# Maps movie_ids to a dictionary of: title, year, stars (a set of person_ids)
movies = {}


class Node:
    def __init__(self, value=None, parent=None, neighbours=[], film = None) -> None:
        self.value = value
        self.parent = parent
        self.neighbours = neighbours
        self.film = film

    def __str__(self) -> str:
        return f"""
Value: {self.value}
Parent: {self.parent}
Neighbours: {self.neighbours}
Movie: {self.film}
        """


@print_durations()
def load_data(directory):
    """
    Load data from CSV files into memory.
    """
    # Load people
    with open(f"{directory}/people.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            people[row["id"]] = {
                "name": row["name"],
                "birth": row["birth"],
                "movies": set()
            }
            if row["name"].lower() not in names:
                names[row["name"].lower()] = {row["id"]}
            else:
                names[row["name"].lower()].add(row["id"])

    # Load movies
    with open(f"{directory}/movies.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            movies[row["id"]] = {
                "title": row["title"],
                "year": row["year"],
                "stars": set()
            }

    # Load stars
    with open(f"{directory}/stars.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                people[row["person_id"]]["movies"].add(row["movie_id"])
                movies[row["movie_id"]]["stars"].add(row["person_id"])
            except KeyError:
                pass


def main():
    if len(sys.argv) > 2:
        sys.exit("Usage: python degrees.py [directory]")
    directory = sys.argv[1] if len(sys.argv) == 2 else "SixDegrees\\small"
    # Load data from files into memory
    print("Loading data...")
    load_data(directory)
    print("Data loaded.")

    source = person_id_for_name(input("Name: "))
    # source = person_id_for_name("Kevin Bacon")
    if source is None:
        sys.exit("Person not found.")
    target = person_id_for_name(input("Name: "))
    # target = person_id_for_name("Tom Hanks")
    if target is None:
        sys.exit("Person not found.")

    path = shortest_path(source, target)
    print(path)
    if path is None:
        print("Not connected.")
    else:
        degrees = len(path)
        print(f"{degrees} degrees of separation.")
        path = [(None, source)] + path
        for i in range(degrees):
            person1 = people[path[i][1]]["name"]
            person2 = people[path[i + 1][1]]["name"]
            movie = movies[path[i + 1][0]]["title"]
            print(f"{i + 1}: {person1} and {person2} starred in {movie}")


@print_durations()
def shortest_path(source, target):
    """
    Returns the shortest list of (movie_id, person_id) pairs
    that connect the source to the target.

    If no possible path, returns None.
    """
    StartNode = Node(value=source)
    ActualNode = StartNode
    EndNode = Node(value=target)
    visited = []
    future = []
    ans = []
    seen = set(ActualNode.value)
    future.append(ActualNode)
    while future:
        ActualNode.neighbours = neighbors_for_person(ActualNode.value)
        visited.append(ActualNode.value)
        future.pop(0)
        if ActualNode.value == EndNode.value:
            while ActualNode != StartNode:
                # for pos in ActualNode.neighbours:
                    # if ActualNode.value == pos[1]:
                    #     ans.append(pos)
                    #     break
                ans.append((ActualNode.film, ActualNode.value))
                ActualNode = ActualNode.parent
            return list(reversed(ans))
        for personFilm in ActualNode.neighbours:
            temp = Node(value=personFilm[1], parent=ActualNode, film=personFilm[0])
            if temp.value in seen or temp.value in visited:
                continue
            elif temp.value == EndNode.value:
                ActualNode = temp
                break
            seen.add(temp.value)
            future.append(temp)
        ActualNode = future[0] if (ActualNode.value != EndNode.value and len(future) != 0) else ActualNode

    return None

@print_durations()
def person_id_for_name(name):
    """
    Returns the IMDB id for a person's name,
    resolving ambiguities as needed.
    """
    person_ids = list(names.get(name.lower(), set()))
    if len(person_ids) == 0:
        return None
    elif len(person_ids) > 1:
        print(f"Which '{name}'?")
        for person_id in person_ids:
            person = people[person_id]
            name = person["name"]
            birth = person["birth"]
            print(f"ID: {person_id}, Name: {name}, Birth: {birth}")
        try:
            person_id = input("Intended Person ID: ")
            if person_id in person_ids:
                return person_id
        except ValueError:
            pass
        return None
    else:
        return person_ids[0]

@print_durations()
def neighbors_for_person(person_id):
    """
    Returns (movie_id, person_id) pairs for people
    who starred with a given person.
    """
    movie_ids = people[person_id]["movies"]
    neighbors = set()
    for movie_id in movie_ids:
        for person_id in movies[movie_id]["stars"]:
            neighbors.add((movie_id, person_id))
    return neighbors


if __name__ == "__main__":
    main()
