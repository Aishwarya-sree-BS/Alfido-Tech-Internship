def temperature():
    print("\nTEMPERATURE CONVERSION")
    print("1.Celsius to Fahrenheit")
    print("2.Celsius to Kelvin")
    print("3.Fahrenheit to Celsius")
    print("4.Fahrenheit to Kelvin")
    print("5.Kelvin to Celsius")
    print("6.Kelvin to Fahrenheit")
    
    ch=input("Enter your choice(1/2/3/4/5/6):")

    temp=float(input("Enter temperature:"))  
    
    if ch=='1':
        fahrenheit=(temp*9/5)+32
        print(f"{temp}°C={fahrenheit}°F")
    elif ch=='2':
        kelvin=temp+273.15
        print(f"{temp}°C={kelvin}°K")
    elif ch=='3':
        celsius=(temp-32)*5/9
        print(f"{temp}°F={celsius}°C")
    elif ch=='4':
        kelvin=(temp-32)* 5/9 + 273.15
        print(f"{temp}°F={kelvin}°K")
    elif ch=='5':
        celsius=temp-273.15
        print(f"{temp}°K={celsius}°C")
    elif ch=='6':
        fahrenheit=(temp-273.15)* 9/5 +32
        print(f"{temp}°K={fahrenheit}°F")
    else:
        print("Error:Invalid choice")
def main():
    while True:
        temperature()
        continuee=input("Do you want to calculate again?(yes/no):")
        if continuee.lower()!='yes':
            break

if __name__=="__main__":
    main()
