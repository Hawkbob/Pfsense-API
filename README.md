# pfSense-API
Se você é daqueles que cria bastante regras no pfSense, e depois precisa remove-las,<br> 
aqui está uma solução simples e que funciona perfeitamente para regras temporarias,<br>
que as vezes você cria e acaba esquecendo de remover.<br>
Não apenas isso, mas é possível gerenciar diversas outras coisas no Pfsense.

## Documentação da API
A documentação da API fica no repositório:
[Jared Hendrickson](https://github.com/jaredhendrickson13/pfsense-api)<br>
e vamos usa-la para nossa automação.<br>
Siga os passos para instalação dessa API diretamente no pfSense, para<br>
depois continuar aqui com a automação.

## Consumindo a API (Automação)
Vou dar o exemplo do meu caso, e você pode aplicar pro seu contexto.<br>
Todos os dias, criava regras de abrir rotas no pfSense, o problema<br>
é que se você esquece essas regras no pfSense, rotas abertas, etc<br>
isso pode abrir uma brecha na segurança da sua infraestrutura.<br>

Então o ideal, era que essas regras fossem removidas no final do dia<br>
Criei um script em Python, ele faz a chamada na API para remover essas<br>
regras, e aplicar as alterações feitas. Você pode usa-lo, é o arquivo<br>
rule.py

## Como funciona? (Logica)
Toda regra tem o campo "Descrição" e você pode por qualquer nome ali<br>
para identificar a regra. Podemos colocar 'tmp' (temporaria) apenas para<br>
que o nosso script chame a API e encontre essas regras com descrição 'tmp'

A Chamada de API funciona da seguinte forma:<br>
Você pode filtrar as regras diretamente no link, exemplo;<br><br>
***/api/v2/firewall/rules?if=openvpn&descr=tmp***

- if=openvpn | é o Nome da interface de rede no pfSense
- dscr=tmp | pega as regras que tem a palavra tmp na descrição

Agora é só fazer a chamada API usando método DELETE<br>
Você pode usar o curl para ir testando antes de usar o script<br>
Altere o Script conforme estiver configurado os nomes no seu pfSense.

## Deixando automatico
Você pode usar o Cron do Linux para agendar uma tarefa de execução<br>
desse script personalizada nos dias e horas que você quiser.

⚠️ **Crie um ambiente de teste antes de aplicar em produção.** 


