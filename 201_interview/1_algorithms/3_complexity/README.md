# Complexity Interview Practice

## How to Use

### 1. Exercises (`1_exercises/`)

15 individual exercises, each in its own file. For each one:

1. Read the code snippet
2. Fill in your answers between the `YOUR ANSWER` markers
3. Optionally explain your reasoning in `EXPLANATION`
4. When done, ask Claude to evaluate: *"Evaluate my complexity answers in 1_exercises/"*

### 2. Speedrun (`2_speedrun/`)

30 rapid-fire questions in one file. Time yourself (target: 5 minutes).

1. Open `speedrun.py`
2. Fill in `TIME = "???"` and `SPACE = "???"` for all 30 questions
3. When done, ask Claude to evaluate: *"Evaluate my speedrun answers"*

### Rules

- Do NOT look at `_answers/` before completing the exercises
- Write Big-O notation like: `"O(1)"`, `"O(n)"`, `"O(n^2)"`, `"O(n log n)"`, `"O(2^n)"`, `"O(m*n)"`
- The `EXPLANATION` field is optional but helps Claude give better feedback

### Answer Format

Every question uses this format for easy evaluation:

```python
# ===== YOUR ANSWER =====
TIME = "???"
SPACE = "???"
EXPLANATION = """???"""
# ===== END ANSWER =====
```

Replace `"???"` with your answer. That's it.

### Scoring

| Exercises (15) | Speedrun (30) | Level |
|---|---|---|
| 14-15 | 28-30 | Interview ready |
| 11-13 | 22-27 | Strong, review misses |
| 8-10 | 15-21 | Re-study patterns first |
| <8 | <15 | Go back to `200_algorithms/1_algorithms/3_complexity/` |
