def main():
        num1=input("Enter first number: ")
        num2=input("Enter second number: ")
        op=time=input("Choose the operation(+, -, /, *): ")
        listOp=["+","-","/","*"]
        if (num1.isdigit and num2.isdigit()):
                if(op=="+"):
                        print("The answer is ", (int(num1)+int(num2)))
                elif(op=="-"):
                        print("The answer is ", (int(num1)-int(num2)))
                elif(op=="*"):
                        print("The answer is ", (int(num1)*int(num2)))
                elif(op=="/"):
                        print("The answer is ", (int(num1)/int(num2)))
                else:
                        print("the operation is not valid")
        else:
                print("the numbers are invalid")

if __name__ == '__main__':
	main()
