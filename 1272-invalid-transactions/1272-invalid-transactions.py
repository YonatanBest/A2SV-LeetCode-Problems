class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        already_done = set()
        invalid_transactions = []
        for i in range(len(transactions)):
            for j in range(len(transactions)):

                if i == j:
                    continue

                name_i, time_i, amount_i, city_i = transactions[i].split(",")
                name_j, time_j, amount_j, city_j = transactions[j].split(",")

                if name_i == name_j and abs(int(time_j) - int(time_i)) <= 60 and city_i != city_j:
                    if i not in already_done:
                        invalid_transactions.append(transactions[i])
                        already_done.add(i)
                    if j not in already_done:
                        invalid_transactions.append(transactions[j])
                        already_done.add(j)
                    continue
                
                if int(amount_i) > 1000 and i not in already_done:
                    invalid_transactions.append(transactions[i])
                    already_done.add(i)

                if int(amount_j) > 1000 and j not in already_done:
                    invalid_transactions.append(transactions[j])
                    already_done.add(j)

        return invalid_transactions