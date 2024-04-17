# shuntingyardalgopluscalc
Basic python implementation for Dijkstra's shunting yard algorithm including a calculator. Made by a CS/DS freshman.

First, a little bit of context:
Shunting yard algorithm is an algorithm devised by Esdger Dijkstra for converting ordinary infix mathematical operators into postfix (or RPN, the acronym for Reverse Polish Notation).
For example, you would write `3 + 4 * 5` as `3 4 5 * +`, and `3 / ( 2 + 1 )` as `3 2 1 + /`.

This algorithm makes it easier for machines to calculate math operations since it's closer to machine language. In fact, [HP used it in its earliest calculators in the 70s (e.g. HP-35 and HP-45)](https://en.wikipedia.org/wiki/Reverse_Polish_notation#Hewlett-Packard). It also eliminates the need for brackets, since the order of calculation depends on the order and placement of the operators themselves, and not on the conventional order of precedence used in infix.

Of course it's way more intuitive and easier for everyone to write math expressions in infix, but shunting yard is waaaaay too intriguing to ignore :) ... and so I made this implementation. Keep in mind, I'm still a CS/DS Major college freshman, and I didn't try to implement more complex data types than lists, soooo this is a very basic implementation for now.

> [!IMPORTANT]
> Read this guide on how the algorithm functions first: https://mathcenter.oxford.emory.edu/site/cs171/shuntingYardAlgorithm/
> Don't worry, I'll try to guide you through the code comments as much as I can. Enjoy!
