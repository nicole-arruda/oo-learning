from random import randint

from first_approach.get_me_home import GetMeHome
# from strategy_approach.get_me_home import GetMeHome


class HighlyAdvancedUI:
    weather = ["sun", "rain", "snow"]

    def start(self):
        while True:
            weather = self.weather[randint(0, 2)]
            print(f"Today's weather: {weather}")
            print()

            print("How do you want to get home?")
            print("  [bike]\n  [car]\n  [metro]\n  [foot]")
            print("  [quit] to stop")

            user_choice = input()
            if user_choice == "quit":
                break

            GetMeHome().run(user_choice, weather)
