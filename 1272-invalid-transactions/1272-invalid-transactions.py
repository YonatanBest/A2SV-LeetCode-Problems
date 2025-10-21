class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        invalid_transactions = set()
        for i in range(len(transactions)):
            for j in range(i + 1, len(transactions)):
                name_i, time_i, amount_i, city_i = transactions[i].split(",")
                name_j, time_j, amount_j, city_j = transactions[j].split(",")

                if name_i == name_j and abs(int(time_j) - int(time_i)) <= 60 and city_i != city_j:
                    invalid_transactions.add(i)
                    invalid_transactions.add(j)
                    continue
                
                if int(amount_i) > 1000:
                    invalid_transactions.add(i)

                if int(amount_j) > 1000:
                    invalid_transactions.add(j)

        return [transactions[i] for i in invalid_transactions]