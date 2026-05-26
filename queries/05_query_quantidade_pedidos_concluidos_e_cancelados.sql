DROP VIEW IF EXISTS vw_qntd_pedidos_concluidos_e_cancelados;

CREATE OR REPLACE VIEW vw_qntd_pedidos_concluidos_e_cancelados AS
SELECT nome_da_loja, 
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
COUNT(id_completo_do_pedido) FILTER(WHERE status_final_do_pedido = 'CONCLUIDO') AS quantidade_pedidos_concluidos,
COUNT(id_completo_do_pedido) FILTER(WHERE status_final_do_pedido = 'CANCELADO') AS quantidade_pedidos_cancelados
FROM pedidos_fatos
GROUP BY nome_da_loja, mes_pedido;