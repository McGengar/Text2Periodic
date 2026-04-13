# Text2Periodic
## Is this made of Phosphorus, Yttrium, Thorium, Oxygen and Nitrogen? Because this is PYThON!
This is a small project of mine, that, if possible, translates any text to elements in periodic table.

For example, if your input is word "Polish", output will be:

<code>Are you made of Polonium Lithium Sulfur Hydrogen ?  
Because you are PoLiSH</code>


Right now it is very simple, as it only checks if next 2 or 1 letters can be represented as an elements, and if so it saves it and goes on with the input. However it has some problems.
For example, lets say we check for first one letter match, in that case, word "sec" is impossible. We will find "S" and then the rest "ec" can't be represented as any combination of elements.
I chose other way around, scipt start searching for 2-letter match first, and then for 1-letter. It's still not perfect, as there are some phrases that are still impossible with this method, like "Crab", where if we start form "Cr" we trap ourselfs because there is no way to finish "ab", however if we start from just "C", we can complete our word with "Ra" and "B".

Maybe in the future i will optimise it to check for all possibilities, not just lock itself to 1 or 2-letter matches. In the meantime i hope you enjoy using this silly script.