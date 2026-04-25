# ✊✋✌️ Rock Paper Scissors — CLI Game

A Python command-line Rock Paper Scissors game where you can challenge the computer at different difficulty levels.

---

## 🎮 Features

- **4 Difficulty Levels** — from a helpless opponent to a tricky adaptive one
- **Custom Round Count** — you choose how many rounds to play
- **Live Score Tracking** — see the score after every round
- **Input Validation** — handles invalid input gracefully with re-prompts

---

## 🧠 Difficulty Levels

| Level | Name        | Strategy |
|-------|-------------|----------|
| 1     | Super Easy  | Always plays `rock` |
| 2     | Easy        | Cycles through rock → paper → scissors in order |
| 3     | Medium      | Mirrors your last move |
| 4     | Hard        | Plays completely at random |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.x

### Run the Game

```bash
git clone https://github.com/your-username/rock-paper-scissors.git
cd rock-paper-scissors
python rps.py
```

---

## 🕹️ How to Play

1. Run the script
2. Select a difficulty level (1–4)
3. Enter the number of rounds
4. Type `rock`, `paper`, or `scissors` each round
5. See who wins!

---

## 📁 Project Structure

```
rock-paper-scissors/
│
├── rps.py          # Main game file
└── README.md       # Project documentation
```

---

## 📌 Example Output

```
Select a level:
  1 - Super Easy
  2 - Easy
  3 - Medium
  4 - Hard
Your choice: 3

How many rounds do you want to play? 3

Game start!

--- Round 1 ---
Rock, Paper, or Scissors? rock
You: rock  |  Computer: rock
It's a tie this round!
Score: You 0 : 0 Computer
...
=== Final Score: You 2 : 1 Computer ===
You won the game! Congratulations!
```

---

## 🛠️ Built With

- Python 3 — standard library only (`random`, no external dependencies)

