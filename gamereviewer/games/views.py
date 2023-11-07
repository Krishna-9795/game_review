
from .models import Game, Review, Comment
from .serializers import GameSerializer, ReviewSerializer, CommentSerializer
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response


@api_view(['POST'])
def create_game(request):
    if request.method == 'POST':
        serializer = GameSerializer(data=request.data)

        if serializer.is_valid():
            # Create and save the game instance to the database
            game = serializer.save()
            return Response(GameSerializer(game).data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET'])
def game_list(request):
    if request.method=='GET':
        games=Game.objects.all()
        serializer=GameSerializer(games,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def game_detail(request, pk):
    game = get_object_or_404(Game, pk=pk)

    if request.method == 'GET':
        serializer = GameSerializer(game)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = GameSerializer(game, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        game.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
# CRUD for reviews table
@api_view(['POST'])
def create_review(request):
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def review_list(request):
    reviews = Review.objects.all()
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET', 'PUT', 'DELETE'])
def review_detail(request, pk):
    review = get_object_or_404(Review, pk=pk)

    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def create_comment(request):
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def comment_list(request):
    comments = Comment.objects.all()
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)







""""
from django.http import HttpResponse
from rest_framework import generics
from django.shortcuts import get_object_or_404, render

class ReviewList(generics.ListCreateAPIView):
    queryset = Review.objects.filter(approved=True)
    serializer_class = ReviewSerializer
    def get_queryset(self):
        game_id = self.kwargs['game_id']
        game = get_object_or_404(Game, pk=game_id)
        return Review.objects.filter(game=game, approved=True)

class ReviewCreate(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    def perform_create(self, serializer):
        game_id = self.kwargs['game_id']
        game = get_object_or_404(Game, pk=game_id)
        serializer.save(game=game)

class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class GameDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    def get(self, request, pk):
        game = get_object_or_404(Game, pk=pk)
        reviews = Review.objects.filter(game=game, approved=True)
        return render(request, 'games/game_detail.html', {'game': game, 'reviews': reviews})
#def index(request):
#   return HttpResponse("Welcome to the Game Review Platform")
"""