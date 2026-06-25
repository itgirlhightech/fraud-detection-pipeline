--total de transacoes por tipo (suspeito ou nao)

SELECT suspeita, AVG(Amount) as avg_amount, COUNT(*) as total_transactions
 from transactions GROUP BY suspeita

--transicoes com valor alto e suspeitas

SELECT * from transactions WHERE Amount > 1000 AND  suspeita = 1

-- top 10 maiores transacoes suspeitas 

SELECT * from transactions ORDER BY Amount DESC LIMIT 10

-- CTE: percentual de fraudes entre transacoes de valor alto

WITH high_value AS (
    SELECT * FROM transactions WHERE Amount > 1000
) 
SELECT
 (SELECT COUNT(*) FROM high_value WHERE suspeita = 1)
  * 100.0 / COUNT(*) as fraud_percentual
   FROM high_value