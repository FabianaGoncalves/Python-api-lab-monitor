create table usuario (
    id integer primary key autoincrement not null,
    nome varchar(200)  not null unique,
    senha varchar(14) not null unique
);

create table pc(
    patrimonio varchar(20) primary key not null,
    usuario varchar(200),
    ip varchar(18),
    mac varchar(18) unique,
    gateway varchar(18),
    sala varchar(300) not null,
    status varchar(10)
)
--delete from pc
--insert into pc values ('SGA123124','Fabiana','192.168.1.10','1c:39:47:5e:ab:42','192.168.1.1','Teste','True')
select * from pc;
update pc set status = 'True' where patrimonio = 'SGA242450';