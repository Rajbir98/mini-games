# Snake Water Gun

![image](https://user-images.githubusercontent.com/84771149/214829059-355682e3-2f24-4e64-b75c-41e7f4ed1a59.png)

A simple command-line program which uses mathematics to play the classic game of Snake Water Gun with you.

## Main Idea

In the game of Snake Water Gun, we have the following rules:
- If Snake V/S Water [Snake Wins]
- If Water V/S Gun   [Water Wins]
- If Snake V/S Gun   [Gun   Wins]

To make it easier to code, we will associate each possibility with a number:
- 1: Snake
- 2: Water
- 3: Gun

By combining these numbers and the rules of the game, we can create a pattern for determining the winner:
- If both numbers are the same, no one wins
- If both numbers are consecutive, the smaller one wins
- If both numbers aren't consecutive, the bigger one wins.

Thanks for reading and enjoy playing the game!
