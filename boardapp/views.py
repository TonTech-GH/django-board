from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from . import models

def signupfunc(request):
    '''
    ユーザー登録画面
    '''
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            # ユーザー名の重複確認
            User.objects.get(username=username)
            print('****** objects type *****')
            print(type(User.objects))
            print('*************************')

            return render(request, 'signup.html', {'error': 'このユーザーは登録されています'})
        except:
            # 重複がなかったのでDBに登録する
            user = User.objects.create_user(username, '', password)
            print('****** registered *****')
            print(user.__dict__)
            print('***********************')
            return render(request, 'signup.html', {'some':100})

    return render(request, 'signup.html', {'some':100})

def loginfunc(request):
    '''
    ログイン画面
    '''
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # ユーザー名/パスワードの認証を行い、紐づくユーザー情報を持ってくる
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # ログインセッション生成
            login(request, user)
            return redirect('list')
        else:
            return render(request, 'login.html', {'error': 'ログインに失敗しました'})

    return render(request, 'login.html')

@login_required
def listfunc(request):
    '''
    記事のリスト表示画面
    '''
    object_list = models.BoardModel.objects.all()
    return render(request, 'list.html', {'objects': object_list})

def logoutfunc(request):
    '''
    ログアウト
    '''
    logout(request)
    return redirect('login')

@login_required
def detailfunc(request, pk):
    '''
    記事の詳細表示
    '''
    obj = models.BoardModel.objects.get(pk=pk)
    return render(request, 'detail.html', {'obj':obj})
