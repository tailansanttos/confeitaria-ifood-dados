CREATE OR REPLACE VIEW vw_pedidos_por_meio_pagamento AS
SELECT nome_da_loja, forma_de_pagamento,
COUNT(id_completo_do_pedido) AS pedido_meio_pagamento
FROM pedidos_fatos
GROUP BY nome_da_loja, forma_de_pagamento
ORDER BY pedido_meio_pagamento DESC;