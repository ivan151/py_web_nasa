nav_bar = """
<html>
<head>
	<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
	<title>{% block title %}{% endblock %}</title>
	</head>
	<body>
		<nav class="navbar navbar-dark bg-dark">
		  <a class="navbar-brand" href="#">SPACE</a>
		  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
		    <span class="navbar-toggler-icon"></span>
		  </button>
		  <div class="collapse navbar-collapse" id="navbarNav">
		    <ul class="navbar-nav">
		      <li class="nav-item active">
		        <a class="nav-link" href="/">Home <span class="sr-only">(current)</span></a>
		      </li>
		      <li class="nav-item">
		        <a class="nav-link" href="/login">Login</a>
		      </li>
          <li class="nav-item">
		        <a class="nav-link" href="/search">Поиск</a>
		      </li>
          <li class="nav-item">
		        <a class="nav-link" href="/apod">Обьект дня</a>
		      </li>
          <li class="nav-item">
		        <a class="nav-link" href="/earth">Земля</a>
		      </li>
		      <li class="nav-item">
		        <a class="nav-link" href="/logout">Logout</a>
		      </li>
		    </ul>
		  </div>
		</nav>
		{% block content %}
		{% endblock %}
		<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
		<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
		<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
	</body>
</html>
"""


def html_item(item):
    item_html = f"""<html>
<head>
	<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
	<title>Поиск картинок NASA</title>
	</head>
	<body>
	
<div class="container">
     <h1>{item.title}</h1>
    <div class="row">
        <div class="col-md-4">
            <div class="imgAbt">
                <img width="220" height="220" src={item.img} />
            </div>
        </div>
        <div class="col-md-8">
            <p>{item.desc}</p>
        </div>
    </div>
</div>
</body>
</html>"""
    return item_html
