-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/d/uVlm60
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE "population_table" (
    ID_State VARCHAR   NOT NULL,
    State VARCHAR   NOT NULL,
    ID_Year DATE   NOT NULL,
    Year DATE   NOT NULL,
    Population Integer   NOT NULL,
    Slug_State VARCHAR   NOT NULL
);

