#%% BFS
from collections import deque
from maze import maze
from index import Node, MazeProblem


def breath_first_search(problem):
    node = Node(problem.init)
    if problem.goal_test(node.position):
        # Return solution
        return node.solution()
    frontier, explored = deque([node]), []
    while frontier:
        node = frontier.popleft()
        if node.position not in explored:
            explored.append(node.position)

        for child in node.expand(problem):
            if child.position not in explored and child not in frontier:
                if problem.goal_test(child.position):
                    return child.solution(), explored
                frontier.append(child)
    return None


if __name__ == "__main__":
    init = (5, 0)
    goal = (8, 7)
    problem = MazeProblem(init, goal, maze)
    solution, explored = breath_first_search(problem)
    print("solution: ", solution)
    print("\n")
    print("explored: ", explored)
