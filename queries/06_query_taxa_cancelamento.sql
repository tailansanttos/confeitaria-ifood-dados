DROP VIEW IF EXISTS vw_taxa_de_cancelamento;

CREATE OR REPLACE VIEW vw_taxa_de_cancelamento AS
SELECT 
    nome_da_loja,
    -- Removemos o ROUND e o * 100. Deixamos apenas a divisão pura.
    COUNT(id_completo_do_pedido) FILTER (WHERE status_final_do_pedido = 'CANCELADO')::NUMERIC 
    / COUNT(id_completo_do_pedido) AS percentual_pedidos_cancelados
FROM pedidos_fatos 
GROUP BY nome_da_loja;