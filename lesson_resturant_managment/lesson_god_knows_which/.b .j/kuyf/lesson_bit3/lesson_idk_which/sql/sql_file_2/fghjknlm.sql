create table if not exists product(
    pro_id text primary key,
    pro_name text,
    pro_price text,
    pro_com text
;)


insert into product production(pro_id,pro_name,pro_price,pro_com)
VALUES
   
   ("101", "mother board","3200","15")
   ("102", "key board","450","16")
   ("103", "zip drive","250","14")
   ("104", "speacker","550","16")
   ("105", "monitor","800","11")
   ("106", "dvd drive","2600","12")
   ("107", "cd drive","350","12")
   ("108", "Printer","800","13")
   ("109", "Refill","3200","13")
   ("110", "Mouse","250","12");
   select pro_name,pro_price from
   from product
   wherepro_price =
   (select min(pro_price) from product);
   select pro_name, pro_price
   from product
   where pro_price =
   (select max(pro_price) from prpduct);

      

   