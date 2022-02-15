# Inspired by blog:
# https://towardsdatascience.com/implementing-a-trie-data-structure-in-python-in-less-than-100-lines-of-code-a877ea23c1a1

class TrieNode:

    def __init__(self, ch):
        self.ch = ch
        self.children = []
        self.word_finished = False
        self.counter = 1


def add(root, word):

    node = root
    for c in word:
        ch_found = False
        for child in node.children:
            if child.ch == c:
                child.counter += 1
                node = child
                ch_found = True
                break

        if not ch_found:
            child = TrieNode(c)
            node.children.append(child)
            node = child

    node.word_finished = True


def find_prefix(root, prefix):

    node = root

    for ch in prefix:
        ch_found = False

        for child in node.children:
            if child.ch == ch:
                ch_found = True
                break

        if not ch_found:
            return False, 0

        node = child

    return True, node.counter


def word_exists(root, word):

    node = root

    for c in word:
        ch_found = False

        for child in node.children:
            if child.ch == c:
                ch_found = True
                node = child
                break

        if not ch_found:
            return False

    return child.word_finished


if __name__ == '__main__':
    root = TrieNode('*')
    add(root, "hackathon")
    add(root, 'hack')

    print(find_prefix(root, 'hac'))
    print(find_prefix(root, 'hack'))
    print(find_prefix(root, 'hackathon'))
    print(find_prefix(root, 'ha'))
    print(find_prefix(root, 'hammer'))
    print(word_exists(root, 'hammer'))
    print(word_exists(root, 'hackathon'))
    print(word_exists(root, 'hack'))
