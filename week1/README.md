## Week 1 – Conditionals

Problem Set 1 from CS50P, covering `if`/`elif`/`else` logic, string methods, and structuring code with helper functions.

### deep.py — Deep Thought
Asks the user for "the answer to life, the universe, and everything" and prints `Yes` if they answer `42`, `forty-two`, or `forty two` (case- and space-insensitive), otherwise `No`.

### bank.py — Home Federal Savings Bank
Asks for a greeting and prints how much money it's "worth": `$0` for a greeting starting with "hello", `$20` for one starting with just "h", and `$100` for anything else — case-insensitive, ignoring leading spaces.

### extensions.py — File Extensions
Asks for a filename and prints its likely media (MIME) type based on the extension (`.jpg` → `image/jpeg`, `.pdf` → `application/pdf`, etc.), defaulting to `application/octet-stream` for anything unrecognized.

### interpreter.py — Math Interpreter
Asks for a simple expression like `1 + 1` and evaluates it, printing the result as a float rounded to one decimal place. Handles `+`, `-`, `*`, and `/`.

### meal.py — Meal Time
Asks for a 24-hour time (e.g. `7:30`) and prints whether it falls in the breakfast (7:00–8:00), lunch (12:00–13:00), or dinner (18:00–19:00) window — printing nothing if it's outside all three. Uses a separate `convert` function to turn the time string into a float number of hours.
