import termcolor


questions = (
    ('What is the capital of France',           'C',   'Berlin', 'Madrid',   'Paris', 'Rome'   ),
    ('Which planet is known as the red planet', 'B',    'Earth',   'Mars', 'Jupiter', 'Saturn' ),
    ('What is the largest ocean on Earth',      'D', 'Atlantic', 'Indian',  'Arctic', 'Pacific')
    )
count = 0
for i, q in enumerate(questions):
    print(f'Question {i + 1}: {q[0]}?')
    for j, qq in enumerate(q[2:]):
        print(f'{chr(j+65)}. {qq}')

    if input('Your answer: ').upper() == q[1]:
        t, c = 'Correct', 'green'
        count += 1
    else: 
        t, c = f'Wrong! The correct answer is {q[1]}', 'red'
    termcolor.cprint(t, color=c)
    print()

print(f'Quiz over! Your final score is {count} out of {len(questions)}')
