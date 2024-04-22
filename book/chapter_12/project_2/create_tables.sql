CREATE TABLE public.daily_adjusted
(
	price_date date,
	symbol varchar,
    daily_open double precision,
    daily_close double precision,
    daily_high double precision,
    daily_low double precision,
    daily_volume double precision
);

CREATE TABLE public.intraday_adjusted
(
    price_timestamp timestamp without time zone,
	symbol varchar,
    open_price double precision,
    close_price double precision,
    high double precision,
    low double precision,
    volume integer,
	ingestion_timestamp timestamp without time zone
)