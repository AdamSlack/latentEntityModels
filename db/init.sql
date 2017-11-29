
begin;
--
--  table of books and entity-term associations
--

create table books(
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


commit;
