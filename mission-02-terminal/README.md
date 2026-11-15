# Mission 2 - Become comfortable with the Terminal

## 1. Task / objective
Practise navigation, directory listings, safe file creation, copying, renaming, reading files, flags, pipes, and package-manager inspection.

## 2. Work completed
Created `terminal-practice/notes.txt`, wrote a first line, appended a second, copied it, renamed the copy to `backup-notes.txt`, and read both files. The original and backup each contained the two expected lines. No files outside this assignment repository were changed.

| Operation | Command used | What it does / observation |
|---|---|---|
| Current directory | `pwd` | Prints the current folder path. For privacy, the account portion of the path is redacted in this report. |
| Directory listing | `ls` | Lists names in the current folder. In `terminal-practice`, it showed `notes.txt` and `backup-notes.txt`. |
| Detailed listing | `ls -la` | Shows hidden entries, permissions, sizes, and dates. The notes files had `-rw-r--r--` permissions and were 39 bytes each. |
| Change directory | `cd ..` | Moves to the parent folder; running `pwd` there showed the parent, then I returned to the project. |
| Create directory | `mkdir terminal-practice` | Created the practice folder inside the repository. |
| Create empty file | `touch terminal-practice/notes.txt` | Created the empty notes file before adding text. |
| Copy file | `cp terminal-practice/notes.txt terminal-practice/notes-copy.txt` | Made an independent copy of the notes. |
| Move / rename file | `mv terminal-practice/notes-copy.txt terminal-practice/backup-notes.txt` | Renamed the copy; the original remained. |
| Display file contents | `cat terminal-practice/notes.txt` | Printed both lines: “First line of text” and “Second line of text”. |

### Task 2.2: Safe file changes
Replacing with `>` overwrites the file contents. Appending with `>>` adds text after what is already there. `cp` leaves the source and creates another file; `mv` relocates or renames the existing file. `pwd` tells me which folder relative paths apply to, and `ls` helps me check the available files before acting.

### Task 2.3: Flags and pipes
`ls -lah terminal-practice` showed the entries including `.` and `..`, file permissions, and human-readable sizes. `-l` requests a detailed listing, `-a` includes hidden entries, and `-h` makes sizes easier to read. `ls -l | head -n 5` sent the listing from `ls` into `head`, which displayed its first five lines.

### Task 2.4: Package managers
Homebrew was installed. `brew --version` reported Homebrew 7.0.12, and `brew list` displayed installed package names. I did not install, update, or remove packages. A package manager keeps track of software packages and can help install or update them consistently from configured sources.

## 3. Commands / tools used
- `pwd`, `ls`, `ls -la`, `cd ..` - checked location and contents.
- `mkdir`, `touch`, `echo ... >`, `echo ... >>`, `cp`, `mv`, and `cat` - practised file operations within the repository.
- `ls -lah` and `ls -l | head -n 5` - inspected flags and a pipe.
- `brew --version` and `brew list` - checked Homebrew without changing installed software.
- Git - staged, committed, and pushed this mission checkpoint.

## 4. My understanding
Terminal commands act on the current folder, so checking `pwd` before a file operation helps prevent mistakes. Redirection with `>` replaces data, while `>>` preserves earlier data and adds to it. A pipe passes one command's output to another command, which can filter or shorten it.

## 5. Difficulties faced
No major difficulties.

## 6. How I resolved them
Not applicable.

## 7. Evidence / files
- `terminal-practice/notes.txt` - original two-line practice file.
- `terminal-practice/backup-notes.txt` - renamed copy of the file.
- `mission-02-terminal/README.md` - commands, observations, and explanations.

## 8. Commit details
- **Commit message:** `Complete Terminal and file management mission`
- **Status:** To be pushed and verified on GitHub.
