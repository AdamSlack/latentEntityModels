
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



commit;