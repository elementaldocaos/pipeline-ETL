# Pipeline ETL com IA Generativa

## Gerenciando as tarefas dos projeto:
O tempo estimado para concluir o projeto pode variar dependendo da sua experiência em programação, familiaridade com as ferramentas e bibliotecas envolvidas, e a complexidade das mensagens geradas. No entanto, posso fornecer uma estimativa aproximada com base nas etapas descritas:

1. **Preparação Inicial e Preparação de Dados**:
   - Essas etapas geralmente não consomem muito tempo. Pode levar cerca de 30 minutos a 1 hora para garantir que seu ambiente de desenvolvimento esteja configurado corretamente e que você tenha o arquivo CSV com os IDs de usuário.

2. **Consumindo a API da Santander Dev Week 2023**:
   - O tempo para consumir a API e obter os dados dos clientes pode variar com base na eficiência da sua implementação. Dependendo do número de IDs de usuário e da taxa de solicitação, isso pode levar algumas horas.

3. **Utilizando a API do ChatGPT (OpenAI)**:
   - O tempo para gerar mensagens personalizadas depende da complexidade das mensagens e do número de clientes. Isso pode levar algumas horas, especialmente se você estiver gerando muitas mensagens.

4. **Atualizando os Dados dos Clientes**:
   - Atualizar os dados na API da Santander também pode variar em tempo, dependendo do número de clientes e da eficiência da implementação. Isso pode levar algumas horas.

5. **Revisão e Entrega**:
   - A revisão final e a garantia de que tudo funcione corretamente podem levar cerca de 1 a 2 horas, dependendo da quantidade de testes e verificações necessários.

6. **Entrega Final**:
   - O tempo para preparar a documentação e entregar o projeto geralmente não é muito longo, cerca de 1 a 2 horas.

Com base nessas estimativas, o projeto completo pode levar de aproximadamente 5 a 10 horas para ser concluído. Lembre-se de que essas são estimativas aproximadas e podem variar dependendo das circunstâncias específicas. É sempre bom reservar algum tempo extra para garantir que tudo esteja funcionando perfeitamente e para acomodar eventuais desafios imprevistos.

Se você estiver com prazos apertados ou preocupado com o tempo, é importante planejar e priorizar as etapas do projeto de acordo com sua disponibilidade e urgência.

## Instruções 
**Passo 1: Preparação Inicial**

- Certifique-se de ter o ambiente de desenvolvimento configurado e o repositório "santander-edv-week-2023" clonado no seu ambiente.

**Passo 2: Preparação de Dados**

- Você já possui o arquivo "SDW2023.csv" com a lista de IDs de usuário. Certifique-se de que ele está disponível no diretório apropriado.

**Passo 3: Consumindo a API da Santander Dev Week 2023 (Swagger)**

- Acesse a Swagger da API usando o link fornecido: [Swagger API](https://sdw-2023-prd.up.railway.app/swagger-ui.html).
- Utilize uma biblioteca em Python, como `requests`, para fazer solicitações GET à API da Santander Dev Week 2023 (endpoint `https://sdw-2023-prd.up.railway.app/users/{id}`) para obter os dados de cada cliente.
- Itere sobre os IDs de usuário da lista do CSV e, para cada ID, faça uma solicitação GET para obter os dados do cliente correspondente.

**Passo 4: Utilizando a API do ChatGPT (OpenAI)**

- Use a API do ChatGPT (OpenAI) para gerar mensagens de marketing personalizadas para cada cliente. Certifique-se de que os clientes recebam mensagens que enfatizam a importância dos investimentos.

**Passo 5: Atualizando os Dados dos Clientes**

- Utilize a biblioteca `requests` novamente para fazer solicitações PUT à API da Santander Dev Week 2023 (endpoint `https://sdw-2023-prd.up.railway.app/users/{id}`) para atualizar as informações de "news" de cada cliente com as mensagens geradas.

**Passo 6: Revisão e Entrega**

- Após concluir os passos anteriores, verifique se todas as mensagens foram geradas e atualizadas com sucesso na API da Santander Dev Week 2023.
- Realize uma revisão final do código e dos dados para garantir que tudo esteja em ordem.

**Passo 7: Entrega Final**

- Prepare uma documentação ou relatório resumido que descreva o que você fez no projeto, incluindo quaisquer desafios enfrentados e soluções encontradas.
- Entregue o projeto conforme as instruções fornecidas pela equipe do Santander.

Certifique-se de documentar todas as etapas do projeto, incluindo o uso da Swagger da API para futura referência. Se surgirem dúvidas durante o processo, sinta-se à vontade para pedir assistência. Boa sorte na conclusão do projeto!