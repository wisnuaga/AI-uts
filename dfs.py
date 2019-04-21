map =  {'A':set(['B']),
         'B':set(['C','A']),
         'C':set(['B','I','H','D']),
         'D':set(['C','E','H','F']),
         'E':set(['D']),
         'F':set(['D','G']),
         'G':set(['F','H']),
         'H':set(['D','C','G','L']),
         'I':set(['C','J','K']),
         'J':set(['I']),
         'K':set(['L','I']),
         'L':set(['K','H'])}

map_2 = {
    'A':set(['C', 'B']),
    'B':set(['A', 'E']),
    'C':set(['K', 'F', 'D', 'A']),
    'D':set(['C', 'J', 'E']),
    'E':set(['B', 'D', 'H']),
    'F':set(['C', 'G']),
    'G':set(['F', 'J']),
    'H':set(['E', 'I']),
    'I':set(['H', 'J', 'L']),
    'J':set(['D', 'G', 'I']),
    'K':set(['C']),
    'L':set(['I'])}


def dfs(map, start, finish):
    stack = [[start]]
    visited = set()

    while(stack):
        path = stack.pop(-1)
        node = path[-1]

        if node == finish:
            return path
        elif node not in visited:
            for branch in map.get(node, []):
                new_path = list(path)
                new_path.append(branch)
                stack.append(new_path)
                if branch == finish:
                    return new_path
            visited.add(node)

    return "Maaf jalur tidak ditemukan, coba ganti tujuan anda"



print (dfs(map_2, 'A', 'J'))