# -*- coding: utf-8 -*- 
from question_classifier import *
from question_parser import *
from answer_search import *

import sys
reload(sys)
sys.setdefaultencoding('utf8')

# '''问答类'''
class ChatBotGraph:
    def __init__(self):
        self.classifier = QuestionClassifier()
        self.parser = QuestionPaser()
        self.searcher = AnswerSearcher()

    def chat_main(self, sent):
        answer = '没能理解您的问题，系统数据量有限。'
        res_classify = self.classifier.classify(sent)
        if not res_classify:
            return answer
        res_sql = self.parser.parser_main(res_classify)
        final_answers = self.searcher.search_main(res_sql)
        if not final_answers:
            return answer
        else:
            return '\n'.join(final_answers)

if __name__ == '__main__':
    handler = ChatBotGraph()
    while 1:
        question = input('用户咨询:')
        answer = handler.chat_main(question)
        print '客服回复:', answer

