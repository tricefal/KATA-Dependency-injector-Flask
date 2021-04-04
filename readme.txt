We will build a web application that helps to search for repositories on the Github. Let’s call it Github Navigator.

How does Github Navigator work?

    User opens a web page that asks to provide a search query.

    User types the query and hits Enter.

    Github Navigator takes that and searches through the Github for matching repositories.

    When search is done Github Navigator returns user a web page with the result.

    The results page shows all matching repositories and the provided search query.

    For any matching repository user sees:

            the repository name

            the owner of the repository

            the last commit to the repository

    User can click on the repository, the repository owner or the last commit to open its web page on the Github.


.
├── Pipfile
├── application.py
├── containers.py
├── views.py
├── requirements.txt
├── Makefile
├── readme.txt
├── git-rm.txt
├── Pipfile.lock
└── templates
    ├── base.html
    └── index.html
	