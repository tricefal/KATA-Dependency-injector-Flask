from github import Github
from flask import url_for


def test_index(client, app, mocker):
	mock_github_client = mocker.Mock(spec=Github)
	mock_github_client.search_repositories.return_value = [
		mocker.Mock(
			html_url='repo1-url',
			name='repo1-name',
			owner=mocker.Mock(
				login='owner1-login',
				html_url="owner1-url",
				avatar_url="owner1-avatar-url",
			),
			get_commits=mocker.Mock(return_value=[mocker.Mock()]),
		),
		mocker.Mock(
			html_url='repo2-url',
			name='repo2-name',
			owner=mocker.Mock(
				login='owner2-login',
				html_url="owner2-url",
				avatar_url="owner2-avatar-url",
			),
			get_commits=mocker.Mock(return_value=[mocker.Mock()]),
		),
	]

	# overriding factory:
	with app.container.github_client.override(mock_github_client):
		response = client.get(url_for('index'))

	assert response.status_code == 200
	assert b'Results found: 2' in response.data

	assert b'repo1-url' in response.data
	assert b'repo1-name' in response.data
	assert b'owner1-login' in response.data
	assert b'owner1-url' in response.data
	assert b'owner1-avatar-url' in response.data

	assert b'repo2-url' in response.data
	assert b'repo2-name' in response.data
	assert b'owner2-login' in response.data
	assert b'owner2-url' in response.data
	assert b'owner2-avatar-url' in response.data


def test_index_no_results(client, app,mocker):
    github_client_mock = mocker.Mock(spec=Github)
    github_client_mock.search_repositories.return_value = []

    with app.container.github_client.override(github_client_mock):
        response = client.get(url_for('index'))

    assert response.status_code == 200
    assert b'Results found: 0' in response.data
