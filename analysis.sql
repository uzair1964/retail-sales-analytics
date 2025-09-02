-- 1) Monthly revenue & profit trend
SELECT strftime('%Y-%m', order_datetime) AS ym,
       ROUND(SUM(net_revenue),2) AS revenue,
       ROUND(SUM(profit),2) AS profit
FROM transactions
WHERE status='Completed'
GROUP BY ym
ORDER BY ym;

-- 2) Top 10 products by revenue
SELECT product_id,
       ROUND(SUM(net_revenue),2) AS revenue
FROM transactions
GROUP BY product_id
ORDER BY revenue DESC
LIMIT 10;

-- 3) Category share of revenue
SELECT category,
       ROUND(SUM(net_revenue),2) AS revenue,
       ROUND(100.0*SUM(net_revenue)/NULLIF((SELECT SUM(net_revenue) FROM transactions),0),2) AS pct_total
FROM transactions
GROUP BY category
ORDER BY revenue DESC;

-- 4) City x Channel performance (Top 10 city-channel pairs)
SELECT city, channel,
       ROUND(SUM(net_revenue),2) AS revenue,
       ROUND(AVG(margin_pct),4) AS avg_margin
FROM transactions
GROUP BY city, channel
ORDER BY revenue DESC
LIMIT 10;

-- 5) AOV (average order value), Units/Order
SELECT
  ROUND(AVG(net_revenue),2) AS aov,
  ROUND(AVG(quantity),2) AS units_per_order
FROM transactions
WHERE status='Completed';

-- 6) Returns/Cancel rate
SELECT
  ROUND(100.0*SUM(CASE WHEN status='Returned' THEN 1 ELSE 0 END)/COUNT(*),2) AS return_rate_pct,
  ROUND(100.0*SUM(CASE WHEN status='Cancelled' THEN 1 ELSE 0 END)/COUNT(*),2) AS cancel_rate_pct
FROM transactions;
