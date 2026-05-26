
DROP VIEW IF EXISTS vw_ticket_medio_mes;
CREATE OR REPLACE VIEW vw_ticket_medio_mes AS
SELECT nome_da_loja,
EXTRACT(MONTH FROM data_pedido::DATE) AS numero_mes,
CASE EXTRACT(MONTH FROM data_pedido::DATE) 
WHEN 1 THEN 'Janeiro'
WHEN 2 THEN 'Fevereiro'
WHEN 3 THEN 'Março'
WHEN 4 THEN 'Abril'
WHEN 5 THEN 'Maio'
WHEN 6 THEN 'Junho'
WHEN 7 THEN 'Julho'
WHEN 8 THEN 'Agosto'
WHEN 9 THEN 'Setembro'
WHEN 10 THEN 'Outubro'
WHEN 11 THEN 'Novembro'
WHEN 12 THEN 'Dezembro'
END AS mes_pedido,
AVG(valor_liquido) AS ticket_medio_mes
FROM pedidos_fatos
GROUP BY nome_da_loja, numero_mes, mes_pedido;
