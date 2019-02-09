Select 
    id,
    movie,
    description,
    rating
From cinema
Where id % 2 = 1
And description != 'boring'
order by rating desc
