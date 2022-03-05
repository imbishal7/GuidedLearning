SELECT ARRAY_AGG(DISTINCT company) as valuestock
  FROM ( SELECT company, fiscal_year 
              , lead( fiscal_year,1) OVER( PARTITION BY company ORDER BY fiscal_year) fym1
              , lead( fiscal_year,2) OVER( PARTITION BY company ORDER BY fiscal_year) fym2               
           FROM dividend
       )csq
   WHERE fiscal_year/10000 = fym1/10000 - 1 
     AND fiscal_year/10000 = fym2/10000 - 2;