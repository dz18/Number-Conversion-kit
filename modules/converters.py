
class Converter: 
    options = ["Decimal", "Binary", "Hexidecimal"]
    source = str()
    hexSet = ('0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F')

    BinToHexSet = {
               "0000" : '0'
              ,"0001" : '1'
              ,"0010" : '2'
              ,"0011" : '3'
              ,"0100" : '4'
              ,"0101" : '5'
              ,"0110" : '6'
              ,"0111" : '7'
              ,"1000" : '8'
              ,"1001" : '9'
              ,"1010" : 'A'
              ,"1011" : 'B'
              ,"1100" : 'C'
              ,"1101" : 'D'
              ,"1110" : 'E'
              ,"1111" : 'F'
              }
    
    HexToDecSet = {
               '0' : "0000"
              ,'1' : "0001"
              ,'2' : "0010"
              ,'3' : "0011"
              ,'4' : "0100"
              ,'5' : "0101"
              ,'6' : "0110" 
              ,'7' : "0111"
              ,'8' : "1000"
              ,'9' : "1001"
              ,'A' : "1010"
              ,'B' : "1011"
              ,'C' : "1100"
              ,'D' : "1101"
              ,'E' : "1110"
              ,'F' : "1111"
              }

    def convert(self, input):
        result = [None,None,None]
        valid = self.check_input_validity(input, self.source)

        if(not valid):
            print(f"ERROR: INVALID INPUT")
            return
        
        if self.source == "Decimal":
            result[0] = input
            result[1] = self.decimal_to_binary(input)
            result[2] = self.decimal_to_hexidecimal(input)
        elif self.source == "Binary" : 
            result[0] = self.binary_to_decimal(input)
            result[1] = input
            result[2] = self.binary_to_hexidecimal(input)
        elif self.source == "Hexidecimal" : 
            result[0] = self.hexidecimal_to_decimal(input)
            result[1] = self.hexidecimal_to_binary(input)
            result[2] = input

        return result
    
    def check_input_validity(self, input, source):
        if source == "Decimal":
            try:
                int(input)
                return True
            except:
                return False
        elif source == "Binary":
            for i,k in enumerate(input):
                test = input[i]
                if k == '0' or k == '1':
                    continue
                else:
                    return False
            return True
        elif source == "Hexidecimal":
            i = 0
            if len(input) <= 2 or input[0:2] == "0x":
                i = 2
            while(i < len(input)):
                if input[i].upper() not in self.hexSet:
                    return False
                i += 1
            return True
            
    def finish_byte(self, result):
        while(len(result) % 4 != 0):
            result = "0" + result
        return result

    def format_bin(self, bin):
        i = 1
        result = str()

        while(i <= len(bin)):
            if i % 4 == 0:
                result = result + bin[i - 4: i] + " "
            i += 1

        result = result[:len(result) - 1]
        return result
    
    def view_settings(self):
        print(f"Current Source: {self.source}\n")

    def set_source(self, new_source):
        self.source = new_source

    def decimal_to_binary(self, input):
        i ,prev = input, input
        result = ""

        if input == 0:
            return '0000'

        while(i != 0):
            i = i // 2
            if i + i == prev: 
                result = "0" + result
            else:
                result = "1" + result
            prev = i

        result = self.finish_byte(result)

        return result
    def decimal_to_hexidecimal(self, input):
        bin = self.decimal_to_binary(input)
        result = self.binary_to_hexidecimal(bin)
        return result
    def binary_to_decimal(self, input):
        p = len(input) - 1
        result = int()

        for i in input:
            if i == '1':
                result += pow(2,p)
            p -= 1

        return result            
    def binary_to_hexidecimal(self, input):
        input = self.finish_byte(input)
        result = "0x"
        i = 0
        while(i <= len(input)):
            if i % 4 == 0 and i != 0:
                result += self.BinToHexSet[input[i - 4: i]]
            i += 4
        return result
    def hexidecimal_to_decimal(self, input):
        bin = self.hexidecimal_to_binary(input)
        result = self.binary_to_decimal(bin)
        return result
    def hexidecimal_to_binary(self, input):
        result = str()

        i = 0
        if len(input) >= 2 and input[0:2] == "0x":
                i = 2
        while(i < len(input)):
            result += self.HexToDecSet[input[i].upper()]
            i += 1

        return result

test = Converter()
test.view_settings()
print("Make Selection: Decimal (1) | Binary (2) | Hexidecimal (3)")
inp = int(input(">> "))
inp = test.options[inp - 1]
print()
test.set_source(inp)
test.view_settings()
test.convert("1818")