from rest_framework import serializers


class CompetitionSingleResultSerializer(serializers.Serializer):
    position = serializers.IntegerField()
    user_name = serializers.CharField()
    flight_time = serializers.FloatField()
    command_name = serializers.CharField()


class CompetitionResultResponseSerializer(serializers.Serializer):
    user_result = CompetitionSingleResultSerializer()
    other_results = CompetitionSingleResultSerializer(many=True)
