using System;

namespace Accounts
{

    class BankAccount
    {
        protected double Balance;
        protected String AccountName;
        protected bool frozenStatus;

        public BankAccount(String name = "Unspecified", double balanceIn = 0, bool status = false) {
            Balance = balanceIn;
            AccountName = name;
            frozenStatus = status;
        }

        public double getBalance() {
            return Balance;
        }

        public String getName() {
            return AccountName;
        }

        public bool Status() {
            return frozenStatus;
        }

        public void Withdraw(double x) {
            if (!statusHandler(x))
            {
                Balance = Balance - x;
            }
            else {
                Console.WriteLine("You Are Attempting A Large Withdrawl. Account Frozen");
                Console.WriteLine("Please Contact A Branch Location");
            }
        }

        public void Deposit(double x) {
            if (!statusHandler(x)){
                Balance = Balance + x;
            }
            else
            {
                Console.WriteLine("You Are Attempting A Large Deposit. Account Frozen");
                Console.WriteLine("Please Contact A Branch Location");
            }
        }

        public void unfreeze() {
            frozenStatus = false;
        }

        protected bool statusHandler(double x) {
            if (x > (0.5 * Balance) || x > 2500) {//Currently all transations on an empty account freeze said account
                frozenStatus = true;
            }
            return frozenStatus;
        }

        //overload <<

    }
}
