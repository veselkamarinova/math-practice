from calculation.summation import Summation
from calculation.calculation_class import Calculation


class Game:
    @staticmethod
    def run_game():
        summation = Summation(1, 10)

        username = input("Здравей! Как се казваш?\n" "Моето име е: ")
        print(f"Добре да се забавляваме, {username}. Нека да започнем с действие събиране!")
        sum_not_correct_answer = 0
        sum_correct_answer = 0

        for i in range(1, 11):
            print(f"Въпрос номер {i}:")
            (question, answer) = summation.get_calculation()
            print(f"На колко е равно:\n {question}")
            user_answer = input("= ")
            while True:
                if user_answer == str(answer):
                    print(f"Поздравления, твоят отговор {answer} е правилен.")
                    sum_correct_answer += 1
                    break
                elif user_answer != str(answer):
                    print(f"Отговорът ти не е правилен. Опитай пак! На колко е равно:\n {question} ?")
                    user_answer = input("= ")
                    sum_not_correct_answer += 1

        print(f"Браво, {username} ти завърши математическата игра!")
        if sum_correct_answer > sum_not_correct_answer:
            if sum_not_correct_answer == 0:
                print(
                    f"Отлична работа, всички отговори са правилни! Твоята награда е 30 минути бонус игра на телефона!")
            elif sum_not_correct_answer < 3:
                print(
                    f'Броят на неверните отговорие е: {sum_not_correct_answer}! '
                    f'Получаваш награда от 20 минути бонус игра на телефона!'
                )
            elif 3 == sum_not_correct_answer < 5:
                print(
                    f"Броят на неверните отговорие е: {sum_not_correct_answer}!"
                    f" Твоята поущтрителна наградата е 15 минути бонус игра на телефона!"
                )
            else:
                print(f" Трябва да решаваш повече задачи, за да получиш награда!")
        else:
            print(
                f"От 10 задачи ти имаш {sum_not_correct_answer} грешни отговора."
                f" Трябва да решаваш повече задачи, за да получиш награда!")


if __name__ == "__main__":
    Game.run_game()
