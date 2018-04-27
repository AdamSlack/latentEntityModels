
begin;
--
--  table of books and entity-term associations
--

create table books( -- Actually book_entity_terms
    id         serial   not null,
    book_title text     not null,
    entity     text     not null,
    term       text     not null,
    strength   float    not null,
    primary key(book_title, entity, term)
);


create table topics(
    topic_id    int     not null,
    term        text    not null,
    strength    float   not null,
    primary key(topic_id, term)
);

create table book_topics(
    id          serial  not null,
    book_title  text    not null,
    topic_id    int     not null,
    score       float   not null,
    primary key(book_title, topic_id)
);

drop materialized view if exists book_titles;
create materialized view book_titles as
    select distinct book_title from books;

create table book_entity_topics(
    entity     text not null ,
    book_title text not null ,
    topic_id   serial not null,
    strength   float not null,
    primary key(entity, book_title, topic_id)
);

create table latent_entities(
    entity_id    serial  not null,
    topic_id     serial  not null ,
    score        float   not null,    
    primary key(entity_id, topic_id)
);

create table latent_entity_entities(
    entity_id   serial not null,
    entity      text   not null,
    euclid_dist float,
    primary key (entity_id, entity)
);


commit;

-- create index book_idx on books(book_title, entity);
-- create index topics on topics(term);
-- create index entity_topic_idx on book_entity_topics(book_title, entity);
