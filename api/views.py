from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .models import ResultEntry
from .serializers import CompetitionResultResponseSerializer


class CompetitionResultView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        competition = request.data.get("competition")
        user_name = request.data.get("user_name")
        scenario = request.data.get("scenario")
        limit = request.query_params.get("limit", 9)

        try:
            limit = int(limit)
        except ValueError:
            limit = 9

        if not all([competition, user_name, scenario]):
            return Response(
                {"error": "Missing fields"}, status=status.HTTP_400_BAD_REQUEST
            )

        queryset = ResultEntry.objects.filter(
            competition=competition, scenario=scenario, false_start=False
        ).order_by("flight_time")

        entries = list(queryset)
        user_result = next(
            (entry for entry in entries if entry.user_name == user_name), None
        )

        if not user_result:
            return Response(
                {"error": "User result not found"}, status=status.HTTP_404_NOT_FOUND
            )

        user_position = entries.index(user_result) + 1

        # Подготовка результатов
        user_data = {
            "position": user_position,
            "user_name": user_result.user_name,
            "flight_time": user_result.flight_time,
            "command_name": user_result.command_name,
        }

        other_results = []
        for idx, entry in enumerate(entries):
            if entry.pk != user_result.pk:
                other_results.append(
                    {
                        "position": idx + 1,
                        "user_name": entry.user_name,
                        "flight_time": entry.flight_time,
                        "command_name": entry.command_name,
                    }
                )
            if len(other_results) >= limit:
                break

        response_data = {"user_result": user_data, "other_results": other_results}

        serializer = CompetitionResultResponseSerializer(response_data)
        return Response(serializer.data)
