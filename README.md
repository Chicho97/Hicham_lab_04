# Lab 4 - Goldbach and Large-Number Arithmetic

This project contains two independent Python programs required by Lab 4.

## Files

- `goldbach.py`: reads an even integer greater than 2, checks primality with a function, and prints every distinct pair `(p, q)` where `p + q` equals the input and `p <= q`.
- `numere_mari.py`: reads two non-negative integers from `numere.txt` and calculates their sum and product using digit-by-digit algorithms. The complete numbers remain strings; only individual digits are converted to integers.
- `numere.txt`: sample input, with one number per line (`999` and `2`).
- `tests/test_lab4.py`: optional automated tests.

## Requirements

- Python 3.10 or newer.
- No third-party packages are required.

## Run the programs

```bash
python goldbach.py
python numere_mari.py
```

For `goldbach.py`, try `10`. Expected pairs: `3 + 7` and `5 + 5`.

For `numere_mari.py`, the provided file contains `999` and `2`. Expected sum: `1001`; expected product: `1998`.

## Run tests

From this folder:

```bash
python -m unittest discover -s tests -v
```

## Git branches and Pull Requests required by the assignment

1. Work on `feature/goldbach`, commit the Goldbach solution, push the branch, open a Pull Request targeting `main`, review it, and merge it.
2. Create `feature/big-numbers` from the updated `main`, commit the large-number solution, push the branch, open a Pull Request targeting `main`, review it, and merge it.

The public GitHub repository must be named `name_lab_04` (replace `name` with your own name). Keep the two tasks in separate Python files.
