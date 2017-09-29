#! -*- coding=utf-8 -*-

import re

class DartScore:
    '''This class defines Score
    '''
    def __init__(self):
        self.score = 0
        self.bonus = None
        self.option = None
    def print_score(self):
        #print(self.score, self.score.__class__)
        #print(self.bonus, self.bonus.__class__)
        #print(self.option, self.option.__class__)
        print(self)

    def __str__(self):
        return "<DartScore: score = %d, bonus = %s, option = %s>" % (self.score, self.bonus, self.option)

class DartScoreCalculator:
    '''This class is for calculating score of dart game
    '''
    def __init__(self):
        self.score_list = []
        self.score_total = 0

    def add_score(self, score_tuple):
        '''score_tuple must be in the form of ( int_score, str_bonus, str_opt )
        '''
        pass

class DartScoreReader:
    '''This class is for reading score from the user
    '''
    def __init__(self):
        pass

    def read_score(self):
        str_score = raw_input("Enter score card: ")
        tpl_score = self.parse_score(str_score)
        # 아래와 같이 할 방법은 없을까?
        #for s, b, o in tpl_score:
        #    print("Score : ", s)
        #    print("Bonus : ", b)
        #    print("Option : ", o)
        for i in range(3):
            s = tpl_score[3*i+0]
            b = tpl_score[3*i+1]
            o = tpl_score[3*i+2]
            #print("Score : %d" % int(s))
            #print("Bonus : %s" % b)
            #print("Option : %s" % o)
            score = DartScore()
            score.score = self._check_score(s)
            score.bonus = b
            score.option = o if o else None
            score.print_score()
        
    def parse_score(self, str_score):
        pattern = r'([0-9]*)(S|D|T)(\*|#?)([0-9]*)(S|D|T)(\*|#?)([0-9]*)(S|D|T)(\*|#?)'
        parsed = re.search(re.compile(pattern), str_score)
        if not parsed: raise BaseException("Score Card is invalid(%s)" % str_score)
        return parsed.groups()

    def _check_score(self, str_score):
        if not str_score.isdigit(): raise BaseException("Score(%s) is not number" % str_score)
        if not 0 <= int(str_score) <= 10: raise BaseException("Score(%s) is not in range 0-10" % str_score)
        return int(str_score)
