# Python Beginning

My notes and practice code while learning Python. The goal is to build a solid
Python foundation before moving on to NumPy, pandas and machine learning.

Every lesson is a small, runnable script with comments. Every exercise is a
complete mini-program written after the matching lessons.

## Repository structure

```
Python-Beginning/
├── Lessons/       # one folder per topic, scripts with explanatory comments
├── Exercises/     # practice programs, from easy to harder
├── pyproject.toml # project metadata and dependencies
└── uv.lock        # locked dependency versions
```

## Getting started

This project uses [uv](https://docs.astral.sh/uv/) for the environment.

```bash
git clone https://github.com/Huseynov-Huseyn/Python-Beginning.git
cd Python-Beginning
uv sync
uv run python Lessons/17Functions/DefaultArguments.py
```

Some scripts use `matplotlib` (for example, the random numbers lesson). It is
installed by `uv sync`.

## Lessons

| #  | Topic                                                                                                                                                         |
|----|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1  | Beginning (first program, `print`)                                                                                                                            |
| 2  | Variables and data types                                                                                                                                      |
| 3  | Type casting                                                                                                                                                  |
| 4  | User input                                                                                                                                                    |
| 5  | Arithmetic, math and membership operators                                                                                                                     |
| 6  | `if` statements                                                                                                                                               |
| 7  | Logical operators                                                                                                                                             |
| 8  | Conditional expressions (ternary operator)                                                                                                                    |
| 9  | String methods                                                                                                                                                |
| 10 | String indexing and slicing                                                                                                                                   |
| 11 | Format specifiers                                                                                                                                             |
| 12 | Loops: `for`, `while`, nested loops                                                                                                                           |
| 13 | Collections: list, set, tuple, list comprehension                                                                                                             |
| 14 | Two-dimensional collections                                                                                                                                   |
| 15 | Dictionaries                                                                                                                                                  |
| 16 | Random numbers and Gaussian distribution                                                                                                                      |
| 17 | Functions: default, keyword and arbitrary arguments (`*args`, `**kwargs`)                                                                                     |
| 18 | Iterables: comprehensions, generators, custom iterators                                                                                                       |
| 19 | `match` / `case` statement                                                                                                                                    |
| 20 | Modules                                                                                                                                                       |
| 21 | Variable scope and the LEGB rule                                                                                                                              |
| 22 | `if __name__ == "__main__"`                                                                                                                                   |
| 23 | Object-oriented programming: classes, class variables, inheritance, class and static methods, multiple inheritance, `super()`, polymorphism, abstract classes |

## Exercises

| #  | Exercise                                                                                                                                                     |
|----|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1  | Mad Libs game                                                                                                                                                |
| 2  | Calculator                                                                                                                                                   |
| 3  | Temperature and weight converters                                                                                                                            |
| 4  | Input validation                                                                                                                                             |
| 5  | Compound interest calculator                                                                                                                                 |
| 6  | Countdown timer and stopwatch                                                                                                                                |
| 7  | Hollow rectangle                                                                                                                                             |
| 8  | Pyramid and diamond                                                                                                                                          |
| 9  | Shopping cart                                                                                                                                                |
| 10 | Quiz game                                                                                                                                                    |
| 11 | Concession stand                                                                                                                                             |
| 12 | Collections and dictionaries (favorite fruits, student grades, unique numbers, word counter, phone book, group by length, inventory manager, anagram groups) |
| 13 | Random: dice roller, number guessing, rock paper scissors                                                                                                    |
| 14 | Banking program (ATM)                                                                                                                                        |
| 15 | Slot machine                                                                                                                                                 |
| 16 | Encryption                                                                                                                                                   |
| 17 | Hangman                                                                                                                                                      |
| 18 | Tic-Tac-Toe (player vs. computer)                                                                                                                            |
| 19 | Blackjack                                                                                                                                                    |

## Notes

- Code is written for learning, so comments explain the idea behind each topic.
- Scripts are meant to be run one by one from the project root.

## License

See the [LICENSE](LICENSE) file.