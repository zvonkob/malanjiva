import random
import termcolor


def set_question(i, question, answers):
    print(f'Question {i}: {question}?')
    for j, qq in enumerate(answers):
        print(f'{chr(j+65)}. {qq}')

def judge_answer(count, answer, correct_answer):
    if answer == correct_answer:
        t, c = 'Correct', 'green'
        count += 1
    else: 
        t, c = f'Wrong! The correct answer is {correct_answer}', 'red'
    termcolor.cprint(t, color=c)
    print()
    return count

def main():
    questions = [
        ('What is the capital of France',           'C',
            'Berlin',  'Madrid',   'Paris', 'Rome'   ),
        ('Which planet is known as the red planet', 'B',
            'Earth',     'Mars', 'Jupiter', 'Saturn' ),
        ('What is the largest ocean on Earth',      'D',
            'Atlantic', 'Indian', 'Arctic', 'Pacific')
        ]
    random.shuffle(questions)
    for q in questions:
        print(q[0])
    count = 0
    for i, q in enumerate(questions, start=1):
        set_question(i, q[0], q[2:])

        answer = input('Your answer: ').upper().strip()
        
        count = judge_answer(count, answer, q[1])

    print(f'Quiz over! Your final score is {count} out of {len(questions)}\n')

if __name__ == '__main__':
    main()
