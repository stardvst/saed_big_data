import collections


def get_lines(file_name):
    with open(file_name) as f:
        return f.read().split()


def get_names(file_name):
    return set(get_lines(file_name))


def unique_sorted(file_name):
    return sorted(set(map(int, data)))


def get_author2films(file_name):
    author2films = collections.defaultdict(list)
    with open(file_name) as f:
        stripped_lines = (line.strip() for line in f)
        for line in stripped_lines:
            film, author = line.split(', ')
            author2films[author].append(film)
    return author2films


def get_films_of(author2films, author):
    return author2films.get(author)


if __name__ == '__main__':
    # 1. Two text files are provided. Each of them contains names in each line.
    # Find all names in the first file that aren't in the second file.
    names1 = get_names('names1.txt')
    names2 = get_names('names2.txt')
    print(names1 - names2)

    # 2. Given a file containing a number in each line. Read the line, remove
    # duplicates and sort the numbers.
    data = get_lines('numbers.txt')
    print(unique_sorted(data))

    # 3. Given file containing file name and author in each line, find all
    # films for given author. Author names will be passed by keyboard.
    author2films = get_author2films('film2author.txt')
    print('Enter author name: ', end='')
    author = input()
    print(get_films_of(author2films, author))
