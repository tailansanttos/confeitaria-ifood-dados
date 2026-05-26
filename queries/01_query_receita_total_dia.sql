
DROP VIEW IF EXISTS vw_receita_liquida_dia;
CREATE  OR REPLACE VIEW vw_receita_liquida_dia AS 
SELECT nome_da_loja, 
SUM(valor_liquido) AS total_liquido_dia,
CASE EXTRACT(DOW FROM data_pedido::DATE) 
WHEN 0 THEN 'Domingo'
WHEN 1 THEN 'Segunda-Feira'
WHEN 2 THEN 'Terça-Feira'
WHEN 3 THEN 'Quarta-Feira'
WHEN 4 THEN 'Quinta-feira'
WHEN 5 THEN 'Sexta-feira'
WHEN 6 THEN 'Sábado'
END AS dia_pedido 
FROM pedidos_fatos 
GROUP BY nome_da_loja, dia_pedido
ORDER BY SUM(valor_liquido) DESC;