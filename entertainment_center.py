# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define instances of the class Movie defined
# in media.py. After you follow along with Kunal, make some instances
# of your own!

# After you run this code, open the file fresh_tomatoes.html to
# see your webpage!
#it is good practise to make your class in one file and to use/call it in another file

# https://www.udacity.com/course/viewer#!/c-nd000/l-4185678656/e-991358856/m-1013629064
#import media to tell my prgramm that i want to use the content of the media.py file
import media
import fresh_tomatoes

#media is the name of the other py file and Movie is the name of the class defined in that file
#"module" est la mm chose que "filename"
toy_story = media.Movie("Toy story", 
						"A story of a boy and his toys that come to life",
						"http://img.lum.dolimg.com/v1/images/open-uri20150422-20810-m8zzyx_5670999f.jpeg?region=0,0,300,450",
						"https://www.youtube.com/watch?v=KYz2wyBy3kc")

#print toy_story.storyline 

avatar = media.Movie("Avatar",
					"A marine on an alien planet",
					"http://t0.gstatic.com/images?q=tbn:ANd9GcQCfmvrE4fMo2cd8esc7mDZPtFSJThAujddMPkRtti1_ij6u-jp",
					"https://www.youtube.com/watch?v=LPk3n5Om28o")
#print avatar.storyline
#avatar.show_trailer()

gomorra = media.Movie("Gomorra la serie", "the story of the mafia in naples", "http://i.f1g.fr/media/figaro/805x453_crop/2015/09/29/XVM4624d3a4-66d4-11e5-9a21-23daa8ae8265.jpg", "https://www.youtube.com/watch?v=FsMnW43n3AI")
#gomorra.show_trailer()

quaidesorfevres = media.Movie("36 quai des orfevres", "the story of top police men turning dark", "http://fr.web.img3.acsta.net/medias/nmedia/18/35/42/86/18395118.jpg", "https://www.youtube.com/watch?v=nlTAUiRHP9U")

persepolis = media.Movie("persepolis", "the story of the iranian revolution from the point of view of a young girl", "http://images.google.fr/imgres?imgurl=http://fr.web.img6.acsta.net/medias/nmedia/18/63/80/43/18761581.jpg&imgrefurl=http://www.allocine.fr/film/fichefilm_gen_cfilm%3D110204.html&h=800&w=600&tbnid=eqwsaiRm_qiNCM:&tbnh=186&tbnw=139&docid=0ilSiuzFidzkuM&itg=1&usg=__Vn1ewEhNvn2-3WDxo7yWMmbFXO0=", "https://www.youtube.com/watch?v=3PXHeKuBzPY")

#movies = [toy_story, avatar]
#fresh_tomatoes.open_movies_page(movies)

movies = [toy_story, avatar, gomorra, quaidesorfevres, persepolis]
fresh_tomatoes.open_movies_page(movies)