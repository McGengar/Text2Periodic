# Text2Periodic
## Is this made of Phosphorus, Yttrium, Thorium, Oxygen and Nitrogen? Because this is PYThON!

### Introduction
This is a small project of mine that, if possible, translates any text to elements in the periodic table.

For example, if your input is word "Polish", the output will be:

<code>Are you made of Polonium Lithium Sulfur Hydrogen ?  
Because you are PoLiSH</code>

The algorithm got a lot better since the beginning. At first it was very simple, as it only checked if the next 2 or 1 letters can be represented as abbreviations of elements, and if so, it saves it and goes on with the input. However, it had some problems.
For example, lets say we check for first one letter match, in that case, word "sec" is impossible. We will find "S" and then the rest "ec" can't be represented as any combination of elements.
Second route isn't that much better, script starts searching for 2-letter match first, and then for 1-letter. There are some phrases that are still impossible with this method, like "Crab", where if we start form "Cr" we trap ourselfs because there is no way to finish "ab", however if we start from just "C", we can complete our word with "Ra" and "B".That was the state of the pogram until recently, when i moved entire logic to the recursive function.

### The Algorithm
```python
def text2periodic(e_dict,text,output=[]):
    N = len(text)  
    if N==0:  
        return True,output
    if text[0].capitalize() in e_dict.keys():
        output.append(text[0].capitalize())
        temp_bool,output =  text2periodic(e_dict, text[1:],output)
        if temp_bool:
            return True, output
        else:    
            output = output[:-1]
    if N>1 and text[0:2].capitalize() in e_dict.keys():
        output.append(text[0:2].capitalize())
        temp_bool,output = text2periodic(e_dict, text[2:],output)
        if temp_bool:
            return True, output
        else:    
            output = output[:-2]
    return False,output
```
Lets break it down.

Function takes a whole periodic table dictionary (may be unnecessary if we make it global), as well as our text input, and output, which isn't really a function parameter, rather it saves our output information between function executions. It also returns bool value of whether we found matches for our whole phrase or not, and we encountered dead end, as well as output, which is list of abbreviations from our periodic table in correct order.

When building recursive function we must consider our base cases, of which there are 2: either we checked the whole text and didn't encounter any problems, in which case we return True and our output, or we didn't find any match with our dictionary, then we return False and output we've got so far. For second case it's easy, we just return False and output at the end, so it only gets there if nothing happens before that. As for first case, we recognize checking whole phrase if it's length is 0. After all, if there is nothing to check, nothing can go wrong.

After we've got our base cases, we need our recursive cases, which are 2 big if statements in the middle, checking for 1-letter match and 2-letter match respectively. For example, if first letter of our text can be represented as an element in the periodic table, we add it to our output, and then the function executes itself with same dictionary, new output, and text without its first letter. Same thing will happen if we find 2-letter match in second if statement, except we will run function with text parameter without first 2 letters of course. We can expect that our new function execution either find another match and run recursively, or eventually run into either of our base statements, success or failure. In case of success, that is it, we found matches for whole phrase and we have our output ready. In case of failure, we must take a step back and try again, so we delete last one, or two elements of our output.
This is important because we might run into a problem described in the introduction, an the way we solve it is always checks both options. 

For exemple, let's say our text is "sec". It's length is obviously more than zero so we check fist letter. We found a match! It's "S", so we run our function recursively, now with saved output of ["S"] and text without first letter, "ec". Length is still more than than zero so we check first letter and fail to find match. We check first two letters and we still fail, so we fall into our base case of returning False and output. Now let's go back to our base function, which now saves False as a temporary bool, and updates output. if our temporary bool would be true, that would be that we eventually found all matches, but in that case we got False, so we need to remove "S" from output, because that route was a dead end. Then we move on to check first two letters, and from then on it works like previously.

### What's next?

Now that the algorithm has solved our most important problems and does its job, next step is probably to allow it to process multiple words, allow joke message to be customizable, and maybe add some graphical interface, maybe even generate meme images. For now, thank you for reading and i hope this silly project brings you a little bit of joy!