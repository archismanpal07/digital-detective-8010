# Mission 4 - How programs run

## 1. Task / objective
Create and run a small Python program and compare compilation with interpretation.

## 2. Work completed
Created `hello.py` and ran it with Python 3. It printed `Hello from Python`.

| Point | Compiler | Interpreter |
|---|---|---|
| When translation / execution happens | Commonly translates source code before execution. | Executes program instructions at runtime. |
| Typical output | Often produces an executable or other translated form. | Produces the program's output while running; it may also use an intermediate form. |
| One example | A C compiler such as Clang | The Python interpreter |
| One advantage | The translated program can run efficiently without translating source each time. | Convenient to run and change code during development. |

A compiler usually translates source code before the program runs, while an interpreter executes instructions at runtime. The distinction is not absolute: language implementations can combine approaches. Python's standard interpreter compiles source to bytecode and then executes that bytecode. Running the sample demonstrated that Python can run a `.py` file directly from Terminal.

## 3. Commands / tools used
- `python3 mission-04-programs/hello.py` - ran the script using Python 3.14.7.
- `print()` - displayed the message in the Terminal.
- Git - staged, committed, and pushed the program and notes.

## 4. My understanding
Source code is written for people to read, so a language implementation must translate or execute it in a form the computer can use. A compiler often translates ahead of time; an interpreter performs execution at runtime. Real language implementations may combine both methods.

## 5. Difficulties faced
No major difficulties.

## 6. How I resolved them
Not applicable.

## 7. Evidence / files
- `mission-04-programs/hello.py` - one-line Python program.
- `mission-04-programs/README.md` - execution result and compiler/interpreter comparison.

## 8. Commit details
- **Commit message:** `Compare compilers and interpreters`
- **Status:** To be pushed and verified on GitHub.
