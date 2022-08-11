# Pyramid draxing with Asterisks

Hi there!

I attempted to create a simple custom size drawing program using Asterisks with the use of a definition for the first time. the user is allowed to add a random number to create a certain size.

The idea of a definition is created because I added a Try-Except statement within it, which would allow the user to help entering a correct value. 
A ValueError exception is thrown to warn the user that only a whole nomber can be accepted.
This obligation has been created by translating my user input into an integer value.

The program runs well when a whole number had been added for the first time. However, if a ValueError is shown, the try-except statement runs correctly, but after entering a correct whole number, the system dousn't seem to pick up that size variable. He annnounces me that tha value is "None". It doesn't seem to want to take over the size-variable after a second input and I can't seem to find out why.

If somebody could help me out, or give additional suggestions, I would be glad to hear them!

# What I learned

- Make use of definitions to keep code clean
- integrate a Try-Except statemtn which attempts to get a correct user-input
