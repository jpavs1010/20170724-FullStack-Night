# Lab 4: Guess the Number


Let's re-create our 'guess the number' lab in a web page. We'll need to use `Math.random()` and some arithmetic to generate a number for the computer. Then we'll need a text input and a button for the user to submit their guess. Then compare the user's guess to the computer's guess and use `alert` to tell the user whether it was correct or incorrect.

Below is a template and demonstration of how a JavaScript function is invoked from a button.

```HTML
<html>
    <head>
        <script>
            // pick a random int between 1 and 10 using Math.random() and Math.floor()
            function check_guess()
            {
                // get the value from the text input, convert it to an int
                // compare it to the computer's guess
                // if it's right, show 'correct!'
                // if it's not, show 'incorrect!'
            }
        </script>
    </head>
    <body>
        <button onclick="check_guess()">click me</button>
    </body>
</html>
```

## Version 2

Instead of using an `alert`, you can have two div, one which says 'correct' and the other which says 'incorrect', and toggle their visibility (alternate between `display:none` and `display:block` or `display:inline`.

Keep track of the number of guesses, display that number to the user.

Keep track of their previous guesses, if they repeat a number, indicate that to the user.

Also display higher/lower (and closer/further if you want)

## Version 3

Using Javascript, automatically generate a button for each number that can be guessed. When a user clicks a button, check if they're correct. When the user runs out of guesses or guesses correctly, disable everything, and give them the option to start over. 
