# sys is a module. It lets us access command line arguments
# which are stored in sys.argv

import sys

if len(sys.argv) < 2:
    print("Please supply the total, without a leading '$'")
    exit(1)

total = float(sys.argv[1])

for tip_amount in [.1, .15, .2]:
    tip = tip_amount * total
    print("%.1f percent: tip $%.2f, total is $%.2f"%(tip_amount*100,tip, tip+total))
