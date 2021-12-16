import math 

class simple_calc:
    def __init__(self):
        print("Hey user, you have selected simple calculator operation...")
        oper=['+','-','*','/','%','//','**']
        self.sim_oper="NA"
        while self.sim_oper not in oper:
            print("Please select proper operation you want to perform ")
            self.sim_oper=input(f"List of operations you can select and perform :{oper}") # * 
        print("Please enter the values you need to perform")
        self.one_value=int(input("Enter value 1 ")) # 10 
        self.two_value=int(input("Enter value 2 ")) # 10 
        
    def return_sum(self):
        print(f"Sum is {self.one_value+self.two_value}")
    def return_sub(self):
        print(f"Sub is {self.one_value-self.two_value}")
    def return_multiply(self):
        print(f"Multiplication value is {self.one_value*self.two_value}")
    def return_div(self):
        print(f"Division value is {self.one_value/self.two_value}")
    def return_modulas(self):
        print(f"Modulas value is {self.one_value%self.two_value}")
    def return_floorDivision(self):
        print(f"floor Division value is {self.one_value//self.two_value}")
    def return_powerOf(self):
        print(f"Power Of value is {self.one_value**self.two_value}")

class advance_calc(simple_calc):
    def __init__(self):
        print("Hey user, you have selected advance calculator operation...")
        simoper=['+','-','*','/','%','//','**']
        adv_oper=["factorial","squareroot","log_2","cosine","sine","ten","combination"]
        self.sim_oper="NA"
        while (self.sim_oper not in simoper) and (self.sim_oper not in adv_oper):
            print("Please select proper operation you want to perform ")
            self.sim_oper=input(f"List of operations you can select and perform :{simoper} or {adv_oper}")
        print("Please enter the value you need to compute ")
    
        if self.sim_oper in simoper:
            self.one_value=int(input("Enter 1st value: "))
            self.two_value=int(input("Enter 2nd value: "))
        else:
            self.one_value=int(input("enter input value"))
        
    def get_factorial(self): # User defined functions and NOT Built in 
        print(f"The factorial value is {math.factorial(self.one_value)}")
    def get_squareroot(self):
        print(f"The squareroot value is {math.sqrt(self.one_value)}")
    def get_log_2(self):
        print(f"The logarithmatic value is {math.log2(self.one_value)}")
    def get_cosine(self):
        print(f"The cosine value is {math.cos(self.one_value)}")
    def get_sine(self):
        print(f"The sine value is {math.sine(self.one_value)}")
    def get_tan(self):
        print(f"The tan value is {math.tan(self.one_value)}")
    def get_combination(self):
        print(f"The combination value is {math.comb(self.one_value)}")

if __name__=="__main__": # main method 
    enter_data=0
    while enter_data not in ["1","2"]:
        print('''Please enter type of calculation you want to use
              Select 1> For Simple calculator
              Select 2> For advance calculator
              ''')
        enter_data=input("Please enter your selection : ") # 1 
        if enter_data=="1":
            simple_obj=simple_calc()
            if simple_obj.sim_oper =="+":
                simple_obj.return_sum()
            elif simple_obj.sim_oper =="-":
                simple_obj.return_sub()
            elif simple_obj.sim_oper =="*":
                simple_obj.return_multiply()
            elif simple_obj.sim_oper =="/":
                simple_obj.return_div()
            elif simple_obj.sim_oper =="%":
                simple_obj.return_modulas()
            elif simple_obj.sim_oper =="//":
                simple_obj.return_floorDivision()
            elif simple_obj.sim_oper =="**":
                simple_obj.return_powerOf()
            else:
                print("Your operation is invalid")
        elif enter_data=="2":
            adv_obj=advance_calc()
            if adv_obj.sim_oper =="+":
                adv_obj.return_sum()
            elif adv_obj.sim_oper =="-":
                adv_obj.return_sub()
            elif adv_obj.sim_oper =="*":
                adv_obj.return_multiply()
            elif adv_obj.sim_oper =="/":
                adv_obj.return_div()
            elif adv_obj.sim_oper =="%":
                adv_obj.return_modulas()
            elif adv_obj.sim_oper =="//":
                adv_obj.return_floorDivision()
            elif adv_obj.sim_oper =="**":
                adv_obj.return_powerOf()
            elif adv_obj.sim_oper =="factorial":
                adv_obj.get_factorial()
            elif adv_obj.sim_oper =="squareroot":
                adv_obj.get_squareroot()
            elif adv_obj.sim_oper =="log_2":
                adv_obj.get_log_2()
            elif adv_obj.sim_oper =="cosine":
                adv_obj.get_cosine()
            elif adv_obj.sim_oper =="sine":
                adv_obj.get_sine()
            elif adv_obj.sim_oper =="tan":
                adv_obj.get_tan()
            elif adv_obj.sim_oper =="combination":
                adv_obj.get_combination()
            else:
                print("Your operation is invalid ")
        else:
            print("Please select the option from above")