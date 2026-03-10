SELECT category, AVG(stability_score) AS avg_stability
FROM cosmetic_rd_dataset
GROUP BY category
ORDER BY avg_stability DESC;

SELECT ingredient_name, cost_per_kg, final_score
FROM cosmetic_rd_dataset
ORDER BY final_score DESC;

SELECT category, AVG(final_score) AS avg_final_score
FROM cosmetic_rd_dataset
GROUP BY category;