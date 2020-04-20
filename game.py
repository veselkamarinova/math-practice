from calculation.summation import Summation
from calculation.subtraction import Subtraction
import random


class Game:
    @staticmethod
    def run_game():
        username = input("Здравей! Как се казваш?\n" "Моето име е: ")
        print(f"Добре да се забавляваме, {username}. Нека да започнем играта!")
        incorrect_count = 0
        correct_count = 0

        for i in range(1, 11):
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

        print(f"Браво, {username} ти завърши математическата игра!")
        if correct_count > incorrect_count:
            if incorrect_count == 0:
                print(
                    f"Отлична работа, всички отговори са правилни! Твоята награда е 30 минути бонус игра на телефона!")
            elif incorrect_count < 3:
                print(
                    f'Броят на неверните отговорие е: {incorrect_count}! '
                    f'Получаваш награда от 20 минути бонус игра на телефона!'
                )
            elif 3 == incorrect_count < 5:
                print(
                    f"Броят на неверните отговорие е: {incorrect_count}!"
                    f" Твоята поущтрителна наградата е 15 минути бонус игра на телефона!"
                )
            else:
                print(
                    f"Имаш {incorrect_count} грешни отговора. Трябва да решаваш повече задачи, за да получиш награда!")
        else:
            print(
                f"От 10 задачи ти имаш {incorrect_count} грешни отговора."
                f" Трябва да решаваш повече задачи, за да получиш награда!")

    @staticmethod
    def get_calculation_class():
        number = random.randint(1, 6)
        if number % 2 == 0:
            return Summation(1, 10)
        else:
            return Subtraction(1, 20)


if __name__ == "__main__":
    Game.run_game()

