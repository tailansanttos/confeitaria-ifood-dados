DROP VIEW IF EXISTS vw_quantidade_pedido_por_dia_da_semana;

CREATE OR REPLACE VIEW vw_quantidade_pedido_por_dia_da_semana AS 
SELECT nome_da_loja, 
CASE EXTRACT(DOW FROM data_pedido::DATE) 
WHEN 0 THEN 'Domingo'
WHEN 1 THEN 'Segunda-feira'
WHEN 2 THEN 'Terça-feira'
WHEN 3 THEN 'Quarta-feira'
WHEN 4 THEN 'Quinta-feira'
WHEN 5 THEN 'Sexta-feira'
WHEN 6 THEN 'Sábado'
END AS dia_pedido,
COUNT(id_completo_do_pedido) AS quantidade_pedido_dia_semana
FROM pedidos_fatos
GROUP BY nome_da_loja, dia_pedido
ORDER BY quantidade_pedido_dia_semana DESC;