from super_api import SuperHeroAPI, API_KEY
class SuperHeroApp() :
    def __init__(self)            :
           self._s = SuperHeroAPI(API=API_KEY)
           self._status = True
           self._prelude_text = "Потом напишу help, compare name name, exit "
    def _change_status(self) :
        self._status = False
    def run(self) :
        print(self._prelude_text)
        while self._status :
            _input = input("Введение команду ")
            command = self._parse_command(_input)
            self.command_dispatcher(command)
    def _parse_command(self, _input) :
        return _input.strip().lower().split()
    def command_dispatcher(self, command) :
        if len(command) <= 1:
            if not command or command[0] == "exit":
                self._change_status()
            elif command[0]=="help" :
                print(self._prelude_text)
        else :
            action, *arguments = command
            print(action, *arguments)
            if action == "compare" :
                num = 0
                for i in arguments :
                    if i == "vs" :
                        first_hero = arguments[:num]
                        second_hero = arguments[num+1:]
                    num += 1
                self._compare_heroes([" ".join(first_hero), " ".join(second_hero)])

    def _compare_heroes(self, heroes) :
        hero_one = self._s.get_hero_stats(heroes[0])
        hero_two = self._s.get_hero_stats(heroes[1])
        power_one, hp_one = int(hero_one["power"]), int(hero_one["durability"])
        power_two, hp_two = int(hero_two["power"]), int(hero_two["durability"])
        # print(power_one, power_two, hp_one, hp_two)
        # print(hp_two - power_one, hp_one - power_two)
        if hp_two - power_one > 0 and hp_two - power_one > hp_one - power_two:
            print(f"{' '.join(second_hero).title()} победил! Осталось здоровья: {hp_two - power_one}")
        elif hp_one - power_two > 0 and hp_one - power_two > hp_two - power_one :
            print(f"{' '.join(first_hero).title()} победил! Осталось здоровья: {hp_one - power_two}")
        else :
            print("Ничья!")
if __name__ == "__main__" :
    app = SuperHeroApp()
    app.run()
