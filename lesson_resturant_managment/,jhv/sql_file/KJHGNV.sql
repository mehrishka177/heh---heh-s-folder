CREATE TABLE Department (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(100) NOT NULL,
    manager_id INT
);

CREATE TABLE Employee (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(100) NOT NULL,
    salary DECIMAL(10,2) NOT NULL,
    department_id INT,
    FOREIGN KEY (department_id) REFERENCES Department(department_id)
);

SELECT department_id, COUNT(*) AS employee_count 
FROM Employee 
GROUP BY department_id;

SELECT department_id, SUM(salary) AS total_salary 
FROM Employee 
GROUP BY department_id;

SELECT department_id, COUNT(*) AS employee_count, SUM(salary) AS total_salary 
FROM Employee 
GROUP BY department_id;

SELECT d.department_id, SUM(e.salary) AS total_salary 
FROM Employee e 
JOIN Department d ON e.department_id = d.department_id 
WHERE d.manager_id = 103 
GROUP BY d.department_id;

SELECT department_id, COUNT(*) AS employee_count 
FROM Employee 
GROUP BY department_id 
HAVING COUNT(*) > 2;


 