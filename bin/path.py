import os

class Path_finder:
    resources = '.\\resources'
    def init(self):
        return
    def get_list(self):
        names = []
        paths = []
        for root, dirs, files in os.walk(self.resources):
            for file in files:
                if os.path.splitext(file)[1] == '.xls':
                    names.append(file)
                    paths.append(os.path.join(root, file))
        return names, paths

if __name__ == '__main__':
    test = Path_finder()
    print(test.get_list())