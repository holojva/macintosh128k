from super_api import SuperHeroAPI, API_KEY
import tkinter
root = tkinter.Tk()
class SuperHeroApp() :
    def __init__(self)            :
           self._s = SuperHeroAPI(API=API_KEY)
           self._status = True
           self._prelude_text = "Потом напишу help, compare -name -name, exit "
    def _change_status(self) :
        self._status = False
    def tkinter_manager(self) :
        self._input = tkinter.StringVar()
        self.command_text = tkinter.Label(root, text = 'Enter command')
        self.entry = tkinter.Entry(root, textvariable = self._input)
        self.command_text.pack()
        self.entry.pack()
        print("one")

        self.button = tkinter.Button(root, text="Submit", command=self.run)
        self.button.pack()
        print("two")
    def run(self) :
        print(self._prelude_text)  
        while self._status :
            # _input = input("Введение команду ")
            command = self._parse_command(self._input.get())
            self.command_dispatcher(command)
    def _parse_command(self, _input) :
        return [i.strip() for i in _input.strip().lower().split('-')]
        
    def command_dispatcher(self, command) :
        if len(command) <= 1:
            if not command or command[0] == "exit":
                self._change_status()
            elif command[0]=="help" :
                self.output = tkinter.Label(text=self._prelude_text).pack()
                root.mainloop()
        else :
            action, *arguments = command
            print(action, *arguments)
            if action == "compare":
                self._compare_heroes(arguments)

    def _compare_heroes(self, heroes) :
        hero_one = self._s.get_hero_stats(heroes[0])
        hero_two = self._s.get_hero_stats(heroes[1])
        power_one, hp_one = int(hero_one["power"]), int(hero_one["durability"])
        power_two, hp_two = int(hero_two["power"]), int(hero_two["durability"])
        # print(power_one, power_two, hp_one, hp_two)
        # print(hp_two - power_one, hp_one - power_two)
        if hp_two - power_one > 0 and hp_two - power_one > hp_one - power_two:
            
            self.output = tkinter.Label(text=f"{heroes[1].title()} победил! Осталось здоровья: {hp_two - power_one}").pack()
        elif hp_one - power_two > 0 and hp_one - power_two > hp_two - power_one :
            self.output = tkinter.Label(text=f"{heroes[0].title()} победил! Осталось здоровья: {hp_one - power_two}").pack()
        else :
            self.output = tkinter.Label("Ничья!").pack()
        root.mainloop()
if __name__ == "__main__" :
    app = SuperHeroApp()
    app.tkinter_manager()
    root.mainloop()