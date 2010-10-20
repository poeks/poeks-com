from helpers import *

def index(request):

	return render(
		'poeks/index.html', 
		request, 
		locals()
	)