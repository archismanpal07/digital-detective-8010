# Mission 6 - Git and GitHub

## 1. Task / objective
Practise Git status, staging, commits, history, and branches; add a short learning section to the root README; publish the branch and open a Pull Request.

## 2. Work completed
Reviewed the repository status and commit history. Created the `update-about` branch, added a `My Learning` section to the root README, documented the Git workflow, and published the branch. Opened a Pull Request from `update-about` into `main`; it is left open for review.

| Git operation | What it does |
|---|---|
| Check repository status | `git status` shows the current branch and changed, staged, or untracked files. |
| Stage selected changes | `git add README.md` selects the root README update for the next commit. |
| Create a commit | `git commit -m "Complete Git and GitHub collaboration mission"` records staged changes in local history. |
| View commit history | `git log --oneline` lists recent commits. |

Staging prepares selected changes for a commit. The commit then saves those selected changes as a checkpoint. A branch is a separate line of work; a Pull Request asks for review of changes before they are merged. They help contributors discuss changes without putting unreviewed work directly on the main branch.

## 3. Commands / tools used
- `git status` - checked the working tree and current branch.
- `git add README.md mission-06-git-github/` - staged the README update and this mission notes.
- `git commit -m "Complete Git and GitHub collaboration mission"` - saved the branch changes.
- `git log --oneline` - inspected recent history.
- `git switch -c update-about` - created and switched to the branch.
- `git push -u origin update-about` - published the branch and set its upstream.
- GitHub browser - created a Pull Request targeting `main`.

## 4. My understanding
A commit records a checkpoint in one branch. Staging lets me select exactly which file changes belong in that checkpoint. A branch keeps new work separate, and a Pull Request gives others a place to inspect and discuss it before merging.

## 5. Difficulties faced
The GitHub CLI was not authenticated, so I used the already signed-in GitHub browser to open the Pull Request after publishing the branch from Terminal.

## 6. How I resolved them
Used the authenticated browser session on the repository page to create the PR and verify its status.

## 7. Evidence / files
- `README.md` - contains the `My Learning` section on branch `update-about`.
- `mission-06-git-github/README.md` - Git workflow glossary and branch/PR explanation.
- Pull Request from `update-about` into `main` - open for review.

## 8. Commit details
- **Commit message:** `Complete Git and GitHub collaboration mission`
- **Status:** Branch pushed; Pull Request to `main` opened and left unmerged for review.
