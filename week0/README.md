# Week 0 – Functions, Variables
Problem Set 0 from CS50P, covering basic input/output, string methods, and writing simple functions.

## indoor.py — Indoor Voice
Takes a line of text from the user and prints it back entirely in lowercase, since typing in all caps is like yelling. Punctuation and spacing stay unchanged.

## playback.py — Playback Speed
Takes a line of text and prints it back with every space replaced by `...`, mimicking a slowed-down "playback speed" effect (e.g. `This is CS50` → `This...is...CS50`).

## faces.py — Making Faces
Converts old-school emoticons into emoji: `:)` becomes 🙂 and `:(` becomes 🙁, with everything else left as-is. Implemented as a `convert` function (does the work) called from a `main` function (handles input/output) — first practice separating logic from I/O.

## einstein.py — Einstein
Calculates mass–energy equivalence using Einstein's E = mc². Takes a mass in kilograms as input and outputs the equivalent energy in Joules (using the speed of light as 300,000,000 m/s).

## tip.py — Tip Calculator
Completes a partially-written tip calculator by implementing two helper functions: one that strips the `$` from a price string and converts it to a float, and one that strips the `%` from a tip percentage and converts it to a decimal. Together with the provided `main`, it calculates and prints how much to tip on a restaurant bill.
