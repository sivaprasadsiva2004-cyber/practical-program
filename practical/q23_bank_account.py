# ============================================================
# Q23. Class BankAccount with deposit, withdraw,
#      and display methods.
# ============================================================

import datetime


class BankAccount:
    """
    Represents a simple bank account.

    Attributes:
        owner       (str)   : Account holder name
        account_no  (str)   : Unique account number
        balance     (float) : Current balance (private)
        transactions(list)  : History of all transactions
    """

    # Class variable – shared across all instances
    bank_name   = "PyBank Ltd."
    interest_rate = 0.04    # 4% annual

    def __init__(self, owner: str, account_no: str,
                 initial_deposit: float = 0.0):
        """Initialise account with owner details and optional deposit."""
        if initial_deposit < 0:
            raise ValueError("Initial deposit cannot be negative.")
        self.owner        = owner
        self.account_no   = account_no
        self.__balance    = initial_deposit   # private attribute
        self.transactions = []

        if initial_deposit > 0:
            self._record("OPEN / Initial Deposit", initial_deposit)

    # ── Private helper ────────────────────────────────────────
    def _record(self, txn_type: str, amount: float):
        """Append a transaction record to the history."""
        self.transactions.append({
            "type"   : txn_type,
            "amount" : amount,
            "balance": self.__balance,
            "time"   : datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        })

    # ── Public methods ────────────────────────────────────────
    def deposit(self, amount: float) -> float:
        """
        Deposit `amount` into the account.
        Returns new balance.
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.__balance += amount
        self._record("DEPOSIT", amount)
        print(f"  ✓ Deposited ₹{amount:,.2f}. New balance: ₹{self.__balance:,.2f}")
        return self.__balance

    def withdraw(self, amount: float) -> float:
        """
        Withdraw `amount` from the account.
        Raises InsufficientFundsError if balance is too low.
        Returns new balance.
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.__balance:
            raise ValueError(
                f"Insufficient funds. Available: ₹{self.__balance:,.2f}, "
                f"Requested: ₹{amount:,.2f}"
            )
        self.__balance -= amount
        self._record("WITHDRAWAL", amount)
        print(f"  ✓ Withdrew ₹{amount:,.2f}. New balance: ₹{self.__balance:,.2f}")
        return self.__balance

    def apply_interest(self):
        """Add annual interest to the account."""
        interest = self.__balance * BankAccount.interest_rate
        self.__balance += interest
        self._record("INTEREST", interest)
        print(f"  ✓ Interest applied: ₹{interest:,.2f}. "
              f"New balance: ₹{self.__balance:,.2f}")

    def get_balance(self) -> float:
        """Return current balance (read-only access to private attr)."""
        return self.__balance

    def display(self):
        """Print account summary and transaction history."""
        print("\n" + "=" * 55)
        print(f"  {BankAccount.bank_name}  –  Account Statement")
        print("─" * 55)
        print(f"  Account Holder : {self.owner}")
        print(f"  Account Number : {self.account_no}")
        print(f"  Current Balance: ₹{self.__balance:,.2f}")
        print(f"  Interest Rate  : {BankAccount.interest_rate * 100:.1f}% p.a.")
        print("─" * 55)
        print(f"  {'#':<4} {'Type':<25} {'Amount':>12} {'Balance':>12} {'Time'}")
        print("─" * 55)
        for i, txn in enumerate(self.transactions, 1):
            print(f"  {i:<4} {txn['type']:<25} "
                  f"₹{txn['amount']:>10,.2f} "
                  f"₹{txn['balance']:>10,.2f} "
                  f"{txn['time']}")
        print("=" * 55)

    def __str__(self):
        return (f"BankAccount(owner='{self.owner}', "
                f"acc='{self.account_no}', "
                f"balance=₹{self.__balance:,.2f})")

    def __repr__(self):
        return self.__str__()


# ── Demo ─────────────────────────────────────────────────────
if __name__ == "__main__":
    print("=" * 55)
    print("  BankAccount Class Demo")
    print("=" * 55)

    # Create account
    acc = BankAccount("Prayatn Sharma", "PB-2024-001", initial_deposit=5000.00)

    # Transactions
    acc.deposit(2000)
    acc.deposit(3500)
    acc.withdraw(1200)
    acc.apply_interest()

    try:
        acc.withdraw(50000)    # should fail
    except ValueError as e:
        print(f"  ✗ Error: {e}")

    # Display full statement
    acc.display()

    print(f"\n  str(acc) : {acc}")