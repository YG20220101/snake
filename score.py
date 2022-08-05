class Score(object):
    def __init__(self):
        self.score_list = []

    def write_out(self):
        with open("score.txt", "r") as f:
            for line in f.readlines():
                self.score_list.append(int(line.strip('\n')))
        f.close()

    def get_score(self):
        return self.score_list

    def append_score(self, s):
        self.score_list.append(int(s))
        self.score_list.sort(reverse=True)
        if len(self.score_list) > 10:
            self.score_list = self.score_list[:10]

    def write_in(self):
        with open("score.txt", "w") as f:
            length = len(self.score_list)
            for i in range(length):
                f.write(str(self.score_list[i])+'\n')
        f.close()

