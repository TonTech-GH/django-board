from django.shortcuts import render
from django.contrib.auth.models import User

def signupfunc(request):
    if request.method == 'POST':
        posted_username = request.POST['username']
        posted_password = request.POST['password']
        try:
            # ユーザー名の重複確認
            User.objects.get(username=posted_username)
            return render(request, 'signup.html', {'error': 'このユーザーは登録されています'})
        except:
            # 重複がなかったのでDBに登録する
            user = User.objects.create_user(posted_username, '', posted_password)
            print('****** registered *****')
            print(user.__dict__)
            print('***********************')
            return render(request, 'signup.html', {'some':100})

    return render(request, 'signup.html', {'some':100})