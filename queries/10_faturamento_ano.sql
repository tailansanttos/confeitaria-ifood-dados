DROP VIEW IF EXISTS vw_faturamento_ano;

CREATE OR REPLACE VIEW vw_faturamento_ano AS

SELECT nome_da_loja, 
SUM(valor_liquido) AS faturamento_ano
FROM pedidos_fatos
GROUP BY nome_da_loja;