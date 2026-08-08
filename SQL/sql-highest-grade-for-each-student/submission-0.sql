-- Write your query below
WITH ranks AS(SELECT student_id,exam_id,score,
ROW_NUMBER() OVER(PARTITION BY student_id ORDER BY score DESC,exam_id ASC) as score_max
FROM exam_results)
SELECT student_id,exam_id,score FROM ranks WHERE score_max=1;
