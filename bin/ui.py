import os

class Ui:
    def init(self):
        return
    def welcome(self):
        print("Welcome to Words-Helper!\n")
        print("\n\n")
    def clear(self):
        os.system("cls")
    def select(self, names):
        l = len(names)
        for i in range(0, l):
            name = names[i]
            print("[{}] {}".format(i, name))
        while True:
            selection = int(input("Enter the number: "))
            if 0 <= selection and selection < l:
                return selection
            else:
                print("Invalid input!")
    def get_answer(self, meaning):
        print(meaning)
        print('\n')
        result = input()
        return result
    def finish(self):
        print("Done!")
        print("Check your results in .\\results.")

