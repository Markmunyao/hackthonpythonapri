from django.shortcuts import render
import requests


def home(request):
  response = requests.get('https://api.github.com/users/markmunyao')
  data = response.json()
  result = data["bio"]

  response2 = requests.get('https://api.github.com/users/markmunyao')
  data2 = response2.json()
  result2 = data2["repos_url"]

  response3 = requests.get('https://api.github.com/users/markmunyao')
  data3 = response3.json()
  result3 = data3["location"]

  return render(request, 'templates/index.html', {
      'result': result,
      'result2': result2,
      'result3': result3
  })
