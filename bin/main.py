from datetime import datetime
import random


from bin.path import Path_finder
from bin.ui import Ui
from bin.xls import Problem, Result

class Entry:
    def run(self):
        path_finder = Path_finder()
        ui = Ui()
        problems = Problem()
        result = Result()

        ui.init()
        path_finder.init()

        ui.welcome()
        file_names, file_paths = path_finder.get_list()
        selection = ui.select(file_names)
        ui.clear()

        file_path = file_paths[selection]
        problems.init(file_path)

        words = problems.get_words()
        meanings = problems.get_meanings()
        temp = list(zip(words, meanings))
        random.shuffle(temp)
        words[:], meanings[:] = zip(*temp)

        num = len(words)
        yourspells = []
        correct = 0
        TF_state = []                       # state of True or False
        for i in range(0, num):
            meaning = meanings[i]
            word = words[i]
            answer = ui.get_answer(meaning)
            yourspells.append(answer)
            if answer == word:
                correct += 1
                TF_state.append('T')
            else:
                TF_state.append('F')
            ui.clear()

        strnow = datetime.strftime(datetime.now(),'%Y_%m_%d_%H_%M_%S')

        result_path = ".\\results\\result_" + strnow + ".xls"
        result.init(result_path)
        result.write_meanings(meanings)
        result.write_words(words)
        result.write_yourspells(yourspells)
        result.write_iscorrect(TF_state)
        result.write_number(correct, num)
        result.save()

        ui.clear()
        ui.finish()


if __name__ == '__main__':
    runner = Entry()
    runner.run()