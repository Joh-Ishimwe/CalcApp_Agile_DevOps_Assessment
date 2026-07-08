# CalcApp Product Backlog

## Product Vision
For anyone who needs quick calculations, CalcApp is a 
simple command-line calculator that performs basic 
arithmetic operations reliably and accurately.

## User Stories

### Story 1 — Addition
**As a** user,  
**I want to** add two numbers,  
**So that** I can get their sum.

**Estimate:** 2 points  
**Priority:** HIGH

**Acceptance Criteria:**
- User can enter two numbers
- App returns correct sum
- Works with decimals
- Works with negative numbers
- Result displays clearly (e.g. 2 + 3 = 5)

---

### Story 2 — Subtraction
**As a** user,  
**I want to** subtract two numbers,  
**So that** I can find the difference.

**Estimate:** 2 points  
**Priority:** HIGH

**Acceptance Criteria:**
- User can enter two numbers
- App returns correct difference
- Works with decimals
- Works with negative numbers
- Result displays clearly (e.g. 5 - 3 = 2)

---

### Story 3 — Multiplication
**As a** user,  
**I want to** multiply two numbers,  
**So that** I can get the product.

**Estimate:** 2 points  
**Priority:** HIGH

**Acceptance Criteria:**
- User can enter two numbers
- App returns correct product
- Works with decimals
- Works with negative numbers
- Result displays clearly (e.g. 3 * 4 = 12)

---

### Story 4 — Division
**As a** user,  
**I want to** divide two numbers,  
**So that** I can get the result.

**Estimate:** 3 points  
**Priority:** HIGH

**Acceptance Criteria:**
- User can enter two numbers
- App returns correct result
- Works with decimals
- Works with negative numbers
- Result displays clearly (e.g. 10 / 2 = 5)

---

### Story 5 — Division by Zero Error
**As a** user,  
**I want to** see an error when dividing by zero,  
**So that** the app doesn't crash.

**Estimate:** 3 points  
**Priority:** MEDIUM

**Acceptance Criteria:**
- App does NOT crash when dividing by zero
- Clear error message shown
- App continues running after error
- All other operations still work

---

### Story 6 — Calculation History
**As a** user,  
**I want to** see a history of my calculations,  
**So that** I can review past results.

**Estimate:** 4 points  
**Priority:** LOW

**Acceptance Criteria:**
- Every calculation saved automatically
- User types 'history' to see all past calculations
- History shows in order from first to latest
- Each entry shows full calculation

---

## Definition of Done
Every story must meet ALL of these before counting as complete:

- [ ] Code written and working locally
- [ ] All acceptance criteria met
- [ ] At least one unit test written
- [ ] All tests passing
- [ ] CI pipeline passing on GitHub
- [ ] Code committed with clear message
- [ ] No crashes or unhandled errors