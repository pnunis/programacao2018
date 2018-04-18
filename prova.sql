-- Database: ifrn

-- DROP DATABASE ifrn;

CREATE DATABASE ifrn
  WITH OWNER = postgres
       ENCODING = 'UTF8'
       TABLESPACE = pg_default
       LC_COLLATE = 'pt_BR.UTF-8'
       LC_CTYPE = 'pt_BR.UTF-8'
       CONNECTION LIMIT = -1;

-- Table: public.docente

-- DROP TABLE public.docente;

CREATE TABLE public.docente
(
  id integer NOT NULL DEFAULT nextval('aluno_id_seq'::regclass),
  matricula text,
  ndisciplina text,
  nota1 text,
  nota2 text,
  CONSTRAINT docente_pkey PRIMARY KEY (id)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public.docente
  OWNER TO postgres;

