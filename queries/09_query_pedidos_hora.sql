DROP VIEW IF EXISTS vw_pedidos_hora;
CREATE OR REPLACE VIEW vw_pedidos_hora AS
SELECT nome_da_loja,
EXTRACT(HOUR FROM hora_pedido::time) AS hora_do_pedido,
COUNT(id_completo_do_pedido) AS quantidade_pedido
FROM pedidos_fatos
GROUP BY nome_da_loja, hora_do_pedido
ORDER BY quantidade_pedido DESC;