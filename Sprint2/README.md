# Conteúdos da Sprint 2

## SQL para Análise de Dados: Do básico ao avançado 


### Data & Analytics - PB - AWS 2/10 Exercícios práticos

**Exercício 1**
```SQL
select *
from livro
where publicacao > '2014-12-31'
order by cod
```

**Exercício 2**
```SQL
select titulo,valor
from livro
order by valor desc
limit 10 
```

**Exercício 3**
```SQL
select count(livro.cod) as quantidade, editora.nome, endereco.estado, endereco.cidade
from editora 
    inner join livro  on livro.editora = editora.codeditora
    inner join endereco on editora.endereco = endereco.codendereco
group by editora.nome
order by quantidade desc
limit 5
```

**Exercício 4**
```SQL
select autor.nome,autor.codautor, autor.nascimento,count(livro.cod) as quantidade
from autor 
    left join livro  on livro.autor = autor.codautor
group by autor.nome
order by autor.nome
```

**Exercício 5**
```SQL
select distinct autor.nome
from autor 
    left join livro on autor.codautor = livro.autor
    left join editora on livro.editora = editora.codeditora 
    left join endereco on endereco.codendereco = editora.endereco
where endereco.estado not in ('RIO GRANDE DO SUL','PARANÁ')
order by autor.nome
```

**Exercício 6**
```SQL
select autor.codautor, autor.nome, count(livro.autor) as quantidade_publicacoes
from autor
    left join livro on autor.codautor = livro.autor
group by livro.autor
order by quantidade_publicacoes desc
limit 1
```

**Exercício 7**
```SQL
select autor.nome
from autor
    left join livro on autor.codautor = livro.autor
where livro.publicacao is null
```

**Exercício 8**
```SQL
select tbvendedor.cdvdd, tbvendedor.nmvdd
from tbvendedor 
    left join tbvendas on tbvendedor.cdvdd = tbvendas.cdvdd
where tbvendas.status = 'Concluído' 
limit 1
```
**Exercício 9**
```SQL
select tbvendas.cdpro, tbvendas.nmpro
from tbvendas 
    left join tbestoqueproduto on tbvendas.cdpro = tbvendas.cdpro
where (tbvendas.status = 'Concluído') and dtven >= '2014-02-03' and dtven <= '2018-02-02'  
limit 1   
```
**Exercício 10**
```SQL
select tbvendedor.nmvdd as vendedor, sum (tbvendas.vrunt * tbvendas.qtd) as valor_total_vendas, round(sum (tbvendas.vrunt * tbvendas.qtd) * tbvendedor.perccomissao /100,2) as comissao 
from tbvendedor 
    left join  tbvendas on tbvendedor.cdvdd = tbvendas.cdvdd
where tbvendas.status = 'Concluído'    
group by tbvendedor.nmvdd, tbvendedor.perccomissao   
order by comissao desc 
```

**Exercício 11**
```SQL
select cdcli,nmcli, sum(qtd*vrunt) as gasto
from tbvendas
where status = 'Concluído' 
group by nmcli
order by gasto desc
limit 1
```

**Exercício 12**
```SQL
select tbdependente.cddep,tbdependente.nmdep,tbdependente.dtnasc, sum(tbvendas.qtd * tbvendas.vrunt) as valor_total_vendas
from tbvendas 
    left join tbdependente on tbdependente.cdvdd = tbvendas.cdvdd 
    left join tbvendedor on tbvendas.cdvdd = tbvendedor.cdvdd
where status = 'Concluído' 
group by tbdependente.nmdep
order by valor_total_vendas
limit 1
```
**Exercício 13**
```SQL
select cdpro, nmcanalvendas,nmpro, sum(qtd)as quantidade_vendas
from tbvendas
where status = 'Concluído' 
group by nmcanalvendas, cdpro
order by quantidade_vendas 
limit 10
```
**Exercício 14**
```SQL
select estado, Round (avg(qtd*vrunt),2)as gastomedio 
from tbvendas
where status = 'Concluído' 
group by estado
order by gastomedio desc
```

**Exercício 15**
```SQL

select cdven
from tbvendas
where deletado = '1'
order by cdven
```
**Exercício 16**
```SQL
select estado, nmpro, Round (avg(qtd),4)as quantidade_media 
from tbvendas
where status = 'Concluído'
group by estado , nmpro 
order by estado , nmpro
```