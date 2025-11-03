-- 코드를 작성해주세요
select b.id, b.length
    from (select id, length, ROW_NUMBER() OVER (ORDER BY length desc, id) AS rown
            from fish_info) b
    where rown <= 10;

