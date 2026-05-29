CREATE OR REPLACE VIEW vw_pedidos_por_meio_pagamento AS
SELECT 
  meio_pagamento,
  SUM(pedido_meio_pagamento) AS pedido_meio_pagamento
FROM (
  SELECT
    CASE 
      WHEN forma_de_pagamento LIKE '%PIX%' THEN 'PIX'
      WHEN forma_de_pagamento LIKE '%Crédito%' THEN 'Crédito'
      WHEN forma_de_pagamento LIKE '%Débito%' THEN 'Débito'
      WHEN forma_de_pagamento LIKE '%App do Banco%' THEN 'App do Banco'
      WHEN forma_de_pagamento LIKE '%Dinheiro%' THEN 'Dinheiro'
      ELSE 'Outro'
    END AS meio_pagamento,
    COUNT(id_completo_do_pedido) AS pedido_meio_pagamento
  FROM pedidos_fatos
  GROUP BY forma_de_pagamento
) sub
GROUP BY meio_pagamento
ORDER BY pedido_meio_pagamento DESC;