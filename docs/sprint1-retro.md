# Sprint 1 Retrospective — CalcApp

**Date:** 08 July 2026  
**Developer:** Josiane Ishimwe

---

## What Went Well

- CI pipeline was set up successfully and triggered 
  automatically on every push
- All 3 Sprint 1 stories were delivered within the sprint
- All 21 unit tests passed on first full run
- Logging was implemented and working from the start
- Commit history shows clear incremental progress

---

## What Didn't Go Well

- Early commits triggered red CI checks because code 
  was incomplete at the time of pushing — should have 
  ensured at least basic tests existed before first push
- Some commits were grouped together rather than being 
  split per feature — for example, Sprint 1 and Sprint 2 
  documentation was committed together in one message

---

## What Puzzled Me

- Understanding why the CI pipeline showed red on early 
  commits even though the final result was correct
- The difference between committing empty files vs 
  files with content and how that affects the pipeline

---

## Improvements for Sprint 2

**Improvement 1:**  
What went wrong: Some commits combined multiple changes  
How I will fix it: Commit immediately after each individual 
function works — one commit per story feature

**Improvement 2:**  
What went wrong: CI showed red on early pushes because 
files were empty  
How I will fix it: Only push code files after they have 
at least basic content and tests written

---

## Estimation Accuracy

| Story | Estimated | Felt |
|---|---|---|
| Story 1: Addition | 2 pts | About right |
| Story 2: Subtraction | 2 pts | About right |
| Story 3: Multiplication | 2 pts | About right |

**Lesson for Sprint 2:** Estimates were accurate for 
simple operations. Division and error handling may need 
slightly more buffer since they involve edge cases.