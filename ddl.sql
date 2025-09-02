PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS transactions;

CREATE TABLE transactions (
  order_id        INTEGER PRIMARY KEY,
  order_datetime  TEXT NOT NULL,
  customer_id     INTEGER NOT NULL,
  state           TEXT,
  city            TEXT,
  channel         TEXT,
  payment_method  TEXT,
  product_id      TEXT,
  category        TEXT,
  subcategory     TEXT,
  unit_price      REAL,
  quantity        INTEGER,
  discount_pct    REAL,
  net_revenue     REAL,
  cogs            REAL,
  profit          REAL,
  margin_pct      REAL,
  status          TEXT
);

-- Helpful view: month-level metrics
DROP VIEW IF EXISTS v_monthly_kpis;
CREATE VIEW v_monthly_kpis AS
SELECT
  strftime('%Y-%m', order_datetime) AS ym,
  SUM(net_revenue) AS revenue,
  SUM(profit) AS profit,
  AVG(margin_pct) AS avg_margin,
  COUNT(DISTINCT customer_id) AS customers,
  AVG(net_revenue) FILTER (WHERE status='Completed') AS avg_ticket
FROM transactions
GROUP BY ym;

-- Helpful view: category mix
DROP VIEW IF EXISTS v_category_mix;
CREATE VIEW v_category_mix AS
SELECT category,
       ROUND(SUM(net_revenue),2) AS revenue,
       ROUND(100.0 * SUM(net_revenue) / NULLIF((SELECT SUM(net_revenue) FROM transactions),0), 2) AS pct_of_total
FROM transactions
GROUP BY category
ORDER BY revenue DESC;
