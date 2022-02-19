from pywebcopy import save_webpage

url = 'http://example.com'
download_folder = './test-results/'    

kwargs = {'bypass_robots': True, 'project_name': 'example'}

save_webpage(url, download_folder, **kwargs)