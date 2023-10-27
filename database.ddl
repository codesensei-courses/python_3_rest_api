create table category
(
    id   INTEGER not null
        primary key,
    name VARCHAR not null
        unique
);

create table event
(
    id           INTEGER not null
        primary key,
    product_code VARCHAR not null
        unique,
    date         DATE    not null,
    price        NUMERIC not null,
    category_id  INTEGER not null
        references category
);
