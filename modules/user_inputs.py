from modules import *

class user_inputs:
    tool = Converter()
    result = [None,None]

    def menu(self):
        print("Change Conversion (+)  |  End Program (-)")
        print("==========================================")
        self.view_settings()
        inp = str(input(">> "))
        print()
        if inp == '+' : self.change_settings()
        elif inp == '-' : return False
        else : self.make_conversion(inp)

    def make_conversion(self, inp):
        self.result = self.tool.convert(inp)

    def view_settings(self):
        for key, value in self.tool.settings.items():
            if value == 1: source = key
            elif value == 2: target = key
        print(f"Current Settings = {source} --> {target}")
        
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
