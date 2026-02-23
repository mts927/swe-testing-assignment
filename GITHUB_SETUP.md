# GITHUB SETUP INSTRUCTIONS

## Quick Guide to Push Your Project to GitHub

Follow these steps to upload the local Quick-Calc project to GitHub:

### Step 1: Create a GitHub Repository
1. Go to https://github.com/new
2. Fill in the repository details:
   - **Repository name**: `swe-testing-assignment`
   - **Description**: A calculator application with comprehensive testing strategy
   - **Visibility**: Select "Public" (required for submission)
   - **Do NOT initialize** with README, .gitignore, or license (we already have these)
3. Click "Create repository"

### Step 2: Add Remote and Push Code
After creating the repository, GitHub will show you the commands to push an existing repository. Run these commands in your terminal:

```bash
cd c:\Users\33787\Downloads\devoir

git remote add origin https://github.com/YOUR_USERNAME/swe-testing-assignment.git
git branch -M main
git push -u origin main
```

Replace `YOUR_USERNAME` with your actual GitHub username.

### Step 3: Push Tags
Push the v1.0.0 release tag to GitHub:

```bash
git push origin v1.0.0
```

### Step 4: Create Release on GitHub
1. Go to your repository: https://github.com/YOUR_USERNAME/swe-testing-assignment
2. Click on "Releases" on the right sidebar
3. Click "Create a new release"
4. Select the tag "v1.0.0"
5. Set title to "Quick-Calc v1.0.0"
6. Copy the release notes from below and paste them into the description
7. Click "Publish release"

### Release Notes for v1.0.0

```
# Quick-Calc v1.0.0

## Features
- ✅ Addition, subtraction, multiplication, and division operations
- ✅ Graceful handling of division by zero
- ✅ Clear operation to reset the calculator
- ✅ Support for decimal numbers and negative numbers
- ✅ Clean, professional code architecture

## Testing
- ✅ 10 comprehensive unit tests covering all operations
- ✅ 6 integration tests covering complete user workflows
- ✅ All tests passing successfully
- ✅ Edge cases handled (division by zero, large numbers, decimals)

## Documentation
- ✅ Professional README.md with setup instructions
- ✅ Comprehensive TESTING.md with lecture concept analysis
- ✅ Framework research comparing pytest vs unittest
- ✅ Clear, descriptive commit history (5+ commits)

## Testing Framework
- **Framework**: pytest 7.4.3
- **Language**: Python 3.8+

## How to Run Tests
```bash
pip install -r requirements.txt
pytest tests/ -v
```

All tests pass successfully! ✅
```

### Step 5: Submit Your GitHub Link
After pushing to GitHub, create a file named `github_link.txt` in your project directory:

```
https://github.com/YOUR_USERNAME/swe-testing-assignment
```

---

## Verification Checklist

Before submitting, verify that your GitHub repository meets all requirements:

- [ ] Repository is named `swe-testing-assignment`
- [ ] Repository is PUBLIC
- [ ] README.md is present and professional
- [ ] TESTING.md is present with lecture concept analysis
- [ ] Minimum 5 meaningful commits visible in commit history
- [ ] All commits use clear, descriptive messages (Conventional Commits)
- [ ] v1.0.0 release tag is created and visible under "Releases"
- [ ] All test files are present (tests/test_calculator.py, tests/test_integration.py)
- [ ] requirements.txt includes pytest
- [ ] .gitignore is properly configured

---

## Required File Contents for Submission

You need to submit ONE file:
- **github_link.txt**: Contains the full URL to your public GitHub repository

Example content:
```
https://github.com/student123/swe-testing-assignment
```

---

## Common Troubleshooting

### Error: "fatal: remote origin already exists"
If you see this error, run:
```bash
git remote remove origin
git remote add origin https://github.com/YOUR_USERNAME/swe-testing-assignment.git
```

### Error: "Authentication failed"
GitHub now requires personal access tokens. See: https://github.com/settings/tokens

### Commits not showing up
Make sure you:
1. Set global Git user: `git config --global user.name "Your Name"` and `git config --global user.email "your@email.com"`
2. Used `git push` to push commits
3. Refreshed your browser

---

## Next Steps

1. ✅ **Done**: Local project setup and testing
2. ⏭️ **Next**: Push to GitHub following the steps above
3. ⏭️ **Final**: Submit github_link.txt file

Good luck with your submission!
