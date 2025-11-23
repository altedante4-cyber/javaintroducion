-- Consulta 1: Clientes con al menos un alquiler
-- El gerente de la tienda desea conocer qué clientes han realizado alquileres de películas, sin incluir a aquellos que no han alquilado nada.


select customer.customer_id  , customer.first_name , customer.last_name, count(rental.rental_id) as cantidad_alquileres 
from customer left join rental on customer.customer_id = rental.customer_id 
where store_id = 1 
group by customer.customer_id , customer.first_name , customer.last_name
order by cantidad_alquileres desc limit 10; 




-- Consulta 2: Todos los clientes y sus alquileres
-- El encargado de atención al cliente quiere un listado de todos los clientes registrados en el almacén 1 y el número de alquileres que han hecho, incluyendo clientes sin alquileres.


select customer.customer_id , customer.first_name , customer.last_name , count(rental.rental_id) as cantidad_alquileres from customer
left  join rental on customer.customer_id  = rental.customer_id 
where customer.store_id = 1  
group by customer.customer_id , customer.first_name , customer.last_name limit 10;


-- Consulta 3: Actores y sus películas
-- El gerente de casting necesita un reporte de los actores y las películas en las que han actuado. Además, quiere incluir actores que aún no han participado en ninguna película.


select  actor.actor_id , actor.first_name , actor.last_name , film.title from actor
left join film_actor on actor.actor_id = film_actor.actor_id 
left join film on  film_actor.film_id = film.film_id 
where actor.actor_id  between 1 and 10 
order by actor.actor_id , film.title asc ;










-- Consulta 4: Categorías y películas

-- El analista de inventario requiere un informe que muestre todas las categorías de películas junto con las películas asignadas a cada categoría. Es posible que existan categorías sin ninguna película asignada y (aunque en Sakila es poco común) películas sin categoría.

select category.category_id , category.name ,  film.title  from  category
left join film_category on category.category_id = film_category.category_id 
left join  film on film_category.film_id = film.film_id
where category.category_id = 1 
order by category.category_id , film.title asc limit 10 ;







-- Consulta 5: Películas y sus actores
-- El director de contenido quiere un listado de las películas y los actores que participan en cada una, pero incluyendo películas que aún no tengan actor asignado.

select film.film_id , film.title , actor.actor_id , actor.first_name , actor.last_name from
actor left join film_actor on actor.actor_id = film_actor.actor_id 
left join film on film_actor.film_id = film.film_id
where film.film_id = 1;

