from typing import Dict, List


def find_ultimate_parent(child: str, parents: Dict[str, str], visited: set = None) -> str:
    """
    Given a child ID and a dictionary mapping IDs to their immediate parents, find the ultimate parent ID.

    If the child has no parent or the parent is not in the dictionary, it is considered the ultimate parent.

    :param child: The ID of the child node.
    :param parents: A dictionary mapping IDs to their immediate parents.
    :param visited: A set containing the nodes already visited in recursion.
    :return: The ID of the ultimate parent node.
    """
    if visited is None:
        visited = set()
    if child in visited:
        # Cycle detected, return None
        return None
    visited.add(child)
    if child not in parents:
        return None
    parent = parents[child]
    if parent is None:
        if len(visited)==1:
            # the node has no parent
            return None
        return child
    return find_ultimate_parent(parent, parents,visited)


def find_child_parent_pairs(ids: List[str], parents: Dict[str, str]) -> List[List[str]]:
    """
    Given a list of IDs and a dictionary mapping IDs to their immediate parents, return a list of child-ultimate parent
    pairs. The pairs consist of the ID of the child and the ID of its ultimate parent.

    :param ids: The list of IDs.
    :param parents: A dictionary mapping IDs to their immediate parents.
    :return: A list of child-ultimate parent pairs.
    """
    pairs = []
    for child in ids:
        ultimate_parent = find_ultimate_parent(child, parents)
        if ultimate_parent:
            pairs.append((child, ultimate_parent))
    return pairs


if __name__ == '__main__':
    with open('data_parent.txt', 'r') as f:
        lines = f.readlines()

    # Create a dictionary mapping IDs to their immediate parents
    immediate_parents = {}
    for line in lines:
        cols = line.strip().split("\t")
        child = cols[0]
        parent = cols[1] if len(cols) > 1 else None
        immediate_parents[child] = parent

    # Find child-ultimate parent pairs
    ids = list(immediate_parents.keys())
    print("Number of ids",len(ids))
    ids.extend(set(immediate_parents.values()) - set(ids))
    pairs = find_child_parent_pairs(ids, immediate_parents)
    print("The length of ultimate parent's pairs",len(pairs))

    # Print results
    print("Child\tParent")
    for pair in pairs:
        print(str(pair[0]) + '\t' + str(pair[1]))