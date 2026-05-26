-- 1. Apaga a view se ela existir para evitar conflitos
DROP VIEW IF EXISTS vw_receita_liquida_dia;

-- 2. Recria a view com o comando correto
CREATE OR REPLACE VIEW vw_receita_liquida_dia AS
SELECT 
    nome_da_loja, 
    SUM(valor_liquido) AS total_liquido_dia,

    EXTRACT(DOW FROM data_pedido::DATE) AS numero_dia,
    
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
GROUP BY nome_da_loja, numero_dia, dia_pedido
ORDER BY numero_dia ASC;