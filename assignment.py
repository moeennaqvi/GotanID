def find_ultimate_parent(child, parents, visited=None):
    """
        Recursive function that finds the ultimate parent of a child node.

        Args:
            child (str): The ID of the child node.
            parents (dict): A dictionary containing the parent-child relationships.

        Returns:
            str: The ID of the ultimate parent of the child node.
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

# Read data from the local unzipped file
filename = "data_parent.txt"
with open(filename, "r") as f:
    data = f.read()


# Process the data and generate output
rows = data.strip().split("\n")
print("Number of lines", len(rows))
immediate_parents = {}
for row in rows:
    cols = row.strip().split("\t") # splitting the columns based on tab
    child, immediate_parent = cols[0], cols[1] if len(cols) > 1 else None
    immediate_parents[child] = immediate_parent


ultimate_parents = []
for child in immediate_parents:
    ultimate_parent = find_ultimate_parent(child, immediate_parents)
    if ultimate_parent:
        ultimate_parents.append((child,ultimate_parent))
print("Number of parents", len(ultimate_parents))
# print the final child and ultimate pairs
#for pair in ultimate_parents:
    #print(pair[0],pair[1])
