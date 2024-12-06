import random
import termcolor

def ask_question(i, question, answers):
    print(f'Question {i}: {question}?')
    for j, answer in enumerate(answers):
        print(f'{chr(j+65)}. {answer}')
    return input('Your answer: ').upper().strip()

def judge_answer(count, answer, correct_answer):
    if answer == correct_answer:
        t, c = 'Correct\n', 'green'
        count += 1
    else: 
        t, c = f'Wrong! The correct answer is {correct_answer}\n', 'red'
    termcolor.cprint(t, color=c)
    return count

def run_quiz(questions):
    random.shuffle(questions)
    count = 0
    for i, q in enumerate(questions, start=1):
        answer = ask_question(i, q[0], q[2:])
        count = judge_answer(count, answer, q[1])
    print(f'Quiz over! Your final score is {count} out of {len(questions)}\n')

def main():
    questions = [
        ('What is the capital of France',           'C',
            'Berlin',  'Madrid',   'Paris', 'Rome'   ),
        ('Which planet is known as the red planet', 'B',
            'Earth',     'Mars', 'Jupiter', 'Saturn' ),
        ('What is the largest ocean on Earth',      'D')]
    run_quiz(questions)

if __name__ == '__main__':
    main()
