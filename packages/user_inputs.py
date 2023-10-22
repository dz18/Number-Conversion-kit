from converters import Converter

class user_inputs:
    tool = Converter()
    result = [None,None]

    def get_input(self):
        inp = str(input(">> "))
        ans = self.tool.convert(inp)
        self.result[0] = inp
        self.result[1] = ans
        pass

    def change_settings(self):
        print("Converting from... \n  1. Decimal\n  2. Binary\n  3. Hexidecimal")
        try:
            inp1 = int(input("  >> "))
            inp1 = self.tool.options[inp1 - 1]
        except:
            print("ERROR")
            return
        print("To.. \n  1. Decimal\n  2. Binary\n  3. Hexidecimal")

        try:
            inp2 = int(input("  >> "))
            inp2 = self.tool.options[inp2 - 1]
        except:
            print("ERROR")
            return
        if(inp1 == inp2 or [inp1, inp2] == self.tool.get_settings()):
            print("Same selections made. No changes made.\n")
            return
        
        for i in self.tool.options:
            self.tool.settings[i] = 0

        self.tool.settings[inp1] = 1
        self.tool.settings[inp2] = 2
        print(f"New Settings: \n  {inp1} --> {inp2}\n")

test = user_inputs()
test.change_settings()
test.get_input()