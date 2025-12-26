# Phase 2 Capstone Project: Interactive ATM System

## 🎯 Project Overview
Build a **complete, working ATM system** that demonstrates all Phase 2 control flow concepts in a real-world application.

## 📋 Requirements & Learning Outcomes

### Concepts Used:
✅ **Lesson 6 (If/Else):** Age verification, account type checking  
✅ **Lesson 7 (If/Elif/Else):** Menu navigation, transaction type selection  
✅ **Lesson 8 (While Loops):** Main ATM menu loop, input validation  
✅ **Lesson 9 (For Loops):** Transaction history display  
✅ **Lesson 10 (Break/Continue):** Exit options, error handling  

## 💡 Feature List

### Core Features (Basic):
1. **Login System** (If/Else + While Loop)
   - Username & password
   - 3 attempts max (While loop + counter + break)
   - Account verification

2. **Main Menu** (If/Elif/Else + While Loop)
   - Check Balance
   - Withdraw Money
   - Deposit Money
   - View Transaction History
   - Exit

3. **Account Management** (Variables + If statements)
   - Account number
   - Balance tracking
   - Account holder name

4. **Transactions** (Arithmetic + If/Else)
   - Withdraw (balance check, limits)
   - Deposit (amount validation)
   - Balance updates

5. **Transaction History** (For Loop)
   - Display last 5 transactions
   - Transaction type, amount, date/time

6. **Error Handling** (If/Else + Continue)
   - Invalid amounts
   - Insufficient funds
   - Invalid menu choice

## 🎓 Starter Code Structure

```python
# ===== ATM SYSTEM - Phase 2 Capstone =====

# Step 1: Define account data (BEFORE login loop)
accounts = {
    "12345": {"password": "pass123", "name": "Ali Khan", "balance": 5000},
    "67890": {"password": "secure", "name": "Sara Ahmed", "balance": 8000}
}

# Step 2: Login system (While loop with attempts)
attempts = 0
logged_in = False
current_account = None

while attempts < 3 and not logged_in:
    # Get account number
    # Get password
    # Verify (if/else)
    # If correct: logged_in = True, break
    # If wrong: attempts += 1, continue
    pass

# Step 3: Main ATM menu (While loop, if/elif/else)
while logged_in:
    # Display menu
    # Get choice
    # If/elif/else for each option
    # Option to exit (break)
    pass

# Step 4: Implement each feature
```

## 📝 Implementation Guide

### Phase 1: Login System (Use Lesson 6 & 8)
- Create while loop: `while attempts < 3:`
- Get user input
- Use if/else to verify credentials
- If correct: set `logged_in = True`, `break`
- If incorrect: `attempts += 1`, display remaining attempts

### Phase 2: Main Menu (Use Lesson 7)
- Create while loop: `while logged_in:`
- Display menu options 1-5
- Get user choice
- Use if/elif/elif/elif/else for each option
- Exit option breaks the loop

### Phase 3: Transactions (Use Lesson 6)
- Withdraw:
  - Check if amount > 0
  - Check if balance sufficient
  - If both OK: update balance, continue
  - If not: display error, return to menu
- Deposit:
  - Similar structure

### Phase 4: Transaction History (Use Lesson 9)
- Store transactions in a list
- For loop: `for transaction in transactions:`
  - Print each transaction

### Phase 5: Error Handling (Use Lesson 10)
- Invalid menu choice: `continue` to show menu again
- Invalid amount: skip that transaction
- Break on exit option

## 🎮 Sample Execution

```
===== WELCOME TO BANK ATM =====
Enter Account Number: 12345
Enter Password: pass123

Welcome Ali Khan!
Balance: Rs. 5000

----- MAIN MENU -----
1. Check Balance
2. Withdraw Money
3. Deposit Money
4. Transaction History
5. Exit

Choose option (1-5): 2

Enter amount to withdraw: 1000
Withdrawal successful!
New Balance: Rs. 4000

Choose option (1-5): 1
Current Balance: Rs. 4000

Choose option (1-5): 5
Thank you for using our ATM. Goodbye!
```

## 📊 Data Structure Example

```python
# Account data
accounts = {
    "12345": {
        "password": "pass123",
        "name": "Ali Khan",
        "balance": 5000,
        "transactions": [
            {"type": "withdrawal", "amount": 500, "time": "2024-12-26 10:30"},
            {"type": "deposit", "amount": 2000, "time": "2024-12-25 15:45"}
        ]
    }
}
```

## 🚀 Extension Challenges

### Easy Extensions:
1. Add "Change Password" feature
2. Add daily withdrawal limit
3. Display formatted balance with commas

### Medium Extensions:
1. Add fee on withdrawals
2. Add interest calculation on balance
3. Add transfer between accounts (nested loops)

### Hard Extensions:
1. Save data to file (Phase 5)
2. Add PIN functionality
3. Add multiple account holders

## ✅ Grading Rubric

| Criteria | Points |
|----------|--------|
| Login system with attempts | 15 |
| Main menu works | 10 |
| Withdraw/Deposit logic | 20 |
| Balance updates correctly | 15 |
| Transaction history displays | 15 |
| Error handling | 10 |
| Code comments | 10 |
| **Total** | **95** |

## 📚 Concepts Checklist

- [ ] Used while loop for login attempts
- [ ] Used if/else for login verification
- [ ] Used if/elif/else for menu navigation
- [ ] Used while loop for main menu
- [ ] Used if statements for transaction validation
- [ ] Used break to exit loops
- [ ] Used for loop to display history
- [ ] Used continue for error handling
- [ ] Code has comments explaining logic
- [ ] Program runs without errors

## 💾 Submission Guidelines

1. Create file: `atm_system.py`
2. Test thoroughly with multiple accounts
3. Test error cases (wrong password, insufficient balance)
4. Add comments explaining each section
5. Submit with sample output showing all features

## 🎯 Success Criteria

✅ Program runs without crashing  
✅ All 5 menu options work  
✅ Login validates correctly  
✅ Balance updates after transactions  
✅ Transaction history shows accurately  
✅ Code includes comments  
✅ Handles user errors gracefully  

---

**Estimated Time:** 4-6 hours  
**Difficulty:** Intermediate  
**Key Learning:** Integration of all Phase 2 concepts  

*Last Updated: December 2024*
