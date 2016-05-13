# coding=utf-8
import Site
import Movie
Star_Wars_1 = Movie.Moovie("Star Wars I","La Menace fantôme","http://www.bedetheque.com/media/Couvertures/StarWarsEpisode1_23052002.jpg","https://www.youtube.com/watch?v=1BKYEL6WIRo")
Star_Wars_2 = Movie.Moovie("Star Wars II","L'Attaque des clones","https://upload.wikimedia.org/wikipedia/en/3/32/Star_Wars_-_Episode_II_Attack_of_the_Clones_(movie_poster).jpg","https://www.youtube.com/watch?v=gYbW1F_c9eM")
Star_Wars_3 = Movie.Moovie("Star Wars III","La Revanche des Sith","http://poster.vumoo.net/300/9805.jpg","https://www.youtube.com/watch?v=5UnjrG_N8hU")
Star_Wars_4 = Movie.Moovie("Star Wars IV","Un nouvel espoir","http://www.bedetheque.com/media/Couvertures/starwars04cof.jpg","https://www.youtube.com/watch?v=oH3TN6f3UCI")
Star_Wars_5 = Movie.Moovie("Star Wars V","L'Empire contre-attaque","http://vignette3.wikia.nocookie.net/starwars/images/c/cb/Ep5DVD.jpg/revision/latest?cb=20060430131933","https://www.youtube.com/watch?v=JNwNXF9Y6kY")
Star_Wars_6 = Movie.Moovie("Star Wars VI","Le Retour du Jedi","https://s-media-cache-ak0.pinimg.com/736x/6e/49/4a/6e494aff4209b0ffcbfc9d6eb5e2e356.jpg","https://www.youtube.com/watch?v=ncErY-o-UZY")
Star_Wars_7 = Movie.Moovie("Star Wars VII","Le Réveil de la Force","http://fr.web.img4.acsta.net/pictures/15/10/18/18/56/052074.jpg","https://www.youtube.com/watch?v=sGbxmsDFVnE")


Films = [Star_Wars_1,Star_Wars_2,Star_Wars_3,Star_Wars_4,Star_Wars_5,Star_Wars_6,Star_Wars_7]
Site.open_movies_page(Films)
