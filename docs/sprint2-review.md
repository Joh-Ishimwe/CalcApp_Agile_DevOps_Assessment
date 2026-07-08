# Sprint 2 Review — CalcApp

**Date:** 08 July 2026  
**Developer:** Josiane Ishimwe

---

## Sprint Goal
Complete the calculator with division, error handling, 
calculation history, and logging. Apply improvements 
from Sprint 1 retrospective.

---

## Sprint 1 Improvements Applied

**Improvement 1:** Commit per feature not per session  
Applied: ✅ Yes  
Evidence: Separate commits for calculator structure, 
tests, and documentation visible in commit history

**Improvement 2:** Only push files with content  
Applied: ✅ Yes  
Evidence: Final commits show green CI pipeline ✅

---

## Planned vs Delivered

| Story | Points | Status |
|---|---|---|
| Story 4: Division | 3 | ✅ Completed |
| Story 5: Division by zero error | 3 | ✅ Completed |
| Story 6: Calculation history | 4 | ✅ Completed |

**Stories planned:** 3  
**Stories delivered:** 3  
**Points planned:** 10  
**Points delivered:** 10  

---

## Definition of Done Checklist

- [x] Code written and working locally
- [x] All acceptance criteria met
- [x] Unit tests written for each story
- [x] All Sprint 1 and Sprint 2 tests passing (21/21)
- [x] CI pipeline passing on GitHub
- [x] Logging added to all operations
- [x] Error handling working correctly
- [x] Code committed with clear messages
- [x] No crashes or unhandled errors

---

## Monitoring and Logging Evidence

Logging captures every operation automatically:

2026-07-08 10:57:15,968 - INFO - Addition: 3.0 + 2.0 = 5.0
2026-07-08 10:59:10,340 - INFO - Subtraction: 6.0 - 2.0 = 4.0
2026-07-08 10:59:37,781 - ERROR - Division by zero attempted
2026-07-08 10:59:46,797 - INFO - Division: 5.0 / 2.0 = 2.5

- INFO logs record every successful calculation
- ERROR logs capture failed operations (e.g. divide by zero)
- Timestamps on every log entry for full traceability

---

## Demo Evidence

### Division
Enter calculation: 5 / 2
2026-07-08 - INFO - Division: 5.0 / 2.0 = 2.5
Result: 5.0 / 2.0 = 2.5

### Division by Zero Error
Enter calculation: 5 / 0
2026-07-08 - ERROR - Division by zero attempted
Error: Cannot divide by zero

### App continues after error
Enter calculation: 3 * 4
Result: 3.0 * 4.0 = 12.0

### Calculation History
Enter calculation: history
--- Calculation History ---

3.0 + 2.0 = 5.0
6.0 - 2.0 = 4.0
5.0 / 2.0 = 2.5
3.0 * 4.0 = 12.0



### Unknown operator handled
Enter calculation: 5 : 0
Unknown operator ':'. Use +, -, *, /

---

## Full Project Summary

| Metric | Result |
|---|---|
| Total stories delivered | 6/6 |
| Total story points delivered | 16/16 |
| All tests passing | ✅ 21/21 |
| CI pipeline working | ✅ Green |
| Logging implemented | ✅ INFO + ERROR |
| Error handling working | ✅ |
| History feature working | ✅ |