# SMATrends

## Descrição

O **SMATrends** é uma ferramenta de pesquisa, revisão e análise de tendências que utiliza agentes inteligentes para coletar informações confiáveis da internet, revisar o conteúdo e gerar insights estratégicos. O fluxo do projeto é baseado em três agentes principais:

1. **Pesquisador** (`research`) – Busca informações detalhadas e confiáveis sobre um tema.
2. **Revisor** (`review`) – Analisa o conteúdo coletado, corrige e destaca os pontos mais relevantes.
3. **Coach de Tendências** (`trends`) – Gera insights estratégicos e recomendações a partir do conteúdo revisado.

O projeto roda localmente e utiliza a **OpenAI API** para processamento dos agentes.

## Como rodar

- Ter instalado python >=3.10 e <3.14
- Ter uma chave de API OpenAI
```bash
 pip install -r requirements.txt
 touch key.txt
 nano key.txt #escreva sua chave de api neste arquivo
 python main.py
 ```

- Digite o tema sobre o qual deseja pesquisar e aguarde a execução.

- O resultado será exibido no terminal após todas as tasks dos agentes serem concluídas.

- O resultado também será salvo no arquivo trends.md.
- Você pode alterar os contextos dos agentes e objetivo das tarefas conforme sua necessidade nos arquivos:
```bash
    ./crew/agents/agents_trends #agentes
    ./crew/tasks/task_trends #tarefas
```
- Contribuições para aprimorar o projeto são bem-vindas!
