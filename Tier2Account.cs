using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Accounts
{
    class Tier2Account:BankAccount
    {
        protected override bool statusHandler(double x)
        {
            if (x > 25000)
            {
                frozenStatus = true;
            }
            return frozenStatus;
        }
    }
}
