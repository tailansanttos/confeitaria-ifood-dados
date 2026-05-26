CREATE OR REPLACE VIEW vw_pedidos_por_turno AS
SELECT nome_da_loja, turno,
COUNT(id_completo_do_pedido) AS pedido_turno
FROM pedidos_fatos
GROUP BY nome_da_loja, turno;