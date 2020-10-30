from calculation.summation import Summation
from calculation.subtraction import Subtraction
import random
import csv
from datetime import date
import os.path


class Game:
    @staticmethod
    def run_game():
        username = input("Здравей! Как се казваш?\n" "Моето име е: ")
        print(f"Добре да се забавляваме, {username}. Нека да започнем играта!")
        incorrect_count = 0

        answer_count = 0
        for answer_count in range(1, 21):
            calculation = Game.get_calculation_class()
            print(f"Въпрос номер {answer_count}:")
            (question, answer) = calculation.get_calculation()
            print(f"На колко е равно:\n {question}")
            user_answer = input("= ")
            while True:
                if user_answer != str(answer):
                    print(f"Отговорът ти не е правилен. Опитай пак! На колко е равно:\n {question} ?")
                    user_answer = input("= ")
                    incorrect_count += 1
                else:
                    print(f"Поздравления, твоят отговор {answer} е правилен.")
                    break
        print(f"Браво, {username} ти завърши математическата куиз!")
        if answer_count > incorrect_count:
            if incorrect_count == 0:
                print(
                    f"Отлична работа, всички отговори са правилни! Твоята награда е 20 минути бонус игра на телефона!")
            elif incorrect_count < 3:
                print(
                    f'Броят на неверните отговорие е: {incorrect_count} от общо {answer_count} решени задачи!'
                    f'Получаваш награда от 10 минути бонус игра на телефона!'
                )
            elif incorrect_count <= 4:
                print(
                    f"Броят на неверните отговорие е: {incorrect_count} от общо {answer_count} решени задачи!"
                    f" Твоята поущтрителна наградата е 5 минути бонус игра на телефона!"
                )
            else:
                print(
                    f"Имаш {incorrect_count} грешни отговора от общо {answer_count} решени задачи! Трябва да решаваш повече задачи, за да получиш награда!")
        else:
            print(
                f"От {answer_count} задачи ти имаш {incorrect_count} грешни отговора."
                f" Трябва да решаваш повече задачи, за да получиш награда!")
        Game.save_stats(username, answer_count, incorrect_count)

    @staticmethod
    def get_calculation_class():
        number = random.randint(1, 6)
        if number % 2 == 0:
            return Summation(1, 50)
        else:
            return Subtraction(1, 100)

    @staticmethod
    def save_stats(username: str, correct_count: int, incorrect_count: int):
        today = date.today()
        content = [today, username, correct_count, incorrect_count]
        file_exists = os.path.isfile('statistics.csv')
        with open('statistics.csv', 'a', newline='\n') as csvfile:
            headers = ["Day", "Username", "Correct count", "Incorrect count"]
            writer = csv.writer(csvfile)
            if not file_exists:
                writer.writerow(headers)
            writer.writerow(content)


if __name__ == "__main__":
    Game.run_game()

