TechFlow Core – Parecer Técnico de Arquitetura

1\. Comparação entre arquiteturas



As aplicações Console/CLI funcionam por meio de comandos digitados no terminal. São leves, possuem implementação simples e consomem poucos recursos do computador. As aplicações Web funcionam por meio de navegadores e permitem acesso por diferentes dispositivos, mas geralmente exigem uma estrutura de servidor e maior configuração. Já as aplicações Desktop possuem interfaces gráficas com janelas, botões e menus, oferecendo interação visual, porém podem exigir mais recursos e cuidados com instalação e compatibilidade.



2\. Justificativa da escolha do Python CLI



A escolha do Python em modo CLI para o TechFlow Core é adequada porque o projeto possui funcionalidades de gerenciamento de demandas, como cadastrar, listar, buscar, atualizar status e excluir registros. Essas operações podem ser realizadas por meio de menus e comandos no terminal, sem a necessidade de desenvolver uma interface gráfica complexa. Além disso, o Python possui uma sintaxe simples e permite organizar o código de maneira clara.



3\. Defesa técnica da arquitetura



O Python CLI atende aos requisitos iniciais do TechFlow Core porque permite desenvolver e testar as funcionalidades de forma rápida, utilizando poucos recursos computacionais e sem exigir uma infraestrutura de servidor. Também permite integrar serviços externos para consultas de CEP e cotações por meio de APIs. Dessa forma, a arquitetura escolhida oferece simplicidade, baixo custo de implementação e facilidade de manutenção, sendo adequada ao escopo atual do projeto.



4\. Conclusão



Com base na comparação realizada, a arquitetura Console/CLI utilizando Python foi escolhida por atender às necessidades atuais do TechFlow Core, oferecendo simplicidade, eficiência e facilidade de desenvolvimento.

