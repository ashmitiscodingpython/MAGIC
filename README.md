# MAGIC

> This was one of my first projects.

## Test

Choose a fruit, answer some questions and the fruit in your mind is shown before you!

## Mechanism

### Pretty bad explanation

The way this works is, it first asks the user the questions, then the corresponding variables are updated. For example, if the first prompt was whether the fruit was in this group: Blueberry, Apple, Mango; then if the answer was yes, 
then the variables blueberry, apple, mango would be changed.

After that, all the variables are checked and then if any of the variables said that one of the fruits had enough prompts to be the chosen fruit, that would be the fruit that the computer believed to be the fruit that the user chose.

### Better Explanation

First, the project asks whether the fruit is in the list of **Apple, Pineapple, Mango**. If the answer was yes, the variables apple, pineapple and mango are increased by 1. 
Next, the project asks for **Mango, Apple, Blueberry**, and increases the variables mango, apple and blueberry by 1 **if** the answer was yes. 
It does the same process for the rest of the questions. All the questions are arranged in such a way that if one of the variables is fully activated, none other will be. 
So, whichever is fully activated, is the fruit chosen by the user.

# **That's it!**
