# Sprint 2 Retrospective — CalcApp

**Date:** 08 July 2026  
**Developer:** Josiane Ishimwe

---

## What Went Well

- All 6 stories delivered across both sprints
- 21/21 tests passing with no failures
- CI pipeline running automatically and showing green
- Logging captured both successful operations and errors
- Error handling prevented app from crashing on 
  invalid input like division by zero and unknown operators
- History feature worked correctly showing all 
  calculations in order

---

## What Didn't Go Well

- Sprint 1 and Sprint 2 were planned and partly 
  executed on the same day, which made the sprint 
  separation less clear than it should be in real practice
- Some documentation commits combined Sprint 1 and 
  Sprint 2 content instead of keeping them separate

---

## Did Sprint 1 Improvements Help?

**Improvement 1: Commit per feature**  
Yes — later commits were more focused and descriptive, 
making the history easier to follow

**Improvement 2: Only push files with content**  
Yes — the final commits show green CI instead of red, 
confirming that pushing complete code makes the 
pipeline more reliable

---

## Overall Project Lessons

**About Agile:**  
Working in sprints forces you to think about priority. 
Knowing Sprint 1 only covers addition, subtraction, 
and multiplication meant I could focus completely 
without being distracted by division or history features.

**About DevOps:**  
Setting up CI early was the right decision. Seeing 
the red crosses on early commits actually helped me 
understand what the pipeline was checking — it made 
the green tick on the final commit feel meaningful.

**About estimating:**  
The simple operations (add, subtract, multiply) were 
accurately estimated at 2 points each. Division with 
error handling deserved its 3 points because edge 
cases like divide by zero required extra thought.

**About myself:**  
I work better when I break tasks into very small steps. 
The commit-per-feature approach kept me focused and 
made progress visible even when the full feature 
wasn't done yet.

---

## What I Would Do Differently

- Start with tests written BEFORE the code (TDD — 
  Test Driven Development) so CI is green from the start
- Keep Sprint 1 and Sprint 2 on separate days to make 
  the timeline clearer
- Add more edge case tests (e.g. very large numbers, 
  floating point precision)

---

## Final Self Assessment

| Area | Score |
|---|---|
| Agile practice quality | 4/5 |
| DevOps implementation | 4/5 |
| Commit discipline | 3/5 |
| Test coverage | 5/5 |
| Reflection depth | 4/5 |

**Most proud of:** 21/21 tests passing and the 
logging system working automatically on every operation

**Will improve next project:** Keeping sprints on 
separate days and committing more granularly 
per individual function