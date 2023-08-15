class CategoryManager:

    def __init__(self, path):
        self.listed_categories = set()
        self.manage_txt(path)

    def manage_txt(self, path):
        with open(path) as file:
            for line in file:
                # print(repr(line))
                if line[0] == "-":
                    C = Categories(line[1:-1])
                    self.listed_categories.add(C)
                else:
                    C.sous_categories.add(Categories(line[5:-1]))


class Categories:
    def __init__(self, name):
        self.name = name
        self.sous_categories = set()

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)


if __name__ == "__main__":
    C = CategoryManager(
        "/Users/yp/Library/CloudStorage/OneDrive-Personnel/Programmation/Python/Projets/Data process/Bank Account Management/Data/Categories.txt")

    print(CategoryManager.__dict__)