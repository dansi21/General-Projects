//Version 1.0
//This driver designed only for basic fuctionality test

//This project is practice of polymorphism and inheritance

using System;


namespace Accounts
{
    class TestDriver
    {
        static void Main(string[] args)
        {
            BankAccount test1 = new BankAccount("William", 2000, false);
            BankAccount test2 = new Tier2Account("William", 2000, false);


            Console.ReadKey();
        }
    }
}
