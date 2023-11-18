# Cricket Score Analyzer

Explore this interactive Python script that lets you input and analyze cricket scores, revealing the player with the highest score.

## How to Use

1. **Enter Cricketer Count:** Begin by specifying the number of cricketers you want to analyze.
2. **Add Names:** Create an empty list 'a' to hold cricketer names.
3. **Record Scores:** Make use of an empty list to store their scores.
4. **Gather Data:** Go through a loop for each cricketer:
   - Provide their name and their corresponding score.
   - Watch as their details are added to the lists.


 Specify the number of cricketers
n = int(input("Enter number of elements: "))

 List to store cricketer names
a = []

 List to store scores
s = []

 Gather input
for i in range(n):
    x = str(input("ENTER NAME:"))
    h = int(input("ENTER SCORES"))
    a.append(x)
    s.append(h)


Discover the Star: Set the stage by initializing a variable 'm' with the first score, then loop through the scores to spot the highest.

m = s[0]

# Compare and find the highest
for z in range(n):
    if s[z] > m:
        m = s[z]
        pos = z

Champion's Reveal: Finally, the curtain rises, and you get to see the cricketer with the highest score.

print("Name Of The Batsman With The Highest Score:", a[pos], ", SCORE:", s[pos])

###### Ready to Play? ######
Prerequisites: Ensure you have Python installed on your system.

Unfold the Script: Copy the provided code into a .py file.

Start the Action: Run the file using a Python interpreter.

Input Your Data: Follow along with the prompts to add cricketer names and their scores.

Celebrate the Winner: The script will reveal the cricketer who clinched the highest score.



#Python #CodingAdventures #CricketFever #ProgrammingBeginner #ExploreTech


This README is your friendly guide to the cricket score analyzer script. With clear steps, relatable explanations, and approachable language, it makes diving into coding as enjoyable as a game of cricket. Feel free to engage and join the coding adventure!
