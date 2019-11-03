import database_utils
import equation_solver
import arith
"""
Generate a list of initial questions for the game
-5 arith(easy)
-5 arith(med)
-5 arith(hard)
"""

def init_quests():
    for i in range(5):
        subject = 'arithmetic_basic'
        temp_quest = arith.make_arith_basic(3)[0]
        eqn = equation_solver.getRes(temp_quest)
        question_img = eqn['input_img']
        answer_img = eqn['answer_img']
        acceptable_answers = eqn['acceptable_answers']

        print("Created Basic Arithmetic Question ", i)
        input()

        database_utils.create_question(question_img, acceptable_answers, answer_img, subject)

        subject = 'arithmetic_intermediate'
        temp_quest = arith.make_arith_exp(5)[0]
        eqn = equation_solver.getRes(temp_quest)
        question_img = eqn['input_img']
        answer_img = eqn['answer_img']
        acceptable_answers = eqn['acceptable_answers']

        print("Created Intermediate Arithmetic Question ", i)
        input()

        database_utils.create_question(question_img, acceptable_answers, answer_img, subject)

        subject = 'arithmetic_expert'
        temp_quest = arith.make_arith()[0]
        eqn = equation_solver.getRes(temp_quest)
        question_img = eqn['input_img']
        answer_img = eqn['answer_img']
        acceptable_answers = eqn['acceptable_answers']

        database_utils.create_question(question_img, acceptable_answers, answer_img, subject)

        print("Created Advanced Arithmetic Question ", i)
        input()

init_quests()