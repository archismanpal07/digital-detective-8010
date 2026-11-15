# Mission 3 - Understand the operating system

## 1. Task / objective
Inspect the operating system, account context, storage, processes, paths, and permissions; explain the operating system's responsibilities.

## 2. Work completed
Checked system details with `uname -srm` and `sw_vers`, checked the active account command without recording its value, inspected available disk space, opened Activity Monitor, and checked the practice file permissions. Machine and account identifiers are omitted or redacted.

| Information explored | What it tells me | Privacy-safe observation |
|---|---|---|
| Operating system / system details | Identifies the OS environment and processor architecture. | macOS 27.2.1; Darwin kernel reports 27.2.0; `arm64` architecture. |
| Current account identity | Identifies the account running commands. | `whoami` succeeded; account name recorded as `[redacted]`. |
| Available and used storage | Shows space on the volume containing the project. | At the time checked, the volume showed 926 GiB total and 744 GiB available. |
| System activity snapshot | Shows running processes and resource use. | Activity Monitor was opened. Chrome and Activity Monitor were running applications during the observation. I did not record user names or process identifiers. |

### Task 3.2: Processes
A process is a running instance of a program. PID means process identifier, a number the operating system uses to distinguish processes. Examples observed as running applications were Chrome and Activity Monitor. Process IDs can change when apps restart.

### Task 3.3: Paths and permissions
- **Absolute path example:** `/Users/[redacted]/Desktop/digital-detective-8010/mission-03-operating-system`
- **Relative path example:** `mission-03-operating-system` when the current directory is the repository root.
- **Observed permission:** `-rw-r--r--` for `terminal-practice/notes.txt`. The first `-` indicates a regular file. The owner can read and write; group and other users can read it. No permission settings were changed.

### Task 3.4: Operating-system responsibilities

| Responsibility | Explanation | Example |
|---|---|---|
| Process management | Starts programs and schedules their use of the processor. | Running Chrome while Terminal is open. |
| Memory management | Allocates memory to programs and reclaims it when no longer needed. | Chrome and other apps use working memory while open. |
| Device management | Coordinates communication between software and hardware. | The OS receives keyboard input and draws the screen. |
| File management | Organizes files and folders and tracks their properties. | Saving a README inside its mission folder. |
| User interface / shell | Provides ways to control the computer graphically or with commands. | Finder and Terminal. |
| Security and permissions | Controls access to accounts, files, and system resources. | File permissions limit who can edit a file. |

## 3. Commands / tools used
- `uname -srm` and `sw_vers -productVersion` - checked kernel, architecture, and macOS version.
- `whoami` - checked that an account identity is available; the value was not recorded.
- `df -h .` - checked storage for the project volume.
- Activity Monitor - inspected the process-monitoring interface.
- `stat -f '%Sp %N' terminal-practice/notes.txt` - read file permissions without changing them.
- Git - committed and pushed this mission checkpoint.

## 4. My understanding
The operating system coordinates programs, memory, files, and devices, and it enforces permissions. A process is one running program instance. Absolute paths start at the filesystem root, while relative paths depend on the current directory.

## 5. Difficulties faced
The command-line process snapshot was blocked by the system environment, so I used Activity Monitor for the process observation instead.

## 6. How I resolved them
Opened Activity Monitor and recorded only the running applications observed, without copying account names or process identifiers.

## 7. Evidence / files
- `mission-03-operating-system/README.md` - privacy-safe system observations, process notes, paths, permissions, and OS responsibilities.
- `terminal-practice/notes.txt` - file used to inspect permissions.

## 8. Commit details
- **Commit message:** `Document operating system and file management`
- **Status:** To be pushed and verified on GitHub.
