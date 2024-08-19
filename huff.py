from heapq import heappop, heappush

class Node:
    def __init__(self, character, frequency):
        self.character = character
        self.frequency = frequency
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.frequency < other.frequency

def huffman_encoding(characters, frequencies):
    queue = []

    for character, frequency in zip(characters, frequencies):
        node = Node(character, frequency)
        heappush(queue, node)

    while len(queue) > 1:
        node1 = heappop(queue)
        node2 = heappop(queue)

        new_node = Node("", node1.frequency + node2.frequency)
        new_node.left = node1
        new_node.right = node2

        heappush(queue, new_node)

    root = heappop(queue)
    huffman_codes = {}

    def traverse(node, code):
        if node is None:
            return

        if node.character is not None:
            huffman_codes[node.character] = code

        traverse(node.left, code + "0")
        traverse(node.right, code + "1")

    traverse(root, "")
    return huffman_codes

# Example usage:
characters = ["A", "B", "C", "D", "E"]
frequencies = [0.35, 0.2, 0.2, 0.2, 0.1]

huffman_codes = huffman_encoding(characters, frequencies)
print(huffman_codes)
