from time import sleep

characters_in_line = 5

text = "hello from pushkar saini"
# text = input("Enter your text to display")
lenA = 2
for i in range((len(text)//lenA)+1):
    print(text[i:lenA-i],end = "")
    sleep(0.5)




