# Mission 5 - Numbers and data

## 1. Task / objective
Convert decimal, binary, and hexadecimal values by hand, check conversions with Python, write a small converter, and explain basic text encoding.

## 2. Work completed

### Task 5.1: Manual conversions

| Question | Working and answer |
|---|---|
| Decimal 13 to binary | Divide by 2: 13→6 remainder 1; 6→3 remainder 0; 3→1 remainder 1; 1→0 remainder 1. Read remainders upward: **1101**. |
| Decimal 25 to binary | 25→12 r1; 12→6 r0; 6→3 r0; 3→1 r1; 1→0 r1. Read upward: **11001**. |
| Binary 1010 to decimal | 1×2³ + 0×2² + 1×2¹ + 0×2⁰ = 8+2 = **10**. |
| Binary 1101 to decimal | 1×2³ + 1×2² + 0×2¹ + 1×2⁰ = 8+4+1 = **13**. |
| Hexadecimal A to decimal | A represents **10** in base 16. |
| Hexadecimal 1F to decimal | 1×16 + 15 = **31**. |
| Binary 1111 to hexadecimal | 1111₂ = 15₁₀ = **F₁₆**. |

### Task 5.2: Python verification

| Expression | Result |
|---|---|
| `bin(13)` | `0b1101` |
| `bin(25)` | `0b11001` |
| `int('1010', 2)` | `10` |
| `int('1101', 2)` | `13` |
| `int('A', 16)` | `10` |
| `int('1F', 16)` | `31` |
| `hex(int('1111', 2))` | `0xf` |

The Python results matched the manual conversions.

### Task 5.3: Converter tests

| Decimal input | Binary output | Hexadecimal output |
|---:|---:|---:|
| 13 | `1101` | `D` |
| 25 | `11001` | `19` |
| 255 | `11111111` | `FF` |

`input()` reads the entry as text; `int()` parses it as a decimal integer. `bin()` and `hex()` produce base-2 and base-16 strings with prefixes, which the program removes with `[2:]`. `upper()` makes hexadecimal letters uppercase. The program rejects non-integers and values that are not positive.

### Task 5.4: How text is stored
- Uppercase `A` is ASCII decimal **65**; lowercase `a` is **97**.
- An encoding standard maps characters to numeric values so systems can store and interpret text consistently.
- A character outside basic ASCII: **€**.

## 3. Commands / tools used
- `python3` expressions using `bin()`, `int(value, base)`, `hex()`, and `ord()` - checked conversions and character codes.
- `python3 mission-05-numbers-data/number_converter.py` - ran the converter with 13, 25, and 255.
- Git - committed and pushed the program and its documentation.

## 4. My understanding
Binary uses powers of 2 and hexadecimal uses powers of 16. One hexadecimal digit represents four binary bits, which makes long binary values shorter to write. Text is also stored as numbers; an encoding defines which character each number represents.

## 5. Difficulties faced
No major difficulties.

## 6. How I resolved them
Not applicable.

## 7. Evidence / files
- `mission-05-numbers-data/number_converter.py` - decimal-to-binary and decimal-to-hexadecimal converter.
- `mission-05-numbers-data/README.md` - conversion working, Python checks, test values, and encoding notes.

## 8. Commit details
- **Commit message:** `Build number converter and practise data representation`
- **Status:** To be pushed and verified on GitHub.
