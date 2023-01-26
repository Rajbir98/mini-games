Snake Water Gun
======================

![image](https://user-images.githubusercontent.com/84771149/214818680-c1a94d1e-8ed0-4157-a37c-98dc5f49d59d.png)

A simple command-line program which uses maths to play swg with you.

*Nostalgia Hit!*
 ______________________


**Main Idea...**

We know that in Snake, Water, Gun

We have, 

    if Snake V/S Water [Snake Wins]
    if Water V/S Gun   [Water Wins]
    if Snake V/S Gun   [Gun   Wins]
  
Let’s associate each possibility with a *number*:

  > 1: Snake
  > 2: Water
  > 3: Gun

If we combine those numbers and the rules of the game, we get:
  Here, '>' indicates towards the **winner**,

    1 > 2 *
    2 > 3 *
    3 > 1 **

So, we got a pattern here,

    If both numbers are the same, no one wins
    If both numbers are consecutive, the smaller one wins (*)
    If both numbers aren’t consecutive, the bigger one wins (**)

Thanks for reading...
