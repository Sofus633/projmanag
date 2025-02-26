import random
lorem_words = [
    "lorem", "ipsum", "dolor", "sit", "amet", "consectetur", "adipiscing", "elit",
    "sed", "do", "eiusmod", "tempor", "incididunt", "ut", "labore", "et", "dolore",
    "magna", "aliqua", "enim", "ad", "minim", "veniam", "quis", "nostrud",
    "exercitation", "ullamco", "laboris", "nisi", "aliquip", "ex", "ea", "commodo",
    "consequat", "duis", "aute", "irure", "dolor", "in", "reprehenderit",
    "voluptate", "velit", "esse", "cillum", "eu", "fugiat", "nulla", "pariatur",
    "excepteur", "sint", "occaecat", "cupidatat", "non", "proident", "sunt", "culpa",
    "qui", "officia", "deserunt", "mollit", "anim", "id", "est", "laborum",
    "curabitur", "pretium", "tincidunt", "lacus", "nulla", "gravida", "orci", "odio",
    "nullam", "varius", "turpis", "et", "commodo", "phasellus", "fermentum", "in",
    "dolor", "pellentesque", "facilisis", "imperdiet", "magnam", "vestibulum",
    "integer", "quam", "morbi", "mi", "eros", "convallis", "at", "nunc", "aenean",
    "eget", "metus", "ornare", "lectus", "finibus", "pulvinar", "sagittis",
    "dapibus", "suscipit", "tortor", "aliquam", "feugiat", "hendrerit", "euismod",
    "tristique", "venenatis", "luctus", "tempus", "sollicitudin", "felis", "libero",
    "sapien", "fermentum", "faucibus", "ornare", "integer", "risus", "placerat",
    "quisque", "vulputate", "bibendum", "vehicula", "posuere", "pharetra", "turpis",
    "fusce", "auctor", "viverra", "consequat", "curabitur", "lacinia", "tincidunt",
    "ultricies", "cras", "mattis", "vehicula", "ultrices", "suspendisse", "potenti"
]
def gen_lorem(lenn):
    return " ".join([lorem_words[random.randint(0, len(lorem_words)-1)] for i in range(lenn)])

if __name__ == '__main__':
    print(gen_lorem(500))