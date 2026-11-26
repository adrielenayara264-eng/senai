TechFlow Core – Engenharia de Requisitos

1\. Introdução



O TechFlow Core é um sistema de gerenciamento de demandas que permite cadastrar, listar, buscar, atualizar e excluir demandas, além de consultar informações de CEP e cotações.



Este documento apresenta os requisitos funcionais e não funcionais do sistema.



2\. Requisitos Funcionais (RF)

RF01 – Cadastrar demanda



O sistema deve permitir cadastrar uma nova demanda, informando título, descrição e responsável.



RF02 – Listar demandas



O sistema deve permitir visualizar todas as demandas cadastradas.



RF03 – Buscar demanda



O sistema deve permitir pesquisar uma demanda pelo seu identificador ou título.



RF04 – Atualizar status



O sistema deve permitir alterar o status de uma demanda para Pendente, Em andamento ou Concluída.



RF05 – Excluir demanda



O sistema deve permitir excluir uma demanda, solicitando confirmação antes da exclusão.



RF06 – Consultar CEP



O sistema deve permitir consultar informações de endereço por meio de um CEP, utilizando uma API externa.



RF07 – Consultar cotação



O sistema deve permitir consultar cotações de moedas utilizando uma API externa.



3\. Requisitos Não Funcionais (RNF)

RNF01 – Segurança



O sistema deve validar os dados informados e impedir acessos não autorizados às funcionalidades protegidas.



RNF02 – Integridade



O sistema deve garantir que os dados cadastrados sejam consistentes e evitar registros incompletos ou inválidos.



RNF03 – Usabilidade



O sistema deve possuir uma interface simples, organizada e intuitiva.



RNF04 – Desempenho



O sistema deve responder às operações comuns em até 3 segundos, em condições normais de funcionamento.



RNF05 – Confiabilidade



O sistema deve tratar erros durante as operações e apresentar mensagens claras ao usuário, evitando perda de dados.



4\. Considerações finais



Os requisitos apresentados neste documento definem o escopo inicial do TechFlow Core e servirão como referência para as próximas etapas de desenvolvimento e testes.

