import random

def determine_winnings(result):
    if result <= (1/292201338):
        return "jackpot"
    elif result <= (1/11688054):
        return 1000000
    elif result <= (1/913129):
        return 50000
    elif (result <= (1/36525)) or (result <= (1/14494)):
        return 100
    elif (result <= (1/580)) or (result <= (1/701)):
        return 7
    elif (result <= (1/92)) or (result <= (1/38)):
        return 4
    else:
        return 0

def run_lifetime(seed_num):
    random.seed(seed_num)
    bank = 0
    jackpot = False
    runs = 0
    how_many = 3 * 52 * 30 # 3 times a week X 52 weeks X 30 years
    # print("will run", how_many)
    while not jackpot:
        bank -= 2
        runs += 1
        prob = random.random()
        result = determine_winnings(prob)
        if result == "jackpot":
            jackpot = True
            return "jackpot"
        elif result > 0:
            bank += result
        if runs == how_many:
            # print("final result", bank)
            break
    return bank

# print(run_lifetime(42))
# print(run_lifetime(43))
# print(run_lifetime(1000))


print(run_lifetime(34525))
# try_a_bunch = [run_lifetime(i) for i in range(50000)]
# print("of 50,000 people trying for 30 years...")
# print(sum([bank > 0 for bank in try_a_bunch if bank != "jackpot"]), "made profit")
# print("jackpots:", try_a_bunch.count("jackpot"))
