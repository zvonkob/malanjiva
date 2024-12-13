from datetime import datetime, timedelta


def main():
    videos = [34, 232, 435, 337, 213, 159, 124, 202, 217, 634, 252, 459,
              453, 212, 358, 250, 149, 216, 156, 324]
    tt = datetime.now()
    print(f'                 {tt.hour} {tt.minute} {tt.second}')
    t = timedelta()
    for v in videos:
        duration = timedelta(minutes=v//100, seconds=v % 100)
        t += duration
        tt += duration
        print(f'{duration} {t}  {tt.hour} {tt.minute} {tt.second}')


if __name__ == '__main__':
    main()
