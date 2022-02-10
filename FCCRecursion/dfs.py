"""
From https://www.youtube.com/watch?v=IJDJ0kBx2LM at ~1h41mins in
"""


from operator import is_


def dfs(node, target, visited = None):
    """
    This is a dfs for a graph
    """
    if visited is None:
        visited = set()

    # base case
    if node is None:
        return False
    if node.val == target:
        return True

    # recursive case - explore all nodes in dfs manner
    for node_neighbour in node.get_neighbours():
        if node_neighbour in visited:
            continue
        visited.add(node_neighbour)
        is_found = dfs(node_neighbour, target, visited)

        if is_found:
            return True

    # if all nodes visited and target not found (i.e. True not returned early)
    # then return False
    return False
