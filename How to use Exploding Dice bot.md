#explodingDice
## Possible Commands
- [[How to use Exploding Dice bot#/roll|/roll]]
- [[How to use Exploding Dice bot#/shadowrun roll|/shadowrun roll]]
- [[How to use Exploding Dice bot#/shadowrun extended|/shadowrun extended]]
- [[How to use Exploding Dice bot#/shadowrun alchemylist|/shadowrun alchemylist]]
- [[How to use Exploding Dice bot#/shadowrun alchemyuse|/shadowrun alchemyuse]]
- [[How to use Exploding Dice bot#/shadowrun alchemyage|/shadowrun alchemyage]]
- [[How to use Exploding Dice bot#/shadowrun alchemycreate|/shadowrun alchemycreate]]
- [[How to use Exploding Dice bot#/shadowrun alchemydelete|/shadowrun alchemydelete]]
- [[How to use Exploding Dice bot#/shadowrun summonspirit|/shadowrun summonspirit]]
- [[How to use Exploding Dice bot#/shadowrun bindspirit|/shadowrun bindspirit]]
- [[How to use Exploding Dice bot#/shadowrun resistdamage|/shadowrun resistdamage]]
- [[How to use Exploding Dice bot#/initshadowrun|/initshadowrun]]

## /roll
```
/roll input:{}
```
This command can take any of the old Exploding Dice commands as an input. This means that if you want to do a vs roll here you would input the following 
```
/roll input:[12v10]
```
Any commands that are displayed from the help command currently can be done this way

## /shadowrun roll
```
/shadowrun roll command:{} annotation:{}
```
This command works similarly to the /roll command above. The difference is this can only do one roll at a time and does not need the "[]" around the command. So while you can give it the same commands as /roll, it can not do the extended tests and it will also not store any kind of memory. This is also how you bring up an interactive array for rolling more dice. 
An example of the same vs command as before is as follows
```
/shadowrun roll command:12v10 annotation:Versus dice roll
```
![[Images/attachments/Pasted image 20230421135730.png]]
## /shadowrun extended
```
/shadowrun extended dice:{} edge:{}
```
This command only does extended dice rolls, edge option only uses edge on the first roll. This will not add your edge to the next roll. Once you roll there will be three buttons
![[Images/attachments/Pasted image 20230421140050.png]]
These buttons do exactly as they say, the first toggles a post edge roll on the last roll. The edge Reroll will roll the next one as a preedge using the edge number you gave previously as the extra to it. The Roll Again will roll your next set of dice for the extended test. Below is what it will look like in your message box, the edge option is not required
![[Images/attachments/Pasted image 20230421135939.png]]
## /shadowrun alchemylist
```
/shadowrun alchemylist annotation:{}
```
This command lists all currently made preps that are stored in the Exploding Dice roller. There is an annotation option, but this is not necesary
## /shadowrun alchemyuse
wip
## /shadowrun alchemyage
wip
## /shadowrun alchemycreate
wip
## /shadowrun alchemydelete
wip
## /shadowrun summonspirit
wip
## /shadowrun bindspirit
wip
## /shadowrun resistdamage
wip
## /initshadowrun
wip