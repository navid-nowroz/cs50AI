class Node():
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action


class StackFrontier():
    def __init__(self):
        self.frontiers = []

    def add(self, node):
        self.frontiers.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontiers)

    def empty(self):
        return len(self.frontiers) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontiers[-1]
            self.frontiers = self.frontiers[:-1]
            return node


class QueueFrontier(StackFrontier):

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontiers[0]
            self.frontiers = self.frontiers[1:]
            return node
