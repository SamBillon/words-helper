from asyncore import write
import xlrd
import xlwt

class Problem:
    path = ""
    def init(self, path):
        self.path = path
        self.table = xlrd.open_workbook(path).sheets()[0]
        return
    def get_colnum(self, colnum):
        return self.table.col_values(colnum, start_rowx=0, end_rowx=None)
    def get_words(self):
        return self.get_colnum(0)
    def get_meanings(self):
        return self.get_colnum(1)


class Result:
    path = ""
    workBook = xlwt.Workbook("UTF-8")
    sheet = workBook.add_sheet("sheet1")
    def init(self, path):
        self.path = path
        self.sheet.write(0, 0, "含义")
        self.sheet.write(0, 1, "单词")
        self.sheet.write(0, 2, "你的拼写")
        self.sheet.write(0, 3, "是否正确")
        self.sheet.write(0, 5, "总计")
        self.sheet.write(1, 5, "正确个数")
        self.sheet.write(2, 5, "正确率")
        self.sheet.write(2, 6, xlwt.Formula("G2/G1"))
        return
    def save(self):
        self.workBook.save(self.path)
    def write_number(self, right, total):
        self.sheet.write(0, 6, total)
        self.sheet.write(1, 6, right)
    def write_colnum(self, list, colnum):
        l = len(list)
        for i in range(0, l):
            self.sheet.write(i + 1, colnum, list[i])
    def write_meanings(self, meanings):
        self.write_colnum(meanings, 0)
    def write_words(self, words):
        self.write_colnum(words, 1)
    def write_yourspells(self, yourspells):
        self.write_colnum(yourspells, 2)
    def write_iscorrect(self, iscorrect):
        self.write_colnum(iscorrect, 3)

if __name__ == '__main__':
    test = Result()
    test.init(".\\results\\test.xls")
    test.write_number(8, 10)
    L = ["appeal", "pending", "judging", "shiyuhe txdy"]
    R = ["你的名字", "想不出来", "这个单词是什么呢"]
    test.write_meanings(R)
    test.write_words(L)
    test.save()