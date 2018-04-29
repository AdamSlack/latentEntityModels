
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


-- Godsend, super simple way of doing it!
-- https://stackoverflow.com/questions/34272482/postgresql-create-function-euclidean-distance-n-dimensions
CREATE OR REPLACE FUNCTION distance(l real[], r real[]) RETURNS real AS $$
DECLARE
  s real;
BEGIN
  s := 0;
  FOR i IN 1..4 LOOP
    s := s + ((l[i] - r[i]) * (l[i] - r[i]));
  END LOOP;
  RETURN |/ s;
END;
$$ LANGUAGE plpgsql;

-- EXAMPLE USAGE
-- select distance(str_array::real[], ARRAY[0,0,0,0,0,0,0,0,0,0]), entity, book_title
--   from ( 
--      select array_agg(strength) as str_array, entity, book_title
--        from book_entity_topics group by entity, book_title
--   ) as a;
