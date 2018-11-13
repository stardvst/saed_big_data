""" Shortest path between words. """


def shortest_apth(word_1, word_2, words):
    """ Return shortest path. """
    if len(word_1) != len(word_2) or not words:
        return None

    visited = set()
    cur_layer = [word_1]
    depth = 0

    parent_dict = {"cat": None}

    while cur_layer:
        next_layer = []
        for word in cur_layer:

            # found the end word
            if word == word_2:

                # construct path and print it
                path = [word_2]
                while parent_dict[word_2]:
                    word_2 = parent_dict[word_2]
                    path.append(word_2)
                while path:
                    print(path.pop(), end=' -> ')
                print('None')
                return depth

            visited.add(word)
            diff = words[word] - visited
            for child in diff:
                parent_dict[child] = word
                # next_layer.extend(w for w in words[w] if w not in visited)
                next_layer.extend(diff)
        depth += 1
        cur_layer = next_layer

    return None


GRAPH = {"put": set(["cut", "but"]),
         "but": set(["cut", "put", "bug"]),
         "cut": set(["but", "cat", "put"]),
         "cat": set(["cut"]),
         "bug": set(["but", "big"]),
         "big": set(["bug"])}
print(shortest_apth('cat', 'big', GRAPH))


# print path, find all sp, merge visited and parent_dict, networkx
