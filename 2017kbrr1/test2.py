#! -*- coding=utf-8 -*-

from mod_kbrr1.game import *

reader = DartScoreReader()

while True:
    scores = reader.read_score()
    calc = DartScoreCalculator()
    calc.add_scores(scores)
    print(calc.score_total)
