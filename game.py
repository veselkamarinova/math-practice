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
        correct_count = 0
        total_answer = 0
        for i in range(1, 11):
            total_answer += i
            calculation = Game.get_calculation_class()
            print(f"Въпрос номер {i}:")
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
                    correct_count += 1
                    break

        print(f"Браво, {username} ти завърши математическата куиз!")
        if correct_count > incorrect_count:
            if incorrect_count == 0:
                print(
                    f"Отлична работа, всички отговори са правилни! Твоята награда е 30 минути бонус игра на телефона!")
            elif incorrect_count < 3:
                print(
                    f'Броят на неверните отговорие е: {incorrect_count} от общо {total_answer} решени задачи!'
                    f'Получаваш награда от 20 минути бонус игра на телефона!'
                )
            elif incorrect_count <= 4:
                print(
                    f"Броят на неверните отговорие е: {incorrect_count} от общо {total_answer} решени задачи!"
                    f" Твоята поущтрителна наградата е 15 минути бонус игра на телефона!"
                )
            else:
                print(
                    f"Имаш {incorrect_count} грешни отговора от общо {total_answer} решени задачи! Трябва да решаваш повече задачи, за да получиш награда!")
        else:
            print(
                f"От {total_answer} задачи ти имаш {incorrect_count} грешни отговора."
                f" Трябва да решаваш повече задачи, за да получиш награда!")
        Game.save_stats(username, correct_count, incorrect_count)

    @staticmethod
    def get_calculation_class():
        number = random.randint(1, 6)
        if number % 2 == 0:
            return Summation(1, 10)
        else:
            return Subtraction(1, 20)

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

