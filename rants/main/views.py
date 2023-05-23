from django.shortcuts import render, redirect
from django.http import HttpResponse
from main.models import users, userRants, userFollowing
from .forms import registerUser, makeRant
from django.contrib.auth.models import User
import datetime

# Create your views here.

def index(response):
    return redirect('/home/')


def userPage(response, id):
    userInfo = response.user
    currentUserRants = userRants.objects.filter(username_id=id)
    users = User.objects.all()
    userRantsinDictionary = {}
    for user in users:
        userRantsinDictionary[user.username] = userRants.objects.filter(username_id=user.id).count()
    sortedUserRantsInDictionary = dict(sorted(userRantsinDictionary.items(), key=lambda x:x[1], reverse=True))
    return render(response, "main/userPage.html", {"userInfo":userInfo, "currentUserRants":currentUserRants, "userRantsinDictionary":sortedUserRantsInDictionary})

def home(response):
    userInfo = response.user
    rants = userRants.objects.all()
    users = User.objects.all()
    userRantsinDictionary = {}
    for user in users:
        userRantsinDictionary[user.username] = userRants.objects.filter(username_id=user.id).count()
    sortedUserRantsInDictionary = dict(sorted(userRantsinDictionary.items(), key=lambda x:x[1], reverse=True))
    print(response.POST)
    listOfFollowedUsers =  list(userFollowing.objects.filter(username=userInfo.id).values_list('followingList', flat=True))

    if response.method == "POST":
        if response.POST.get("rantTextArea"):
            inpRantDate = datetime.datetime.now()
            inpRantText = response.POST.get("rantTextArea").upper()
            if(len(inpRantText) > 0):
                t = userRants(username = response.user, rantText = inpRantText, rantDate = inpRantDate)
                t.save()
            return redirect('/home/')
        
        if response.POST.get('deleteRant'):
            rantToDelete = userRants.objects.get(id=response.POST.get('deleteRant'))
            rantToDelete.delete()
            return redirect('/home/')
        
        if response.POST.get('searchBar'):
            searchedQuery = response.POST.get('searchBar')
            searchedQueryIDs = list(User.objects.filter(username__contains=searchedQuery).values_list('id', flat=True))
            searchQueryRantsMatchingUsername = []
            for user in searchedQueryIDs:
                searchQueryRantsMatchingUsername.append(list(userRants.objects.filter(username_id=user)))
            searchQueryRantsMatchingUsername = [item for sublist in searchQueryRantsMatchingUsername for item in sublist]

            searchedQueryRants = list(userRants.objects.filter(rantText__contains=searchedQuery))
            searchQueryUsersAndRants = list(set(searchQueryRantsMatchingUsername + searchedQueryRants))

            return render(response, "main/home.html", {"userInfo":userInfo, "userRants":rants, "userRantsinDictionary":sortedUserRantsInDictionary, "users":users, "searchedRants":searchQueryUsersAndRants})
        
        if response.POST.get("followUser"):
            userToFollowID = int(response.POST.get("followUser"))
            if userToFollowID not in listOfFollowedUsers:
                print("we are here?")
                t = userFollowing(username = userInfo, followingList = User.objects.get(id=userToFollowID))
                t.save()
                return redirect('/home/')
            
        if response.POST.get("unfollowUser"):
            userToUnfollowID = int(response.POST.get("unfollowUser"))
            if userToUnfollowID in listOfFollowedUsers:
                t = userFollowing.objects.get(username = userInfo.id, followingList = userToUnfollowID)
                t.delete()
                return redirect('/home/')



    return render(response, "main/home.html", {"userInfo":userInfo, "userRants":rants, "userRantsinDictionary":sortedUserRantsInDictionary, "users":users, "listOfFollowedUsers":listOfFollowedUsers})