# CTD-1D
Team 07 - 3 Hard and Irresistable Games

Members: Alexander Lee, Nathan Ly, Nathaniel Neo,  Roshan S/O Manogaran,  Vamshi Krishna, and Wong Guo Yao

## Description

Scenario: This game is aimed with the ojective of raising awareness on different mental illnesses through the trial of gaming. This is to help raise awareness for people and to give an insight on how certain mental illnesses can affect an individual. This software will be providing 3 different mini-games.

## Description game








## Description of mini-game 2

Mini-game 2 runs through a set of words that requires the player to memorise within a time limit, afterwards the words will appear and the user will have to type them in order. This is to help replicate the short term memory of a patient with Alzhimer which is directly linked to dementia. Each time the player gets the answer correct, it will go down a list of harder words based of the initial difficulty they have chosen. 

--------------------------
### Documentation of the game 
`import random` - This library helps to select a random element from a sequence. <br/> 
`import time` - This library allows the programmer to handle time-related operations. <br/>
`from TermControl import TermControl` - This library helps to implement basic operations for analysis and design of a feedback control systems <br/>
`from copy import deepcopy` - This helps to import the data from the library of copy and specifically the function deepcopy into 

`tc = TermControl` - 
 
![Difficulty Library](./img/minigame_2-dicts.png) - The dictionary is pulled to get the words for the user to memorise, it is also pulled to randomise to give it in random order for the user to know how to spell the words 

`def randomiser (difficulty, numWins)` - This function is called to randomise the list in the dictionary, firstly it will take the current list that is being used, create a deepcopy of it to ensure that the dictionary is not modified, randomise the contents in the listt. Then it returns the randomised list. 


`def countdown(t) -> None:`



## Decription of mini-game 3 

--------------------------
